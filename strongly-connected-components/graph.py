import copy

class Graph:
  def __init__(self):
    self.data = {}
    self.visited = {}
    self.finished = {}
    self.nodes = set()

  def get_nodes(self):
    return copy.deepcopy(list(self.nodes))

  def add_edge(self, from_node, to_node):
    self.data[from_node] = self.data.get(from_node) or []
    self.data[from_node].append(to_node)
    self.add_node(from_node)
    self.add_node(to_node)

  def add_node(self, node):
    self.nodes.add(node)

  def connected_nodes(self, from_node):
    return self.data.get(from_node) or []

  def visit(self, node):
    self.visited[node] = True

  def is_visited(self, node):
    return self.visited.get(node) == True

  def finish(self, node):
    self.finished[node] = True

  def is_finished(self, node):
    return self.finished.get(node) == True

  def delete_node(self, node):
    if node in self.data: self.data.pop(node)
