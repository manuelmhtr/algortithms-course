from copy import deepcopy
from cache import TspCache, TspBitmaskCache
from itertools import combinations

class TSPDynamicSolution():
  def __init__(self, graph):
    self.graph = graph
    self.first_node = list(graph.node_tags)[0]
    self.new_cache = TspCache(self.first_node)
    self.cache = None

  def shortest_tour(self):
    for m in range(1, len(self.graph.nodes)):

      # Save some memory rotating caches
      self.cache = deepcopy(self.new_cache)
      self.new_cache = TspCache(self.first_node)
      print(m)

      for s in self.distinct_sets(m):
        for j in s:
          if (j == self.first_node): continue
          prev_set = s - set([j])
          self.new_cache.store(s, j, self.min_distance(prev_set, j))

    self.cache = deepcopy(self.new_cache)
    return self.min_distance(self.graph.node_tags, self.first_node)

  def min_distance(self, prev_set, j):
    min_value = float('inf')
    for k in prev_set:
      distance = self.cache.fetch(prev_set, k) + self.graph.distance(k, j)
      if distance < min_value: min_value = distance
    return min_value

  def distinct_sets(self, count):
    node_tags = self.graph.node_tags - set([self.first_node])
    sets = list(combinations(node_tags, count))
    return list(map(lambda s: set([self.first_node, *s]), sets))

class TSPBitmaskSolution(TSPDynamicSolution):
  def __init__(self, graph):
    self.graph = graph
    self.first_node = list(graph.node_tags)[0]
    self.cache = self.__cache()

  def shortest_tour(self):
    for m in range(1, len(self.graph.nodes)):
      print(m)
      for s in self.distinct_sets(m):
        for j in s:
          if (j == self.first_node): continue
          prev_set = s - set([j])
          self.cache.store(s, j, self.min_distance(prev_set, j))

    return self.min_distance(self.graph.node_tags, self.first_node)

  def __cache(self):
    n = len(self.graph.node_tags)
    return TspBitmaskCache(self.first_node, pow(2, n), n)
