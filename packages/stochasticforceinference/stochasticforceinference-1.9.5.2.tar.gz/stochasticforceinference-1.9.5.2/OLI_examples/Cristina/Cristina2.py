import os
os.environ["JAX_PLATFORMS"] = "cpu"  # Ensure JAX only uses the CPU, if your GPU doesn't have enough memory
import jax.numpy as jnp
import pickle
from jax import random,jit,vmap

# Import the package:
import sys
sys.path.append('../../core/')
from OverdampedLangevinInference import *

# I. Load the data:
metadata, column_headers, particle_indices, time_indices, xvals = SFI_data.load_trajectory_data('track20.csv',particle_column=1, time_column=5, state_columns=[-2,-1]) 
dt = metadata['dt']

track_numbers = set(particle_indices)
track_to_id = { p : i for i,p in enumerate(track_numbers) }
relabeled_tracks = jnp.array([  track_to_id[p] for i,p in enumerate(particle_indices) ])



data = StochasticTrajectoryData(xvals,time_indices,dt,particle_indices=relabeled_tracks)
print("Loaded data. Number of exploitable points:",data.Nparticles.sum())

# II. Perform SFI:

S = OverdampedLangevinInference(data,verbose=False,max_memory_gb=1.)

S.compute_diffusion_constant( method='Vestergaard' # Best with large measurement error 
                              #method='MSD' # Best with ideal data 
                              #method = 'WeakNoise',    # Best with large dt
                             )

# Define the basis:
import OLI_bases
force_b, force_grad_b = OLI_bases.basis_selector({ 'type' : 'polynomial', 'order' : 1},data.d,output="vector")


# Perform inference:
S.infer_force_linear(basis_linear =  force_b,basis_linear_gradient=force_grad_b,
                     mode='Strato',G_mode='shift',diffusion_method = 'Vestergaard', # Best with large measurement error 
                     #mode='Ito',G_mode='trapeze', # Best with ideal data or large delta t
                     ) 

S.compute_force_error()
S.print_report()

# Apply sparsification:
print("Applying sparse model selection:")
S.force_sparsifier.build_pareto_front(max_k=30, beam_width=4, 
                                      aic_patience=2, report_time=True, verbosity=1)
k, support, score, coeffs = S.force_sparsifier.select_by_ic("PASTIS",p_param=0.05)
S._update_force_coefficients(coeffs,support)
print(f"Results after sparsification: Nterms={len(S.force_support)} out of {S.force_sparsifier.p}")
S.compute_force_error()
S.print_report()



################################################################
##### III. Plot the results and compare to exact fields.   #####

# Prepare Matplotlib:
import matplotlib.pyplot as plt
fig_size = [12,8]
params = {'axes.labelsize': 12,
          'font.size':   12,
          'legend.fontsize': 10,
          'xtick.labelsize': 10,
          'ytick.labelsize': 10,
          'text.usetex': False,
          'figure.figsize': fig_size,
          }
plt.rcParams.update(params)
plt.clf()
fig = plt.figure(1)
fig.subplots_adjust(left=0.06, bottom=0.07, right=0.96, top=0.94, wspace=0.35, hspace=0.3)
H,W = 2,2

# Plot the whole trajectory (all components vs t):
plt.subplot(H,W,1)

plt.plot(data.t,data.X[:,0,:])
plt.ylabel(r"$x$")
plt.xlabel(r"$t$")
plt.title("Original data")

# plt.subplot(H,W,4)
# plt.title("Inferred parameters")
# coeffs = jnp.zeros(S.force_sparsifier.p)
# coeffs = coeffs.at[S.force_support].set(S.force_coefficients).reshape((dim+1,dim),order='F')
# plt.imshow(coeffs,cmap='RdBu',vmin=-2,vmax=2.)

# Use the inferred force and diffusion fields to simulate a new
# trajectory with the same times list, and plot it.
plt.subplot(H,W,2)
key = random.key(0)
Y = S.simulate_bootstrapped_trajectory(key,oversampling=20000)
data_bootstrap = StochasticTrajectoryData(*Y.output_trajectory())
plt.plot(jnp.arange(Y.data.shape[0])*Y.dt,Y.data[:,0,:])
plt.title("Simulated trajectory")

plt.suptitle("Stochastic Force Inference demo")
plt.show()



