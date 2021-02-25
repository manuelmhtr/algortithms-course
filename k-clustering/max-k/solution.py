from pathlib import Path
from graph import Node, Union

def get_input(input_path):
  full_path = Path(__file__).parent / input_path
  file = open(full_path, 'r')
  return file.read().strip().split('\n')[1:]

def get_nodes(input_path):
  nodes = {}
  for row in get_input(input_path):
    tag = int(row.replace(' ', ''), 2)
    nodes[tag] = Node(tag)
  return nodes

def max_k(input_path):
  nodes = get_nodes(input_path)
  union = Union(nodes)

  for node in nodes.values():
    neighbors = node.get_neighbors()
    for neighbor in neighbors:
      neighbor_node = nodes.get(neighbor)
      if (neighbor_node is None): continue
      union.join(node.tag, neighbor_node.tag)

  return union.size

print(max_k('./input.txt'))
