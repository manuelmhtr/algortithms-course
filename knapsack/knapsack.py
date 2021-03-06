class Item:
  def __init__(self, tag, value, weight):
    self.tag = tag
    self.value = int(value)
    self.weight = int(weight)

  def __lt__(self, other):
    return self.tag < other.tag

class Cache:
  def __init__(self, default):
    self.data = {}
    self.default = default

  def set_value(self, tag, weight, value):
    if self.data.get(tag) is None:
      self.data[tag] = {}
    self.data[tag][weight] = value

  def get_value(self, tag, weight):
    return (self.data.get(tag) or {}).get(weight) or self.default

class IterativeKnapsack:
  def __init__(self, items, max_weight):
    self.cache = Cache(0)
    self.items = items
    self.max_weight = max_weight

  def max_value(self):
    self.memoize()
    return self.cache.get_value(self.items[-1].tag, self.max_weight)

  def memoize(self):
    for item in self.items:
      for w in range(0, self.max_weight + 1):
        not_include = self.cache.get_value(item.tag - 1, w)
        if w < item.weight:
          self.cache.set_value(item.tag, w, not_include)
        else:
          max_value = max(
            not_include,
            item.value + self.cache.get_value(item.tag - 1, w - item.weight)
          )
          self.cache.set_value(item.tag, w, max_value)

class RecursiveKnapsack:
  def __init__(self, items, max_weight):
    self.cache = Cache(None)
    self.items = items
    self.max_weight = max_weight

  def get_item(self, tag):
    if (tag >= 1): return self.items[tag - 1]

  def max_value(self):
    return self.find_max_value(self.items[-1].tag, self.max_weight)

  def find_max_value(self, tag, weight):
    cached = self.cache.get_value(tag, weight)
    if (cached is not None): return cached

    item = self.get_item(tag)
    max_value = self.calc_max_value(item, weight)
    self.cache.set_value(tag, weight, max_value)
    return max_value

  def calc_max_value(self, item, weight):
    if (item is None): return 0
    not_include = self.find_max_value(item.tag - 1, weight)

    if weight < item.weight: return not_include

    include = item.value + self.find_max_value(item.tag - 1, weight - item.weight)
    return max(include, not_include)
