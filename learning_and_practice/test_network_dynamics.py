from network_dynamics import GraphDynamics
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt



if __name__ == '__main__':

    np.random.seed(122)

    # network of 50 nodes, gnp graph with random initial state vector
    n = 50
    G = nx.gnp_random_graph(n, 0.5)
    v0 = np.random.uniform(-0.5, 0.5, n)

    # intrinsic leaky term
    def f_intrinsic(x, t=None):
        return -1 * x

    # coupling rule:
    def f_couple(x, t=None):
        return 1*np.sin(x)

# set up the simulation object
    sim = GraphDynamics(
        G = G,
        v0 = v0,
        t0 = 0,
        dt = 0.01,
        tf = 100,
        f_intrinsic=[f_intrinsic],
        f_couple=[f_couple]
    )

    times = []
    states = []

    random_weights = np.random.choice([-1, 1], (n, n))
    sim.A = sim.A * random_weights

    for t, x in sim.simulate():
        times.append(t)
        states.append(x)

plt.plot(times, states)
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Node Dynamics')
plt.show()
