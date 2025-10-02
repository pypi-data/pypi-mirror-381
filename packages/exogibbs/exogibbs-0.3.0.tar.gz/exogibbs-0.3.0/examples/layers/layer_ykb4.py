"""
Validation of Gibbs Minimization for Layered Systems 
===================================================================================

This example demonstrates and validates the ExoGibbs thermochemical equilibrium for the layered system

Updated to use the high-level API: exogibbs.api.equilibrium.equilibrium.
"""

from exogibbs.presets.ykb4 import chemsetup
from exogibbs.api.equilibrium import equilibrium_profile, EquilibriumOptions
import numpy as np
import jax.numpy as jnp
from jax import config

config.update("jax_enable_x64", True)


# Thermodynamic conditions
Pref = 1.0  # bar, reference pressure
Parr = jnp.logspace(-8, 2, 10)/Pref  # bar
Tarr = 1500*Parr**0.1


#chemical setup
chem = chemsetup()

##############################################################################
# Solve equilibrium via high-level API
# ------------------------------------
opts = EquilibriumOptions(epsilon_crit=1e-11, max_iter=1000)

res = equilibrium_profile(
    chem,
    Tarr,
    Parr,
    chem.element_vector_reference,
    Pref=Pref,
    options=opts,
)

##############################################################################
nk_result = res.n
print(nk_result)
