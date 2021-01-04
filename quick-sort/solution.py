import math
from pathlib import Path

def get_input(rel_path):
  full_path = Path(__file__).parent / rel_path
  file = open(full_path, 'r')
  strings = file.read().strip().split('\n')
  return list(map(int, strings))

def transpose(arr, index1, index2):
  prev = arr[index1]
  arr[index1] = arr[index2]
  arr[index2] = prev

def get_pivot_first(numbers, l, r):
  return l

def get_pivot_last(numbers, l, r):
  return r - 1

def get_pivot_median(numbers, l, r):
  mid = math.floor((l + r - 1) / 2.0)
  val1 = numbers[l]
  val2 = numbers[r - 1]
  val3 = numbers[mid]
  median = sorted([val1, val2, val3])[1]
  if median == val1:
    return l
  elif median == val2:
    return r - 1
  return mid

def quick_sort(numbers, l = None, r = None):
  l = 0 if l is None else l
  r = len(numbers) if r is None else r
  length = r - l
  if length <= 1: return 0

  pivot_index = get_pivot_first(numbers, l, r)
  pivot_value = numbers[pivot_index]
  transpose(numbers, pivot_index, l)

  i = l + 1

  for j in range(i, r):
    if numbers[j] < pivot_value:
      transpose(numbers, i, j)
      i += 1

  transpose(numbers, l, i - 1)

  comp1 = quick_sort(numbers, l, i - 1)
  comp2 = quick_sort(numbers, i, r)

  return comp1 + comp2 + (length - 1)

numbers = get_input('./sample-input.txt')
print(quick_sort(numbers))
