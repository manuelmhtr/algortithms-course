import copy
from graph import Graph
from pathlib import Path

def read_rows(rel_path):
  full_path = Path(__file__).parent / rel_path
  file = open(full_path, 'r')
  return file.read().strip().split('\n')

def get_graph(rel_path):
  result = {}
  rows = read_rows(rel_path)
  for row in rows:
    values = row.strip().split('\t')
    result[values[0]] = values[1:]
  return result

def find_min_cut(data):
  min_all = float('inf')
  iterations = 10 * len(data)
  for i in range(iterations):
    min_i = Graph(copy.deepcopy(data)).min_cut()
    min_all = min(min_all, min_i)
  return min_all

def dup_dict(data):
  result = {}
  for key in data.keys():
    result[key] = data[key]
  return result

data = get_graph('./sample-input.txt')
print(find_min_cut(data))
