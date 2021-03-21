class TspCache():
  def __init__(self, first_node):
    self.data = {}
    self.fst = first_node

  def store(self, nodes_set, to_node, value):
    set_key = self.__set_key(nodes_set)
    if self.data.get(set_key) is None: self.data[set_key] = {}
    self.data[set_key][to_node] = float(value)

  def fetch(self, nodes_set, to_node):
    if (nodes_set == set([self.fst]) and to_node == self.fst): return 0.0
    set_key = self.__set_key(nodes_set)
    return (self.data.get(set_key) or {}).get(to_node) or float('inf')

  def __set_key(self, nodes_set):
    return ':'.join(map(str, sorted(nodes_set)))

class TspBitmaskCache():
  def __init__(self, first_node, size1, size2):
    self.data = self.__array(size1, size2)
    self.fst = first_node

  def store(self, nodes_set, to_node_str, value):
    set_key = self.__set_key(nodes_set)
    to_node = int(to_node_str)
    self.data[set_key][to_node] = float(value)

  def fetch(self, nodes_set, to_node_str):
    if (nodes_set == set([self.fst]) and to_node_str == self.fst): return 0.0
    set_key = self.__set_key(nodes_set)
    to_node = int(to_node_str)
    return self.data[set_key][to_node] or float('inf')

  def __array(self, size1, size2):
    return [[None for y in range(size2)] for x in range(size1)]

  def __set_key(self, nodes_set):
    key = 0
    for num in list(map(int, list(nodes_set))):
      key = key | 1 << num
    return key

class EuclideanCache():
  def __init__(self):
    self.data = {}

  def store(self, tag1, tag2, value):
    key = self.__key(tag1, tag2)
    self.data[key] = float(value)

  def fetch(self, tag1, tag2):
    key = self.__key(tag1, tag2)
    return self.data.get(key) or None

  def __key(self, tag1, tag2):
    prefix = min(tag1, tag2)
    suffix = max(tag1, tag2)
    return '' + prefix + ':' + suffix
