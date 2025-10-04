# Installation
Package is available on pypi and can be installed with `pip install graphstate-opt`. 

# Optional additional requirements
MOSEK could be used for solving the ILP formulation. MOSEK requires an additional step of download and activation of license file. Mosek can be installed via `pip install mosek` or `pip install "graphstate-opt[mosek]"`. Information about mosek license can be found here: <https://docs.mosek.com/11.0/licensing/quickstart.html>.

# Codes for finding the MER for a given input graph  
The folder optimizer has all the files for optimisation  
`edm_sa.py` and `edm_sa_ilp.py` are the two files that can be used to find the MERs. They take in: `G_in`: a `networkx` graph, `k_max`: maximum iterations and `initial_temp`: the initial temperature.  
- `edm_sa` is the function for implementing simulated annealing approach for finding MERs. This is a heuristic algorithm that can go up to graphs with 100 vertices.  
- `edm_sa_ilp(G_in, k_max, temp)` is the function for running the `SA+ILP` algorithm. We use it to find MERs for graphs up to 16 vertices.  
- `edm_ilp.py` is the source code for the `SA+ILP` algorithm that implements the ILP part of the `SA+ILP` algorithm  

# Edge-minimisation folder
The edge minimisation folder contains the files that can be used to 
- Generate bounded-degree (BD) and Erdos-Renyi (ER) graphs using `gen_bd.py` and `gen_er.py` files respectively.
- Run edge-minimisation of BD and ER graph using `edm_bd_opt.py` and `edm_bd_opt.py` files respectively.
- `plot_bd.py` and `plot_er.py` files for plotting the results for BD and ER graphs respectively.
- The files that start with `grgs_sampling.py` is for sampling gRGS. `grgs_comparison.py` is to analyse and plot the effects of varying fusion probabilities on the resources required to create a gRGS state.
- `weighted_edm.py` shows a use case of the weighted-edge minimization for distributing graph states in a network. It shows the input graph and the final optimized graph

# The tutorial file
`tutorial-1.ipynb` is the file that shows how the aforementioned functions could be used to find MERs. It plots the input graph, approximate MER from `SA` and the exact MER from `SA+ILP`. It also prints the runtime of the `SA+ILP` and `ILP` algorithms.

# Data files
Data files can be found at [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15534839.svg)](https://doi.org/10.5281/zenodo.15534839) and should be put in the folder `edge_minimisation` so that the python files can access the data.
