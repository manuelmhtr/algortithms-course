class Item:
  def __init__(self, tag, value, weight):
    self.tag = tag
    self.value = int(value)
    self.weight = int(weight)

  def __lt__(self, other):
    return self.tag < other.tag

class Cache:
  def __init__(self):
    self.data = {}

  def set_value(self, tag, weight, value):
    if self.data.get(tag) is None:
      self.data[tag] = {}
    self.data[tag][weight] = value

  def get_value(self, tag, weight):
    return (self.data.get(tag) or {}).get(weight) or 0
