class State(object):

    def __init__(self):
        self.organisms = []
        self.size = {'X': 1000,'Y': 1000}

    def transition(self, actions):
        pass

        

class Organism(object):
    
    def __init__(self,cells):
        self.cells = cells

    def add_cells(self, cells):
        self.cells += cells

    

class Action(object):
    pass



