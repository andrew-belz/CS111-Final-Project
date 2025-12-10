import numpy as np
import networkx as nx
from network_dynamics import GraphDynamics
import matplotlib.pyplot as plt


if __name__ == '__main__':

    np.random.seed(122)
    n = 200
    p = [0.01 * i for i in range(100)]
    k_neighbors = 2

    std = []

    for i, prob in enumerate(p):
        state_std = []
        for _ in range(50):
            G = nx.watts_strogatz_graph(n, k_neighbors, prob)
            v0 = np.random.normal(0, 1/np.sqrt(n), n)
            t0 = 0.0
            tf = 20.0
            dt = 0.01

            sim = GraphDynamics(
                G = G,
                v0 = v0,
                t0 = t0,
                tf = tf,
                dt = dt
            )

            final_x = None

            for t, x in sim.diffuse(k = 0.1):
                final_x = x
            state_std.append(np.std(final_x))


        std.append(np.mean(state_std))

    plt.scatter(p, std)
    plt.title(f"Diffusion on Watts-Strogatz Graphs (N={n}, k={k_neighbors}): Spread by Rewiring Probability P", fontsize=16)
    plt.tight_layout()
    plt.show()