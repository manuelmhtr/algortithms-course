import math
from pathlib import Path

def get_input(rel_path):
  full_path = Path(__file__).parent / rel_path
  file = open(full_path, 'r')
  strings = file.read().strip().split('\n')
  return list(map(int, strings))

def two_sum(numbers, min_t, max_t):
  diff = 2 * max(abs(max_t), abs(min_t))
  buckets = get_buckets(numbers, diff)
  matches = {}

  for bucket in buckets.values():
    if len(bucket) <= 1: continue
    find_matches(list(bucket), matches, min_t, max_t)
  return len(matches)

def get_buckets(numbers, diff):
  buckets = {}
  half = round(diff / 2)
  for number in numbers:
    hash_1 = math.floor(abs(number) / diff)
    hash_2 = math.floor((abs(number) + half) / diff)
    buckets[hash_1] = buckets.get(hash_1) or set()
    buckets[hash_2] = buckets.get(hash_2) or set()
    buckets[hash_1].add(number)
    buckets[hash_2].add(number)
  return buckets

def find_matches(numbers, matches, min_t, max_t):
  for i in range(0, len(numbers)):
    for j in range(i + 1, len(numbers)):
      s = numbers[i] + numbers[j]
      if s >= min_t and s <= max_t:
        matches[s] = True

numbers = get_input('./input.txt')
print(two_sum(numbers, -10000, 10000))
