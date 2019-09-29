# mangrove-plots
a package for visualizing statistics over hierarchically structured data

## What is a banyan plot?

A banyan plot is a 3d visualization of hierarchically structured data, where each node is associated with some value (e.g. a count), and the values of nodes are determined by some relationship with their neighbors. The particular use case that motivates this repo is where the count of a parent node is the sum of the counts over its children. As far as I can determine, this kind of visualization does not currently exist, and I am the inventor of it. However, most of the pieces of the visualization are already existing.

The name "banyan plot" is inspired by the root systems of banyan trees. The geometry of a banyan plot is achieved by mapping mapping nodes to half-spheres, and edges to truncated parabolas. 

## MVP

The minimal viable product, and the current target of development, is a Jupyter notebook which produces a banyan plot of a set of data.

Dependencies (besides those listed above): 
* networkx (for network data and layout algorithms)
* plotly (for visualization)


## status
* dev environment: jupyter notebook in python3, setup.sh committed to repo for easy reproduction
* dev dataset: a mini-network is defined within the notebook
* settled on layout from networkx package
* started mapping from 2D layout to 3D contour plot
* investigating edges
* investigating 3D annotations


