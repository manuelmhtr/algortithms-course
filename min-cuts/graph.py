import random

class Graph:
  def __init__(self, data):
    self.graph = dict(data)
    self.nodes = set(self.graph.keys())
    self.edges = self.calculate_edges()

  def calculate_edges(self):
    edges = []
    iterated_nodes = set()
    for node1 in self.graph.keys():
      iterated_nodes.add(node1)
      for node2 in self.graph[node1]:
        if not node2 in iterated_nodes: edges.append([node1, node2])
    return edges

  def min_cut(self):
    if len(self.nodes) <= 2:
      node = list(self.nodes)[0]
      return len(self.valid_nodes(node, self.graph[node]))

    self.contract(self.random_edge())
    return self.min_cut()

  def random_edge(self):
    edge = None
    while not self.is_valid_edge(edge):
      rand_edge = self.edges.pop(random.randrange(len(self.edges)))
      edge = [
        self.get_node(rand_edge[0]),
        self.get_node(rand_edge[1])
      ]
    return edge

  def is_valid_edge(self, edge):
    if not edge: return False
    return edge[0] != edge[1]

  def is_node(self, value):
    return value in self.nodes

  def get_node(self, node):
    return node if self.is_node(node) else self.get_node(self.graph[node])

  def contract(self, edge):
    node1, node2 = edge
    node2_values = self.graph[node2]
    self.nodes.remove(node2)
    self.graph[node2] = node1
    self.graph[node1].extend(self.valid_nodes(node1, node2_values))

  def valid_nodes(self, from_node, to_nodes):
    valids = list(map(lambda n: self.get_node(n), to_nodes))
    return list(filter(lambda n: n != from_node, valids))
