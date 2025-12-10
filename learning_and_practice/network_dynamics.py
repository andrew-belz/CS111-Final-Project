import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

"""
This is meant to be a wrapper for the `networkx` library for use with dynamical systems on graphs.
"""

class GraphDynamics():

    def __init__(self, G: nx.Graph | nx.DiGraph | nx.MultiGraph | nx.MultiDiGraph, v0:list, 
                 t0:float, dt:float, tf:float=None, 
                 f_intrinsic:list=None, f_couple:list=None):
        """
        Initialize GraphDynamics object.
        
        :param self:
        :param G: `networkx` Graph object: Graph, DiGraph, MultiGraph, MultiDiGraph.
        :type G: nx.Graph
        :param v0: Initial state vector. Must be a column vector with number of components equal to nodes in G.
        :type v0: np.array
        :param t0: Start time. Must be greater than or equal to zero.
        :type t0: float
        :param tf: Stop time. Must be greater than t_0
        :type tf: float
        :param dt: Discrete time step. Must be less than (t_f - t_0).
        :type dt: float
        :param f_intrinsic: list of functions governing intrinsic node dynamics. Length is either number of nodes or 1.
        :type f_intrinsic: list
        :param f_couple: list of functions governing coupling dynamics. Either length is number of nodes or 1.
        :type f_couple: list
        """

        self.G = G
        self.v0 = np.array(v0)
        self.t0 = t0
        self.dt = dt
        self.tf = tf

        self.nodes = G.nodes
        self.edges = G.edges

        if f_couple and f_intrinsic:
            # make sure that f_intrinsic and f_couple are lists of length equal to the number of nodes
            if len(f_intrinsic) != len(G.nodes) and len(f_couple) != len(G.nodes) and len(f_intrinsic) != 1 and len(f_couple) != 1:
                print('Lengths of f_intrinsic and f_couple must be 1 or number of nodes.')
                return
            else:
                if len(f_intrinsic) == 1:
                    self.f_intrinsic = [f_intrinsic[0] for _ in range(len(G.nodes))]
                else:
                    self.f_intrinsic = f_intrinsic

                if len(f_couple) == 1:
                    self.f_couple = [f_couple[0] for _ in range(len(G.nodes))]
                else:
                    self.f_couple = [f_couple]
        else:
            self.f_couple = f_couple
            self.f_intrinsic = f_intrinsic



        # get adjacency and laplacian matrices
        # specifying node list keeps this robust to differences in ordering nodes
        self.A = nx.adjacency_matrix(G, nodelist=self.nodes).toarray()
        self.L = nx.laplacian_matrix(G, nodelist=self.nodes).toarray()

        # get a time array using given start, stop, step
        if tf is not None and isinstance(tf, float):
            steps = int(round((tf-t0)/dt))
            self.time_array = np.linspace(t0, tf, steps)
        else:
            self.time_array = None

# ==============================================================================================================
    def diffuse(self, k:float=1.0):
        """
        Return a generator for simulating network diffusion with the graph Laplacian L.
        If no final time tf is given then generates indefinitely.
        Forward Euler method: x_{t+dt} = I - k*dt*L @ x_t
        
        :param self:
        """

        try:
            # first step: define state transition matrix
            x = self.v0.copy()
            t = self.t0
            I = np.eye(self.L.shape[0])
            M = I - k * self.dt * self.L

            # check convergence criteria
            L_eigs = np.linalg.eigvals(self.L)
            if np.max(L_eigs) > 0 and k*self.dt >= 2/np.max(L_eigs):
                print('WARNING: system unstable.')

            yield t, x

        except Exception as e:
            print(f'An error occured at time {t}: {e}')
            return

        # iterate
        while True:
            # check to make sure we're respecting the stopping point, if given
            if self.tf is not None and t >= self.tf:
                break

            try:
                x = M @ x
                t += self.dt
                yield t, x
            except Exception as e:
                print(f'An error occured at time {t}: {e}')
                return

# ==============================================================================================================
    def simulate(self):
        """
        Gives graph dynamical system simulation generator using forward Euler method.
        Formula:
        x(t + dt) = x(t) + dt * h(x, A),

        where A is the adjacency matrix.
        """
        
        try:
            x = self.v0.copy()
            t = self.t0

            # make sure we actually have a system to simulate
            if not self.f_intrinsic:
                print('Error: no update function given.')
                return
            if not self.f_couple:
                print('Error: no coupling function given.')
                return


            # yield initial state
            yield t, x

            while self.tf is None or t < self.tf:

                try:
                    intrinsic = np.array([f(x[i], t) for i, f in enumerate(self.f_intrinsic)])
                    couple = np.array([f(x[i], t) for i, f in enumerate(self.f_couple)])

                    # general form of dynamical system with both intrinsic node dynamics and coupling dynamics
                    dxdt = intrinsic + self.A @ couple
                    
                    # forward Euler update rule
                    x = x + self.dt * dxdt
                    t = t + self.dt

                    # yield current state
                    yield t, x
                except Exception as e:
                    print(f'An error occured at time {t if t else 0}: {e}')
                    return

        except Exception as e:
            print(f'An error occured at time {t if t else 0}: {e}')
            return

# ==============================================================================================================
    def jacobian(self):
        """
        Generate the Jacobian matrix of a graph dynamical system.
        """

# ==============================================================================================================
    def fixed_points(self):
        """
        Return the fixed points (i.e. stead states) of a graph dynamical system via linearization.
        """
        
# ==============================================================================================================
    def limit_cycles(self):
        """
        Return the limit cycles of a graph dynamical system via linearization.
        """

# ==============================================================================================================
    def stability(self):
        """
        Analyze the stability of the fixed points of the linearized dynamical system.
        Returns fixed points and classification of fixed points.
        """

# ==============================================================================================================
    def synchronization(self):
        """
        Analyze the synchronization of the system near limit cycles of the linearized dynamical system.
        """

        