class State(object):

    def __init__(self, width, height):
        self.organisms = []
        self.width = width
        self.height = height
        self.foods = []


    def transition(self, actions):
        for org in self.organisms:
            for foo in self.foods:
                eat_food = list(set(org.cells) & set(foo.cells))
                
                if len(eat_food)>0:
                    org.foodstore += 1
                    foo.delete_cells(eat_food[0])
            org.foodstore -= 1 
            if org.foodstore < 90:
                org.delete_cells(org.cells[0])
            if len(org.cells) == 0:
                self.organisms.remove(org)




       

    def __str__(self): 
        pass


class Organism(object):
    
    def __init__(self, cells, foodstoreinit):
        self.cells = cells
        self.foodstore = foodstoreinit

    def add_cells(self, cells):
        self.cells += cells

    def delete_cells(self, cells):
        self.cells.remove(cells)

class Food(object):

    def __init__(self, cells):
        self.cells = cells

    def add_cells(self, cells):
        self.cells += cells

    def delete_cells(self, cells):
        self.cells.remove(cells)

class Action(object):
    pass



