from csv import reader
from graph import Graph
from pathlib import Path
from scc import SCC

def read_file(rel_path):
  full_path = Path(__file__).parent / rel_path
  return open(full_path, 'r')

def get_graph(rel_path):
  g = Graph()
  with read_file(rel_path) as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
      from_node, to_node = row[0].strip().split(' ')
      g.add_edge(from_node, to_node)
  return g

def find_sccs(input_path):
  graph = get_graph(input_path)
  return SCC(graph).strongly_connected_components()

def print_sccs(sccs):
  sorted_sccs = sorted(sccs, key=len, reverse=True)
  for scc in sorted_sccs[:5]:
    print(f'SCC ({len(scc)}): {scc[:10]}')

print_sccs(find_sccs('./sample-input.txt'))
