from Node import Node
class Problem(object):
  
  def __init__(self, initial, goal):
    
    if not isinstance(initial,Node):
      raise TypeError('node type is required for initial')
    if not isinstance(goal,Node):
      raise TypeError('node type is required for initial')

    self.initial = initial
    self.goal = goal
    
  def expand(self, node):
    
    raise NotImplementedError
