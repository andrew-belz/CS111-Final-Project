import numpy as np
import networkx as nx
from network_dynamics import GraphDynamics
import matplotlib.pyplot as plt


if __name__ == '__main__':

    np.random.seed(122)
    n = 200
    p = [0.1 * i for i in range(10)]
    k_neighbors = 2

    fig, axes = plt.subplots(2, 5, figsize=(20, 8), sharex=True, sharey=True)
    axes = axes.flatten()

    for i, prob in enumerate(p):
        G = nx.watts_strogatz_graph(n, k_neighbors, prob)
        v0 = np.random.normal(0, 1/np.sqrt(n), n)
        t0 = 0
        tf = 100
        dt = 0.01

        sim = GraphDynamics(
            G = G,
            v0 = v0,
            t0 = t0,
            tf = tf,
            dt = dt
        )

        states = []
        times = []

        for t, x in sim.diffuse(k = 0.1):
            times.append(t)
            states.append(x)

        ax = axes[i]
        ax.set_title(f"p = {prob:.1f}")
        ax.plot(times, states, alpha=0.6, linewidth=0.8)
        
    # Add title
    fig.suptitle(f"Diffusion on Watts-Strogatz Graphs (N={n}, k={k_neighbors})", fontsize=16)
    plt.tight_layout()
    plt.show()
