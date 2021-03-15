from copy import deepcopy

class FloydWarshall:
  def __init__(self, graph):
    self.graph = graph
    self.n = len(graph.nodes)
    self.before = {}
    self.after = {}

  def memoize(self, i, j, value):
    if self.after.get(i) is None:
      self.after[i] = {}
    self.after[i][j] = value

  def get_value(self, i, j):
    value = (self.before.get(str(i)) or {}).get(str(j))
    return value or self.graph.distance(i, j)

  def shortest_path(self):
    self.find_all_paths()
    self.negative_cycles()
    if self.negative_cycles:
      return None
    return self.before

  def negative_cycles(self):
    for i in range(1, self.n + 1):
      if get_value(i, i) < 0: return True
    return False

  def find_all_paths(self):
    for k in range(1, self.n + 1):
      for i in self.graph.negative_nodes:
        for j in self.graph.negative_nodes:
          value = min(
            self.get_value(i, j),
            self.get_value(i, k) + self.get_value(k, j)
          )
          self.memoize(i, j, value)
      self.before = deepcopy(self.after)
      self.after = {}
