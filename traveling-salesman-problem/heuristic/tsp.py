class TSPHeuristicSolution():
  def __init__(self, graph):
    self.graph = graph
    self.first_tag = None
    self.solution = {}

  def shortest_tour(self):
    current_node = self.graph.visit_node_at_index(0)
    self.first_tag = current_node.tag

    while len(self.graph.non_visited) > 0:
      print(len(self.graph.non_visited))
      index, distance = self.nearest_node_index(current_node)
      nearest_node = self.graph.visit_node_at_index(index)
      self.add_to_solution(current_node.tag, nearest_node.tag, distance)
      current_node = nearest_node

    distance_to_first = self.graph.distance(current_node.tag, self.first_tag)
    self.add_to_solution(current_node.tag, self.first_tag, distance_to_first)
    return self.__total_distance()

  def add_to_solution(self, from_tag, to_tag, distance):
    self.solution[from_tag] = (to_tag, distance)

  def nearest_node_index(self, from_node):
    min_distance = float('inf')
    min_squared = float('inf')
    min_index = None
    for index in range(0, len(self.graph.non_visited)):
      to_node = self.graph.non_visited[index]
      if not self.__in_range(min_distance, from_node, to_node): continue
      squared = self.graph.squared_distance(from_node.tag, to_node.tag)
      if squared < min_squared:
        min_distance = self.graph.distance(from_node.tag, to_node.tag, squared)
        min_squared = squared
        min_index = index
    return min_index, min_distance

  def __in_range(self, distance, node1, node2):
    abs_x = abs(node1.x - node2.x)
    if abs_x > distance: return False
    abs_y = abs(node1.y - node2.y)
    return abs_y <= distance

  def __total_distance(self):
    distance = 0

    for value in self.solution.values():
      distance += value[1]

    return distance
