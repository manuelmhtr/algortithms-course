import json
from copy import deepcopy

class BellmanFord():
  def __init__(self, graph, from_node):
    self.graph = graph
    self.from_node = from_node
    self.has_negative_cycle = None
    self.distances = {}

  def shortest_paths(self):
    self.has_negative_cycle = True
    k = len(self.graph.nodes) + 1
    last_str = None
    for i in range(0, k):
      self.iterate_paths()
      new_str = self.distances_hash()
      if (last_str == new_str):
        self.has_negative_cycle = False
        return self.distances
      last_str = deepcopy(new_str)
    return None

  def iterate_paths(self):
    for from_node in self.graph.nodes:
      current = self.distance(from_node)
      if current == float('inf'): continue
      edges = self.graph.get_node(from_node)
      for to_node in edges:
        total = current + edges[to_node]
        self.push_shortest_distance(to_node, current + edges[str(to_node)])

  def distances_hash(self):
    return json.dumps(self.distances, sort_keys=True)

  def distance(self, to_node):
    if to_node == self.from_node: return 0
    distance = self.distances.get(to_node)
    if distance is None: return float('inf')
    return distance

  def push_shortest_distance(self, to_node, distance):
    shortest = self.distance(to_node)
    if shortest > distance: self.distances[to_node] = distance
