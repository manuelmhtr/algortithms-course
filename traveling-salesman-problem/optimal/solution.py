from pathlib import Path
from graph import Graph, Node
from tsp import TSPDynamicSolution, TSPBitmaskSolution

def read_file(input_path):
  full_path = Path(__file__).parent / input_path
  return open(full_path, 'r').read().strip().split('\n')[1:]

def get_graph(input_path):
  g = Graph()
  tag = 0
  for row in read_file(input_path):
    x, y = row.strip().split(' ')
    g.add_node(Node(tag, x, y))
    tag += 1
  return g

def tsp(input_path, Solution):
  graph = get_graph(input_path)
  return Solution(graph).shortest_tour()

print('#1:', tsp('./input-min.txt', TSPDynamicSolution))
print('#2:', tsp('./input.txt', TSPBitmaskSolution))
