import math
from pathlib import Path

def get_input(rel_path):
  full_path = Path(__file__).parent / rel_path
  file = open(full_path, 'r')
  strings = file.read().strip().split('\n')
  return list(map(int, strings))

def mix_arrays(arr_1, arr_2):
  sorted = []
  len_1 = len(arr_1)
  len_2 = len(arr_2)
  index_2 = 0
  inversions = 0

  for index_1 in range(len_1):
    value_1 = arr_1[index_1]

    while index_2 < len_2 and value_1 > arr_2[index_2]:
      inversions += len_1 - index_1
      sorted.append(arr_2[index_2])
      index_2 += 1

    sorted.append(value_1)

  sorted.extend(arr_2[index_2:])
  return (inversions, sorted)

def count_inversions(numbers):
  mid = math.floor(len(numbers) / 2)

  if mid == 0: return (0, numbers)

  (count_1, sorted_1) = count_inversions(numbers[:mid])
  count_2, sorted_2 = count_inversions(numbers[mid:])
  count_3, sorted_3 = mix_arrays(sorted_1, sorted_2)

  inversions = count_1 + count_2 + count_3
  return (inversions, sorted_3)

numbers = get_input('./sample-input.txt')
print(count_inversions(numbers)[0])
