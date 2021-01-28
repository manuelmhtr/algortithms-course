from heaps import MedianHeap
from pathlib import Path

def get_input(rel_path):
  full_path = Path(__file__).parent / rel_path
  file = open(full_path, 'r')
  strings = file.read().strip().split('\n')
  return list(map(int, strings))

def sum_of_medians(input_path):
  numbers = get_input(input_path)
  heap = MedianHeap()
  medians_sum = 0

  for num in numbers:
    heap.push(num)
    medians_sum += heap.median()

  return medians_sum

total = sum_of_medians('./input.txt')
print(total % 10000)
