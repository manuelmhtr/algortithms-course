class Subset:
  def __init__(self, tag):
    self.tag = tag
    self.parent = tag
    self.rank = 0

  def increase_rank(self):
    self.rank += 1

  def join(self, parent):
    self.parent = parent

  def is_root(self):
    return self.parent == self.tag

class Union:
  def __init__(self, collection):
    self.collection = collection
    self.size = len(collection)

  def get_group(self, tag):
    node = self.collection[tag]
    while not node.is_root():
      node = self.collection[node.parent]
    return node.parent

  def join(self, tag1, tag2):
    group1 = self.get_group(tag1)
    group2 = self.get_group(tag2)
    if group1 == group2: return

    node1 = self.collection[group1]
    node2 = self.collection[group2]
    self.size -= 1

    if node1.rank > node2.rank:
      node2.join(node1.tag)
    elif node1.rank < node2.rank:
      node1.join(node2.tag)
    else:
      node2.join(node1.tag)
      node1.increase_rank()
