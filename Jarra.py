from Problem import Problem
from Node import Node
class Jarra(Problem):
  def __init__(self, initial, goal):
      super().__init__(initial, goal) 
  
  def expand(self, node):
    children = [] 
    v_la = self.la(node)
    if v_la is not None: 
      children.append(v_la)
    
    v_lb = self.lb(node)
    if v_lb is not None: 
      children.append(v_lb)

    v_va = self.va(node)
    if v_va is not None: 
      children.append(v_va)

    v_vb = self.vb(node)
    if v_vb is not None: 
      children.append(v_vb)
    
    v_ba = self.ba(node)
    if v_ba is not None: 
      children.append(v_ba)    

    v_ab = self.ab(node)
    if v_ab is not None: 
      children.append(v_ab)
    
    return children 
  
  def la(self, node):
    state = node.state 
    if state[0] != 4:
      newState = (4, state[1]) 
      return Node(newState, node, 'llenar jarra-4')
    return None 
  
  def lb(self, node):
    state = node.state 
    if state[1] != 3: 
      newState = (state[0], 3) 
      return Node(newState, node, 'llenar jarra-3')
    return None

  def va(self, node): 
    state = node.state 
    if state[0] != 0: 
      newState = (0, state[1]) 
      return Node(newState, node, 'vaciar jarra-4')
    return None 
    
  def vb(self, node): 
    state = node.state 
    if state[1] != 0: 
      newState = (state[0], 0) 
      return Node(newState, node, 'vaciar jarra-3')
    return None 

  def ab(self, node): 
    state = node.state 
    if state[0] > 0 and state[1] <= 3: 
      add = 3 - state[1]
      newState = (0, state[1] + state[0]) if add >= state[0] else  (state[0]-add, state[1]+add)
      return Node(newState, node, 'vaciar jarra-4 en jarra-3')
    return None 
    
  def ba(self, node): 
    state = node.state 
    if state[1] > 0 and state[0] <= 4: 
      add = 4 - state[0]
      newState = (state[0] + state[1], 0) if add >= state[1] else (state[0] + add, state[1] - add ) 
      return Node(newState, node, 'vaciar jarra-3 en jarra-4')
    return None 
    
