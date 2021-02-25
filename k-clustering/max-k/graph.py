import os, sys, inspect
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from itertools import combinations
from unionfind import Subset, Union

def neighbors_masks(bits):
  masks = [1 << i for i in range(bits)]
  combs = combinations(masks, 2)
  for (a, b) in combs:
    masks.append(a | b)
  masks.sort()
  return masks

class Node(Subset):
  masks = neighbors_masks(24)

  def __init__(self, tag):
    super().__init__(tag)

  def get_neighbors(self):
    return list(map(lambda x: x ^ self.tag, self.masks))
