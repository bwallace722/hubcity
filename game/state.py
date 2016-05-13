class State(object):

    OVERLAP = 'E'
    FOOD = 'F'
    ORGANISM = 'O'
    EMPTY = 'X'

    def __init__(self, width, height):
        self.organisms = []
        self.width = width
        self.height = height
        self.foods = []

    def game_going(self):
        return bool(state.organisms)

    # TODO: implement transition
    # The transition function runs a single step of the game.
    # Rules:
    # An organism starts with some number of food supplies. On any turn
    # that it ends with 0 food supplies, it loses a cell (chosen randomly).
    # Any turn that an organism has any number of overlapping cells with a
    # food, the organism gains a single food supply (rather than losing one),
    # and the food cell loses a cell (chosen randomly from the overlapping
    # cells).
    # These effects are adative for multiple organism and foods, so an organism
    # overlapping two different foods eats from both of them and a food
    # overlapping two different organisms loses two cells.
    # Organisms may not overlap.
    def transition(self, actions):
        for organism in self.organisms:
            for food in self.foods:
                overlapping_cells = set(organism.cells) & set(food.cells)
                
                if overlapping_cells:
                    organism.foodstore += 2
                    food.delete_cell(overlapping_cells.pop())
            organism.foodstore -= 1
            if organism.foodstore <= 0:
                organism.delete_cells(organism.cells[0])
            if len(organism.cells) == 0:
                self.organisms.remove(organism)


    def __str__(self):

        dish = [[State.Empty for _ in range(self.width)] for _ in range(self.height)]

        organism_cells = set([cell for org in self.organisms for cell in org.cells])
        food_cells = set([cell for food in self.foods for cell in food.cells])

        for y in range(self.height):
            for x in range(self.width):
                if (x, y) in organism_cells:
                    is_food = (x, y) in food_cells
                    is_organism = (x, y) in organism_cells
                    if is_food & is_organism:
                        dish[y][x] = State.OVERLAP
                    elif is_organism:
                        dish[y][x] = State.ORGANISM
                    elif is_food:
                        dish[y][x] = State.FOOD

        return '\n'.join[''.join(row) for row in dish]

        



class Organism(object):
    
    def __init__(self, cells, starting_food_supply):
        self.cells = cells
        self.foodstore = starting_food_supply

    def add_cells(self, cells):
        self.cells += cells

    def delete_cell(self, cell):
        self.cells.remove(cell)

class Food(object):

    def __init__(self, cells):
        self.cells = cells

    def add_cells(self, cells):
        self.cells += cells

    def delete_cell(self, cell):
        self.cells.remove(cell)

class Action(object):
    pass
