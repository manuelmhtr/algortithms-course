from heap import Heap
from node import Node
from pathlib import Path

def read_file(rel_path):
  full_path = Path(__file__).parent / rel_path
  return open(full_path, 'r').read()

def add_edge(g, from_node, to_node, cost):
  node = g.get(from_node) or Node(from_node)
  node.add_edge(to_node, cost)
  g[from_node] = node

def get_graph(rel_path):
  g = {}
  rows = read_file(rel_path).strip().split('\n')[1:]

  for row in rows:
    from_node, to_node, cost = row.strip().split(' ')
    add_edge(g, from_node, to_node, cost)
    add_edge(g, to_node, from_node, cost)

  return g

def prims_mst(input_path):
  visited = []
  mst_length = 0

  graph = get_graph(input_path)
  source_node = list(graph.values())[0]
  source_node.push_min_cost(0)

  add_to_visited(visited, graph, source_node)

  pending = Heap(list(graph.values()))

  while pending.has_items():
    new_node = pending.pop()
    mst_length += new_node.min_cost
    add_to_visited(visited, graph, new_node)
    pending.update()

  print(mst_length)

def add_to_visited(visited, graph, node):
  visited.append(node.tag)
  graph.pop(node.tag)

  for to_node in node.get_destinations():
    if to_node in visited: continue
    cost = node.edge_cost(to_node)
    graph[to_node].push_min_cost(cost)

prims_mst('./input.txt')
