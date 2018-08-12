import sys
import ast

from .solver import Solver

def read_stdin():
    big_lst = sys.stdin.readlines()
    big_lst = [ ast.literal_eval(lst.strip()) for lst in big_lst]
    return big_lst

def main():
    adj_matrix = [
        [1, 1, 0, 0 , 0],
        [1, 1, 1, 0 , 0],
        [0, 1, 1, 1 , 1],
        [0, 0, 1, 1 , 0],
        [0, 0, 1, 0 , 1]
    ]
    solver = Solver(adj_matrix)
    solver.solve('MIP')
    print('Solved in {:.1} seconds'.format(solver.time))
    print('Number of variables =', solver.nb_variables)
    print('Number of constraints =', solver.nb_constraints)
    print("Minimum of {} colors are needed".format(solver.nb_colors))
    print(solver.solution)


if __name__ == '__main__':
    main()
