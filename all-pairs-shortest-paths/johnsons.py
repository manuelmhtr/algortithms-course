from bellmanford import BellmanFord

class Johnsons:
  def __init__(self, graph):
    self.graph = graph
    self.node_weights = None

  def shortest_path(self):
    self.all_shortest_paths()
    if self.node_weights:
      return min(list(self.node_weights.values()))

  def all_shortest_paths(self):
    self.calculate_node_weights()

  def calculate_node_weights(self):
    zero_node = '0'
    self.add_zero_node(zero_node)
    self.node_weights = BellmanFord(self.graph, zero_node).shortest_paths()

  def add_zero_node(self, node_name):
    other_nodes = list(self.graph.nodes)
    for node in other_nodes:
      self.graph.add_edge(node_name, node, 0)
