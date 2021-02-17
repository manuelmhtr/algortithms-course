import heapq

class Heap:
  def __init__(self, nodes):
    self.data = [(node.min_cost, node) for node in nodes]
    heapq.heapify(self.data)

  def pop(self): 
    return heapq.heappop(self.data)[1]

  def update(self):
    self.data = list(map(lambda node: (node[1].min_cost, node[1]), self.data))
    heapq.heapify(self.data)

  def has_items(self):
    return len(self.data) > 0
