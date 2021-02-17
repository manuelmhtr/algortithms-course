class Job:
  def __init__(self, weight, length):
    self.weight = float(weight)
    self.length = float(length)

  def __lt__(self, other):
    if (self.priority() == other.priority()):
      return self.weight < other.weight
    else:
      return self.priority() < other.priority()

  def priority(self, other):
    return NotImplemented

class JobDiff(Job):
  def priority(self):
    return self.weight - self.length

class JobRatio(Job):
  def priority(self):
    return self.weight / self.length
