import math
from pathlib import Path

def get_input(rel_path):
  full_path = Path(__file__).parent / rel_path
  file = open(full_path, 'r')
  strings = file.read().strip().split('\n')
  return list(map(int, strings))

def get_hash_table(numbers):
  hash_table = {}
  for number in numbers:
    hash_table[number] = True
  return hash_table

def pair_exists(numbers, hash_table, t):
  for number in numbers:
    target = number + t
    if target != number and hash_table.get(target): return True
  return False

def find_matches(number, hash_table, missing):
  found = set()
  for t in missing:
    target = number + t
    if hash_table.get(target):
      found.add(t)
  return found

def two_sum(numbers, min_t, max_t):
  hash_table = get_hash_table(numbers)
  missing = set(range(min_t, max_t + 1))
  total = len(missing)

  for number in numbers:
    missing = missing - find_matches(number, hash_table, missing)
  return total - len(missing)

numbers = get_input('./input.txt')
print(two_sum(numbers, -10000, 10000))
