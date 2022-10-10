class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state    #ESTADO
        self.parent = parent  
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        rep = 'Node(' + str(self.state)+ ', ' + str(self.action) +')'
        return rep


    def __eq__(self, node):
        return self.state == node.state
  