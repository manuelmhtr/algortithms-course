from graph import Graph

class SCC:
  def __init__(self, graph):
    self.graph = graph
    self.reversed_graph = None
    self.finishing_times = None
    self.sccs = None

  def strongly_connected_components(self):
    if (self.sccs): return self.sccs

    self.reversed_graph = Graph()
    self.finishing_times = []

    self.dfs_loop(self.graph, self.graph.get_nodes(), True)
    self.sccs = self.dfs_loop(self.reversed_graph, self.finishing_times)
    return self.sccs

  def dfs_loop(self, graph, nodes, first_iteration = False):
    sccs = []

    while len(nodes):
      node = nodes.pop()
      scc = self.dfs(graph, node, first_iteration)

      if len(scc): sccs.append(scc)

    return sccs

  def dfs(self, graph, node, first_iteration):
    stack = [node]
    scc = []

    while len(stack):
      next_node = stack[-1]

      if graph.is_finished(next_node):
        stack.pop()
        continue

      done = self.check_node(graph, stack, next_node, first_iteration)
      if done:
        stack.pop()
        scc.append(next_node)
        graph.finish(next_node)
        graph.delete_node(next_node)
        if first_iteration: self.finishing_times.append(next_node)

    return scc

  def check_node(self, graph, stack, from_node, first_iteration):
    graph.visit(from_node)
    visited_all = True
    to_nodes = graph.connected_nodes(from_node)

    while len(to_nodes):
      to_node = to_nodes.pop()
      if first_iteration: self.reversed_graph.add_edge(to_node, from_node)
      if graph.is_visited(to_node): continue
      stack.append(to_node)
      visited_all = False

    return visited_all
