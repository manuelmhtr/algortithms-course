import math

class Node:
  def __init__(self, tag):
    self.tag = tag
    self.edges = {}
    self.min_cost = math.inf

  def __lt__(self, other_node):
    return self.min_cost < other_node.min_cost

  def add_edge(self, to_node, cost):
    self.edges[to_node] = int(cost)

  def get_destinations(self):
    return self.edges.keys()

  def edge_cost(self, to_node):
    return self.edges.get(to_node)

  def push_min_cost(self, new_cost):
    self.min_cost = min(new_cost, self.min_cost)
