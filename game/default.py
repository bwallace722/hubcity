import state
import time
# get_default_state returns an instance of game.State that's 10 x 10
# and contains a single organism with 9 cells on the square with opposite
# corners at 0, 0 and 2, 2.
def get_default_state():
	org1 = state.Organism({},10)
	
	for x in range(3):
		for y in range(3):
			org1.add_cells([(x, y)])
			
	food1 = state.Food([(1,2)])
	food1.add_cells([(2,2)])
	food1.add_cells([(2,3)])


	default_state = state.State(10, 10)
	default_state.organisms = [org1]
	default_state.foods = [food1]
	return default_state
