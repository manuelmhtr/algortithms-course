from math import sqrt
from cache import EuclideanCache

class Node():
  def __init__(self, tag, x, y):
    self.tag = str(tag)
    self.x = float(x)
    self.y = float(y)

class Graph():
  def __init__(self):
    self.nodes = {}
    self.node_tags = set()
    self.cache = EuclideanCache()

  def add_node(self, node):
    tag = node.tag
    self.nodes[tag] = node
    self.node_tags.add(tag)

  def distance(self, tag1, tag2):
    cached = self.cache.fetch(tag1, tag2)
    if cached: return cached
    value = self.__calculate_distance(tag1, tag2)
    self.cache.store(tag1, tag2, value)
    return value

  def __calculate_distance(self, tag1, tag2):
    node1 = self.nodes[tag1]
    node2 = self.nodes[tag2]
    compX = pow(node1.x - node2.x, 2)
    compY = pow(node1.y - node2.y, 2)
    return sqrt(compX + compY)
