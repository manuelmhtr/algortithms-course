import heapq

class MinHeap:
  def __init__(self):
    self.data = []
    self.size = 0

  def push(self, item):
    self.size += 1
    heapq.heappush(self.data, item)

  def pop(self):
    self.size -= 1
    return heapq.heappop(self.data)

  def min(self):
    return self.data[0] if self.size > 0 else float('inf')

class MaxHeap(MinHeap):
  def push(self, item):
    super().push(-1 * item)

  def pop(self):
    return -1 * super().pop()

  def max(self):
    return -1 * super().min()

class MedianHeap:
  def __init__(self):
    self.max_heap = MaxHeap()
    self.min_heap = MinHeap()

  def median(self):
    return self.max_heap.max()

  def push(self, item):
    if item > self.max_heap.max():
      self.min_heap.push(item)
    else:
      self.max_heap.push(item)
    self.rebalance_heaps()

  def rebalance_heaps(self):
    if (self.max_heap.size - self.min_heap.size) > 1:
      self.min_heap.push(self.max_heap.pop())
    elif (self.min_heap.size - self.max_heap.size) > 0:
      self.max_heap.push(self.min_heap.pop())
