class PathGraph:
  def __init__(self, nodes):
    self.nodes = nodes
    self.max_weights = None

  def node(self, index):
    return self.nodes[index - 1]

  def max_weight(self):
    if self.max_weights: return self.partial_max_weight(len(self.nodes))

    length = len(self.nodes) + 1
    self.max_weights = [None] * length
    self.max_weights[0] = (None, 0)
    self.max_weights[1] = (None, self.node(1))

    for i in range(2, length):
      w1 = self.partial_max_weight(i - 1)
      w2 = self.partial_max_weight(i - 2) + self.node(i)
      if w1 > w2:
        self.max_weights[i] = (i - 1, w1)
      else:
        self.max_weights[i] = (i - 2, w2)

    return self.partial_max_weight(len(self.nodes))

  def partial_max_weight(self, index):
    return self.max_weights[index][1]

  def max_weight_set(self):
    self.max_weight()
    return self.find_set(len(self.nodes))

  def find_set(self, index):
    next_index = self.max_weights[index][0] or index
    diff = index - next_index
    if diff == 1: return self.find_set(next_index)
    if diff == 2: return self.find_set(next_index) + [index]
    return [index]
