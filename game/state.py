class State(object):

    def __init__(self, width, height):
        self.organisms = []
        self.width = width
        self.height = height


    def transition(self, actions):
        pass

        

class Organism(object):
    
    def __init__(self,cells):
        self.cells = cells

    def add_cells(self, cells):
        self.cells += cells

    

class Action(object):
    pass



