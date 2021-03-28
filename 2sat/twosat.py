import os, sys, inspect
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir + '/../strongly-connected-components')
sys.path.append(os.path.join(parentdir, 'strongly-connected-components'))

from scc import SCC
from graph import Graph

class TwoSat():
  def __init__(self):
    self.graph = Graph()

  def is_satisfiable(self):
    sccs = SCC(self.graph).strongly_connected_components()
    return not self.__has_invalid_sccs(sccs)

  def add_clause(self, var1, var2):
    key1 = self.__var_key(var1)
    key2 = self.__var_key(var2)
    not_key1 = self.__var_key(self.__not(var1))
    not_key2 = self.__var_key(self.__not(var2))
    self.graph.add_edge(not_key1, key2)
    self.graph.add_edge(not_key2, key1)

  def __var_key(self, var):
    if var < 0: return var * -2 - 1
    return var * 2

  def __not(self, var):
    return var * -1

  def __not_key(self, var):
    if var % 2 == 0: return var - 1
    return var + 1

  def __has_invalid_sccs(self, sccs):
    for scc in sccs:
      for x in scc:
        # Negative X var cannot be in the same SCC
        if (self.__not_key(x) in scc):
          return True
    return False
