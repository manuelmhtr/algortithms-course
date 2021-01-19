from csv import reader
from graph import Graph
from pathlib import Path

def read_file(rel_path):
  full_path = Path(__file__).parent / rel_path
  return open(full_path, 'r')

def get_reversed_graph(rel_path):
  g = Graph()
  with read_file(rel_path) as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
      from_node, to_node = row[0].strip().split(' ')
      g.add_edge(to_node, from_node)
  return g

def find_sccs(input_path):
  reversed_graph = get_reversed_graph(input_path)
  normal_graph = Graph()
  finishing_times = []

  dfs_loop(reversed_graph.get_nodes(), reversed_graph, normal_graph, finishing_times)
  print_sccs(dfs_loop(finishing_times, normal_graph))

def dfs_loop(nodes, graph, rev_graph = None, finishing = None):
  sccs = []

  while len(nodes):
    node = nodes.pop()
    scc = dfs(graph, node, rev_graph, finishing)

    if len(scc): sccs.append(scc)

  return sccs

def dfs(graph, node, rev_graph = None, finishing = None):
  stack = [node]
  scc = []

  while len(stack):
    next_node = stack[-1]

    if graph.is_finished(next_node):
      stack.pop()
      continue

    done = check_node(stack, graph, next_node, rev_graph)
    if done:
      stack.pop()
      scc.append(next_node)
      graph.finish(next_node)
      graph.delete_node(next_node)
      if not finishing is None: finishing.append(next_node)

  return scc

def check_node(stack, graph, from_node, rev_graph=None):
  graph.visit(from_node)
  visited_all = True

  for to_node in graph.connected_nodes(from_node):
    if rev_graph: rev_graph.add_edge(to_node, from_node)
    if graph.is_visited(to_node): continue
    stack.append(to_node)
    visited_all = False

  return visited_all

def print_sccs(sccs):
  sorted_sccs = sorted(sccs, key=len, reverse=True)
  for scc in sorted_sccs[:5]:
    print(f'SCC ({len(scc)}): {scc[:10]}')

find_sccs('./sample-input.txt')
