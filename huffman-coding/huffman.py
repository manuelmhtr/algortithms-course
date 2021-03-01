import heapq

class Symbol:
  def __init__(self, tag, frequency):
    self.tag = tag
    self.frequency = int(frequency)

  def __lt__(self, other):
    return self.frequency < other.frequency

class Huffman:
  def __init__(self, symbols):
    self.symbols = symbols
    self.encoding = {}
    self.encode()

  def encode(self):
    heap = [(sym.frequency, sym) for sym in self.symbols]
    heapq.heapify(heap)

    while len(heap) > 1:
      freq1, sym1 = heapq.heappop(heap)
      freq2, sym2 = heapq.heappop(heap)
      freq = freq1 + freq2
      heapq.heappush(heap, (freq, (sym1, sym2)))

    self.assign_code(heap.pop()[1])

  def assign_code(self, group, codeword = ''):
    if isinstance(group, Symbol):
      self.encoding[group.tag] = codeword
    else:
      sym1, sym2 = group
      self.assign_code(sym1, codeword + '0')
      self.assign_code(sym2, codeword + '1')