# CS 111 Final Project
## BYU Fall 2026

This repository hosts a record of my final coding project.

### Project Goals

1. Build a `networkx` wrapper to simulate different dynamical systems on networks.

### Dependencies:

1. `networkx` for network generation.
2. `numpy` for matrix and vector operations.
3. `matplotlib` for visualizations.

### Resources:

1. _Networks_, 2E by Mark Newman.

### Work Log

| Date | Start Time | Duration | Description |
| --- | --- | --- | --- |
| 2025-11-02 | 20:28 | 1h 30m | initialized github repo and project workflow, including script to update work log. Outlined project plan: Resources, Goals, To-Do |
| 2025-11-03 | 01:17 | 1h 00m | Defined the mathematical model that I am going to be using for this project. Identified biologically plausible values for the model parameters. Researched relevant numerical methods that may be of use. |
| 2025-11-05 | 13:32 | 2h | Implemented my first LIF simulation for a single neuron. |
| 2025-11-10 | 12:55 | 1h 30m | Introduced random noise in the current of my single-neuron LIF model. Implemented Gaussian smoothing to the spike train. |
| 2025-11-13 | 19:51 | 3h | Attempted to implement an LIF model for a network of neurons. Wrote the math to use and attempted the simulation but its incredibly finicky and unstable. Will need to do more research to see what others have done before. |
| 2025-12-09 | 10:00 | 8h | Reworked project scope and goals. Decided to build network analysis tool to simulate dynamical systems on networks. Built both `simulate` and `diffuse` simulation methods for a graph object, and ran some analyses with them. Used what I learned from previous exploration|
Last updated: 2025-12-09T18:14:15.733844
