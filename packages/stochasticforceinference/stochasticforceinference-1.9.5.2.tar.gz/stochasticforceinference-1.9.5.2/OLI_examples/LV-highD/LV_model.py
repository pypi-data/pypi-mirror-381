"""
"""

import jax.numpy as jnp
import numpy as np

def generate_sparse_LV(dim, interaction_density=0.3, interaction_strength_range=(0.3, 1.0),
                        self_interaction_range=(0.9, 1.2), seed=None):
    """
    Generate sparse Lotka–Volterra dynamics with a nontrivial steady state.

    Args:
        dim: Dimension of the system (number of species).
        interaction_density: Fraction of off-diagonal terms that are nonzero.
        interaction_strength_range: Range of absolute values of interaction coefficients (off-diagonal).
        self_interaction_range: Range of negative diagonal values (-alpha_i for self-regulation).
        seed: Random seed (int or PRNGKey).

    Returns:
        r: jnp.array, intrinsic growth rates (dim,)
        A: jnp.array, interaction matrix (dim, dim)
        D: jnp.array, constant diffusion matrix (dim, dim)
        x0: jnp.array, steady-state population (dim,)
    """
    rng = np.random.default_rng(seed)

    # 1. Generate sparse interaction matrix
    A = np.zeros((dim, dim))
    for i in range(dim):
        A[i, i] = -rng.uniform(*self_interaction_range)  # strong self-limitation
        for j in range(dim):
            if i != j and rng.random() < interaction_density:
                strength = rng.uniform(*interaction_strength_range)
                sign = rng.choice([-1, 1])
                A[i, j] = sign * strength

    # 2. Choose a random positive steady state x0
    x0 = rng.uniform(0.5, 1.5, size=(dim,))

    # 3. Set r to ensure steady state: r = -A @ x0
    r = -A @ x0

    # 4. Constant diffusion matrix
    D = 0.002 * jnp.eye(dim)

    return jnp.array(r), jnp.array(A), jnp.array(D), jnp.array(x0)

dim = 100
r, A, D, x0 = generate_sparse_LV(dim, interaction_density=0.02, seed=42)


theta_force = jnp.array([],dtype=float)

from jax import jit
#key= random.key(4)
#key, subkey1, subkey2 = random.split(key,3)
#A = mag * random.bernoulli(subkey1, p = 0.15, shape=(dim,dim)).astype(float) + jnp.eye(dim)
#B = 1. + random.normal(subkey2,shape=(dim,))**2
@jit
def force_LV(x,theta):
    return A @ jnp.exp(x) + r
    
initial_position = jnp.zeros(dim) - 0.

# Uninitialized system to be used elsewhere
from SFI.SFI_Langevin import OverdampedLangevinProcess
LV_Model = OverdampedLangevinProcess(force_LV,D) 

