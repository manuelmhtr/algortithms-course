from pathlib import Path
from graph import Edge, Node, Union

def get_input(input_path):
  full_path = Path(__file__).parent / input_path
  file = open(full_path, 'r')
  return file.read().strip().split('\n')[1:]

def get_graph(input_path):
  edges = []
  nodes = {}
  for row in get_input(input_path):
    from_node, to_node, cost = row.split(' ')
    edges.append(Edge(from_node, to_node, cost))
    if (not nodes.get(from_node)): nodes[from_node] = Node(from_node)
    if (not nodes.get(to_node)): nodes[to_node] = Node(to_node)
  return (nodes, edges)

def krukals_mst(nodes, edges):
  mst = []
  edges.sort(reverse=True)
  union = Union(nodes)

  while union.size > 1:
    edge = edges.pop()
    parent1 = union.get_group(edge.from_node)
    parent2 = union.get_group(edge.to_node)
    if (parent1 == parent2): continue

    mst.append(edge)
    union.join(parent1, parent2)
  return mst

def max_spacing(input_path, clusters):
  nodes, edges = get_graph(input_path)
  mst = krukals_mst(nodes, edges)

  mst.sort(reverse=True)
  return mst[clusters - 2].cost

print(max_spacing('./input.txt', 4))
