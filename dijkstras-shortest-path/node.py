import math

class Node:
  def __init__(self, tag):
    self.tag = tag
    self.edges = {}
    self.min_distance = math.inf

  def __lt__(self, other_node):
    return self.min_distance < other_node.min_distance

  def add_edge(self, to_node, length):
    self.edges[to_node] = length

  def get_destinations(self):
    return self.edges.keys()

  def edge_length(self, to_node):
    return self.edges.get(to_node)

  def push_min_distance(self, distance):
    self.min_distance = min(distance, self.min_distance)
