from heap import Heap
from node import Node
from pathlib import Path

distances = {}
visited = []

def read_file(rel_path):
  full_path = Path(__file__).parent / rel_path
  return open(full_path, 'r').read()

def get_graph(rel_path):
  g = {}
  rows = read_file(rel_path).strip().split('\n')

  for row in rows:
    components = row.strip().split('\t')
    tag = components[0]
    node = Node(tag)
    edges = list(map(lambda n: n.split(','), components[1:]))

    for edge in edges:
      to_node, length = edge
      node.add_edge(to_node, int(length))

    g[tag] = node
  return g

def dijkstra(input_path, source):
  graph = get_graph(input_path)
  source_node = graph[source]
  source_node.push_min_distance(0)

  add_to_visited(graph, source_node)

  pending = Heap(list(graph.values()))

  while pending.has_items():
    new_node = pending.pop()
    add_to_visited(graph, new_node)
    pending.update()

  print(distances)
  print_main_distances(distances)

def add_to_visited(graph, node):
  distances[node.tag] = node.min_distance
  visited.append(node)
  graph.pop(node.tag)

  for to_node in node.get_destinations():
    if not distances.get(to_node) is None: continue
    new_distance = node.min_distance + node.edge_length(to_node)
    graph[to_node].push_min_distance(new_distance)

def print_main_distances(distances):
  default = 1000
  nodes = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
  values = list(map(lambda n: str(distances.get(str(n)) or default), nodes))
  print(','.join(values))

dijkstra('./input.txt', '1')
