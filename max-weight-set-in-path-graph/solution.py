from pathlib import Path
from pathgraph import PathGraph

def get_nodes(input_path):
  full_path = Path(__file__).parent / input_path
  file = open(full_path, 'r')
  strings = file.read().strip().split('\n')[1:]
  return list(map(int, strings))

def max_weight(nodes, checks):
  graph = PathGraph(nodes)
  mws = graph.max_weight_set()
  results = list(map(lambda c: str(int(c in mws)), checks))
  return ''.join(results)

checks = [1, 2, 3, 4, 17, 117, 517, 997]
nodes = get_nodes('./input.txt')
print(max_weight(nodes, checks))
