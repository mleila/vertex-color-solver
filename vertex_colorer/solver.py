import time

from .ip_solver import IPSolver
from .cp_solver import CPSolver
from .greedy_solver import GreedySolver
from .dp_solver import DPSolver


SOLVERS = {
    'IP': IPSolver,
    'CP': CPSolver,
    'Greedy': GreedySolver,
    'DP': DPSolver
}


class Graph:

    def __init__(self, adj_matrix):
        self.adj_matrix = adj_matrix
        self.vertices = range(len(adj_matrix))

    def adjacents(self):
        adj = []
        for idx, val in enumerate(self.adj_matrix):
            for inner_idx, item in enumerate(val):
                if item:
                    adj.append((idx, inner_idx))
        return adj


class Solver:

    def __init__(self, adj_matrix):
        self.graph = Graph(adj_matrix)
        self.solution = None

    def solve(self, solver_type='MIP'):
        solver = SOLVERS[solver_type](self.graph)
        ti = time.time()
        self.solution = solver.solve()
        tf = time.time()
        self.time = tf-ti
        self.nb_variables = solver.nb_variables
        self.nb_constraints = solver.nb_constraints
        self.nb_colors = solver.nb_colors

    def write_solution(self, fpath):
        pass

    def list_solvers(self):
        return SOLVERS.keys()
