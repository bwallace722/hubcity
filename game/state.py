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




       
#Prints Game Board
    def __str__(self):

        dish = []
        orgcells = []
        foodcells = []
        s = ""
        for org in self.organisms:
            for cells in org.cells:
                orgcells.append(cells)
        for food in self.foods:
            for cells in food.cells:
                foodcells.append(cells)
        for y in range(self.height):
            dish.append(["X"]*self.height)
        for cells in orgcells:
            if foodcells.count(cells)>0:
                dish[cells[0]][cells[1]] = 'E'
            else:
                dish[cells[0]][cells[1]] = 'O'
        for cells in foodcells:
            if orgcells.count(cells)>0:
                dish[cells[0]][cells[1]] = 'E'
            else:
                dish[cells[0]][cells[1]] = 'F'
        for row in dish:
            s = '{}\n{}'.format(s,"".join(row))
        return s

        



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



