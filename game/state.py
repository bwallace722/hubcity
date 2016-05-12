class State(object):

    def __init__(self, width, height):
        self.organisms = []
        self.width = width
        self.height = height
        self.food = []


    def transition(self, actions):
        pass

    def __str__(self): #Print the game board ---/n---/n
        pass

class Organism(object):
    
    def __init__(self, cells, foodstoreinit):
        self.cells = cells
        self.foodstore = foodstoreinit

    def add_cells(self, cells):
        self.cells += cells

    

class Food(object):
    def __init__(self, cells):
        self.cells = cells

    def add_cells(self, cells):
        self.cells += cells

    def delete_cells(self, cells):
        self.cells -=

class Action(object):
    pass



