class Graph:
  def __init__(self):
    self.edges = {}
    self.nodes = set()
    self.negative_nodes = set()

  def add_edge(self, from_node, to_node, cost_str):
    cost = int(cost_str)
    if self.edges.get(from_node) is None:
      self.edges[from_node] = {}
    self.edges[from_node][to_node] = cost
    self.nodes.update([from_node, to_node])
    if cost < 0:
      self.negative_nodes.add(from_node)

  def get_node(self, node):
    return self.edges.get(node) or {}

  def distance(self, from_node, to_node):
    if from_node == to_node: return 0
    value = (self.edges.get(str(from_node)) or {}).get(str(to_node))
    if value is None: return float('inf')
    return value
