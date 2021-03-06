import sys
from pathlib import Path
from knapsack import Item, IterativeKnapsack, RecursiveKnapsack

sys.setrecursionlimit(10000)

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

def knapsack(input_path, KnapsackSolution):
  items, max_weight = get_items(input_path)
  return KnapsackSolution(items, max_weight).max_value()

print(knapsack('./input-min.txt', IterativeKnapsack)) # 202
print(knapsack('./input.txt', IterativeKnapsack))     # 2493893
print(knapsack('./input-big.txt', RecursiveKnapsack)) # 4243395
