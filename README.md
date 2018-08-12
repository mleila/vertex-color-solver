# vertex-color-solver
Vertex Coloring is a well known problem in Operations Research where the goal is to find the minimum number of colores required to color vertices of an undirected graph such that no two adjacent vertices have the same color.

Several algorithmic paradigms can tackle the Vertex Coloring problem such as:

* Formulating the model as an Integer Linear Program (IP) and finding a solution using linear relaxations and branch & bound.
* Formulating the model as a Constraint Programming problem and finding solution by domain reduction (constraint propagation).
* Using Dynamic Programming
* Using a Greedy heuristic (suboptimal solutions)

Each approach has its merits and disadvantages. This package provides a collection of solvers that uses each of these approaches. Users can experiment with the different algorithms and figure out the best option the suits their problem.

I started by implementing the Integer Programming solver, the rest are in the pipeline.

## Install
```bash
git clone https://github.com/mleila/vertex-color-solver
pip install -e vertex-color-solver
```

## Usage
Import the solver
```python
from vertex_colorer.solver import Solver
```
pass an undirected graph represented as an adjacency matrix to the solver

```python
adj_matrix = [
	[1, 1, 0, 0, 0],
    [1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 0, 1, 1, 0],
    [1, 1, 1, 0, 1]
 ]
solver = Solver(adj_matrix)
```
![alt text](https://github.com/mleila/vertex-color-solver/blob/master/assets/undirected_graph.png)

choose the backend model/algorithm
```python
# use an Integer Programming approach
solver.solve('IP')
```

view solution
```python
 print(solver.solution)
 [[0, 1], [1, 2], [2, 1], [3, 0], [4, 0]]
```
where the solution is in the format [vertex index, color]
![alt text](https://github.com/mleila/vertex-color-solver/blob/master/assets/colored_undirected_graph.png)
