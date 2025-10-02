import jax.numpy as jnp
from jax import custom_vjp
from jax import jacrev
from jax import jit
from jax.lax import while_loop, stop_gradient
from jax.scipy.linalg import cho_factor
from jax.scipy.linalg import cho_solve
from functools import partial
from typing import Tuple, Callable

from exogibbs.api.chemistry import ThermoState
from exogibbs.optimize.core import _A_diagn_At
from exogibbs.optimize.core import _compute_gk
from exogibbs.optimize.vjpgibbs import vjp_temperature
from exogibbs.optimize.vjpgibbs import vjp_pressure
from exogibbs.optimize.vjpgibbs import vjp_elements



def solve_gibbs_iteration_equations(
    nk: jnp.ndarray,
    ntotk: float,
    formula_matrix: jnp.ndarray,
    b: jnp.ndarray,
    gk: jnp.ndarray,
    An: jnp.ndarray,
) -> Tuple[jnp.ndarray, float]:
    """
    Solve the Gibbs iteration equations using the Lagrange multipliers.
    This function computes the matrix and vector to solve the system of equations
    that arises from the Gibbs energy minimization problem.

    Args:
        nk: number of species vector (n_species,) for k-th iteration.
        ntotk: Total number of species for k-th iteration.
        formula_matrix: Formula matrix for stoichiometric constraints (n_elements, n_species).
        b: Element abundance vector (n_elements, ).
        gk: gk vector (n_species,) for k-th iteration.
        An: formula_matrix @ nk vector (n_elements, ).

    Returns:
        Tuple containing:
            - The pi vector (nspecies, ).
            - The update of the  log total number of species (delta_ln_ntot).
    """
    resn = jnp.sum(nk) - ntotk
    AnAt = _A_diagn_At(nk, formula_matrix)
    Angk = formula_matrix @ (gk * nk)
    ngk = jnp.dot(nk, gk)

    assemble_mat = jnp.block([[AnAt, An[:, None]], [An[None, :], jnp.array([[resn]])]])
    assemble_vec = jnp.concatenate([Angk + b - An, jnp.array([ngk - resn])])
    assemble_variable = jnp.linalg.solve(assemble_mat, assemble_vec)
    return assemble_variable[:-1], assemble_variable[-1]


def compute_residuals(
    nk: jnp.ndarray,
    ntotk: float,
    formula_matrix: jnp.ndarray,
    b: jnp.ndarray,
    gk: jnp.ndarray,
    An: jnp.ndarray,
    pi_vector: jnp.ndarray,
) -> float:

    ress = nk * (formula_matrix.T @ pi_vector - gk)
    ress_squared = jnp.dot(ress, ress)

    An_b = An - b
    resj_squared = jnp.dot(An_b, An_b)

    resn = jnp.sum(nk) - ntotk
    resn_squared = jnp.dot(resn, resn)
    return jnp.sqrt(ress_squared + resj_squared + resn_squared)

CEA_SIZE = 18.420681        # = -ln(1e-8)
LN_X_CAP = 9.2103404        # = -ln(1e-4)

def _cea_lambda(delta_ln_nk, delta_ln_ntot, ln_nk, ln_ntot, size=CEA_SIZE):
    # λ1: ensure |Δln n|<=0.4, |Δln n_k|<=2
    cap_ntot = 5.0 * jnp.abs(delta_ln_ntot)           # 1/0.4
    cap_sp   = jnp.max(jnp.abs(delta_ln_nk))
    denom1   = jnp.maximum(jnp.maximum(cap_ntot, cap_sp), 1e-300)
    lam1     = 2.0 / denom1

    # maintain x_k<=1e-4 if increasing when x_k<=1e-8
    ln_xk  = ln_nk - ln_ntot
    small  = (ln_xk <= -size) & (delta_ln_nk >= 0.0)
    denom2 = delta_ln_nk - delta_ln_ntot
    safe   = small & (denom2 > 0.0)
    cand   = ( -LN_X_CAP - ln_xk ) / denom2           # (-ln 1e-4 - ln xk)/(Δln nk - Δln n)
    lam2   = jnp.where(jnp.any(safe), jnp.min(jnp.where(safe, cand, jnp.inf)), jnp.inf)

    lam = jnp.minimum(1.0, jnp.minimum(lam1, lam2))
    # safe guard
    lam = jnp.clip(lam, 1e-6, 1.0)
    return lam

def update_all(
    ln_nk,
    ln_ntot,
    formula_matrix,
    b,
    T,
    ln_normalized_pressure,
    hvector,
    gk,
    An,
):

    pi_vector, delta_ln_ntot = solve_gibbs_iteration_equations(
        jnp.exp(ln_nk), jnp.exp(ln_ntot), formula_matrix, b, gk, An
    )
    delta_ln_nk = formula_matrix.T @ pi_vector + delta_ln_ntot - gk

    # relaxation and update
    #lam = 0.1  # need to reconsider
    lam = _cea_lambda(delta_ln_nk, delta_ln_ntot, ln_nk, ln_ntot)
    ln_ntot += lam * delta_ln_ntot
    ln_nk += lam * delta_ln_nk

    # computes new gk,An and residuals
    nk = jnp.exp(ln_nk)
    ntot = jnp.exp(ln_ntot)
    gk = _compute_gk(T, ln_nk, ln_ntot, hvector, ln_normalized_pressure)
    An = formula_matrix @ nk
    epsilon = compute_residuals(nk, ntot, formula_matrix, b, gk, An, pi_vector)
    return ln_nk, ln_ntot, epsilon, gk, An

def minimize_gibbs_core(
    state: ThermoState,
    ln_nk_init: jnp.ndarray,
    ln_ntot_init: float,
    formula_matrix: jnp.ndarray,
    hvector_func,
    epsilon_crit: float = 1.0e-11,
    max_iter: int = 1000,
) -> Tuple[jnp.ndarray, float, int]:
    """Compute log(number of species) by minimizing the Gibbs energy using the Lagrange multipliers method.

    Args:
        state: Thermodynamic state containing temperature, pressure, and element abundances.
        ln_nk_init: Initial log number of species vector (n_species,).
        ln_ntot_init: Initial log total number of species.
        formula_matrix: Stoichiometric formula matrix (n_elements, n_species).
        hvector: Chemical potential over RT vector (n_species,).
        epsilon_crit: Convergence tolerance for residual norm.
        max_iter: Maximum number of iterations allowed.

    Returns:
        Tuple containing:
            - Final log number of species vector (n_species,).
            - Final log total number of species.
            - Number of iterations performed.
    """

    hvector = hvector_func(state.temperature)

    def cond_fun(carry):
        _, _, _, _, epsilon, counter = carry
        return (epsilon > epsilon_crit) & (counter < max_iter)

    def body_fun(carry):
        ln_nk, ln_ntot, gk, An, _, counter = carry
        ln_nk_new, ln_ntot_new, epsilon, gk, An = update_all(
            ln_nk,
            ln_ntot,
            formula_matrix,
            state.element_vector,
            state.temperature,
            state.ln_normalized_pressure,
            hvector,
            gk,
            An,
        )
        return ln_nk_new, ln_ntot_new, gk, An, epsilon, counter + 1

    gk = _compute_gk(
        state.temperature,
        ln_nk_init,
        ln_ntot_init,
        hvector,
        state.ln_normalized_pressure,
    )
    An = formula_matrix @ jnp.exp(ln_nk_init)

    ln_nk, ln_tot, _, _, _, counter = while_loop(
        cond_fun, body_fun, (ln_nk_init, ln_ntot_init, gk, An, jnp.inf, 0)
    )
    return ln_nk, ln_tot, counter


# Only function and scalar options are non-differentiable.
# Array-valued args (init vectors, matrices) must NOT be in nondiff_argnums
# to avoid UnexpectedTracerError under vmap/jit.
def minimize_gibbs(
    state: ThermoState,
    ln_nk_init: jnp.ndarray,
    ln_ntot_init: float,
    formula_matrix: jnp.ndarray,
    hvector_func: Callable[[float], jnp.ndarray],
    epsilon_crit: float = 1.0e-11,
    max_iter: int = 1000,
) -> jnp.ndarray:
    """Compute log(number of species) by minimizing the Gibbs energy using the Lagrange multipliers method.

    Args:
        state: Thermodynamic state containing temperature, pressure, and element abundances.
        ln_nk_init: Initial natural log number of species vector (n_species,).
        ln_ntot_init: Initial natural log total number of species.
        formula_matrix: Stoichiometric formula matrix (n_elements, n_species).
        hvector_func: Function that returns chemical potential over RT vector (n_species,).
        epsilon_crit: Convergence tolerance for residual norm.
        max_iter: Maximum number of iterations allowed.

    Returns:
        Final log number of species vector (n_species,).
    """
    # Define an inner custom_vjp function that captures static arrays
    # (ln_nk_init, ln_ntot_init, formula_matrix) to avoid passing them as
    # arguments, which can become JAX Tracers under vmap/jit.
    @custom_vjp
    def _solve(inner_state: ThermoState, ln_nk0: jnp.ndarray, ln_ntot0: float) -> jnp.ndarray:
        ln_nk, _, _ = minimize_gibbs_core(
            inner_state,
            ln_nk0,
            ln_ntot0,
            formula_matrix,
            hvector_func,
            epsilon_crit,
            max_iter,
        )
        return ln_nk

    def _solve_fwd(inner_state: ThermoState, ln_nk0: jnp.ndarray, ln_ntot0: float):
        ln_nk, ln_ntot, _ = minimize_gibbs_core(
            inner_state,
            ln_nk0,
            ln_ntot0,
            formula_matrix,
            hvector_func,
            epsilon_crit,
            max_iter,
        )
        dfunc = jacrev(hvector_func)
        hdot = dfunc(inner_state.temperature)
        residuals = (ln_nk, hdot, inner_state.element_vector, ln_ntot)
        return ln_nk, residuals

    def _solve_bwd(res, g):
        ln_nk, hdot, element_vector, ln_ntot = res

        nk = jnp.exp(ln_nk)
        ntot_result = jnp.exp(ln_ntot)

        Bmatrix = _A_diagn_At(nk, formula_matrix)
        c, lower = cho_factor(Bmatrix)
        alpha = cho_solve((c, lower), formula_matrix @ g)
        beta = cho_solve((c, lower), element_vector)
        beta_dot_b_element = jnp.vdot(beta, element_vector)

        cot_T = vjp_temperature(
            g,
            nk,
            formula_matrix,
            hdot,
            alpha,
            beta,
            element_vector,
            beta_dot_b_element,
        )
        cot_P = vjp_pressure(g, ntot_result, alpha, element_vector, beta_dot_b_element)
        cot_b = vjp_elements(g, alpha, beta, element_vector, beta_dot_b_element)
        # No gradients for initialization arguments
        return (ThermoState(jnp.asarray(cot_T), jnp.asarray(cot_P), cot_b), None, None)

    _solve.defvjp(_solve_fwd, _solve_bwd)

    # Treat initial guesses as non-differentiable inputs
    ln_nk0 = stop_gradient(ln_nk_init)
    ln_ntot0 = stop_gradient(ln_ntot_init)
    return _solve(state, ln_nk0, ln_ntot0)


# Note: custom_vjp is defined inside minimize_gibbs to capture static arrays.
