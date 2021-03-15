from pathlib import Path
from graphs import Graph
from johnsons import Johnsons
from floydwarshall import FloydWarshall

def get_input(input_path):
  full_path = Path(__file__).parent / input_path
  file = open(full_path, 'r')
  return file.read().strip().split('\n')[1:]

def build_graph(input_path):
  strings = get_input(input_path)
  graph = Graph()
  for string in strings:
    from_node, to_node, cost = string.split(' ')
    graph.add_edge(from_node, to_node, cost)
  return graph

def floyd_warshall(input_path):
  graph = build_graph(input_path)
  return Johnsons(graph).shortest_path()

print('Graph 0:', floyd_warshall('./g0.txt'))
print('Graph 1:', floyd_warshall('./g1.txt'))
print('Graph 2:', floyd_warshall('./g2.txt'))
print('Graph 3:', floyd_warshall('./g3.txt'))
print('Large graph:', floyd_warshall('./large.txt'))
