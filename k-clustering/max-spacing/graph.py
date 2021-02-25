import os, sys, inspect
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from unionfind import Subset, Union

class Edge:
  def __init__(self, from_node, to_node, cost):
    self.from_node = from_node
    self.to_node = to_node
    self.cost = int(cost)

  def __lt__(self, other):
    return self.cost < other.cost

class Node(Subset):
  def __init__(self, tag):
    super().__init__(tag)
