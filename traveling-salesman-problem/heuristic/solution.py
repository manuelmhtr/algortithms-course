from pathlib import Path
from graph import Graph, Node
from tsp import TSPHeuristicSolution

def read_file(input_path):
  full_path = Path(__file__).parent / input_path
  return open(full_path, 'r').read().strip().split('\n')[1:]

def get_graph(input_path):
  g = Graph()
  for row in read_file(input_path):
    tag, x, y = row.strip().split(' ')
    g.add_node(Node(tag, x, y))
  return g

def tsp(input_path):
  graph = get_graph(input_path)
  return TSPHeuristicSolution(graph).shortest_tour()

print('#1:', tsp('./input-min.txt'))
print('#2:', tsp('./input.txt'))