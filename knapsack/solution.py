from pathlib import Path
from knapsack import Item, Cache

def get_input(input_path):
  full_path = Path(__file__).parent / input_path
  file = open(full_path, 'r')
  return file.read().strip().split('\n')

def get_items(input_path):
  strings = get_input(input_path)
  max_weight = strings[0].split(' ')[0]
  tag = 0
  items = []
  for row in strings[1:]:
    tag += 1
    value, weight = row.split(' ')
    items.append(Item(tag, value, weight))
  items.sort()
  return items, int(max_weight)

def knapsack(input_path):
  items, max_weight = get_items(input_path)
  cache = Cache()

  for item in items:
    for w in range(0, max_weight + 1):
      not_include = cache.get_value(item.tag - 1, w)
      if w < item.weight:
        cache.set_value(item.tag, w, not_include)
      else:
        max_value = max(
          not_include,
          item.value + cache.get_value(item.tag - 1, w - item.weight)
        )
        cache.set_value(item.tag, w, max_value)

  return cache.get_value(items[-1].tag, max_weight)

print(knapsack('./input-min.txt')) # 202
print(knapsack('./input.txt'))     # 2493893
print(knapsack('./input-big.txt')) # in progress...
