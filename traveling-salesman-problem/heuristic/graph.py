from math import sqrt

class Node():
  def __init__(self, tag, x, y):
    self.tag = str(tag)
    self.x = float(x)
    self.y = float(y)

class Graph():
  def __init__(self):
    self.nodes = {}
    self.node_tags = set()
    self.non_visited = []

  def add_node(self, node):
    tag = node.tag
    self.nodes[tag] = node
    self.node_tags.add(tag)
    self.non_visited.append(node)

  def visit_node_at_index(self, index):
    node = self.non_visited.pop(index)
    return node

  def distance(self, tag1, tag2, squared = None):
    return sqrt(squared or self.squared_distance(tag1, tag2))

  def squared_distance(self, tag1, tag2):
    node1 = self.nodes[tag1]
    node2 = self.nodes[tag2]
    compX = pow(node1.x - node2.x, 2)
    compY = pow(node1.y - node2.y, 2)
    return compX + compY
