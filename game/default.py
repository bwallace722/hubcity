import state
import time
# get_default_state returns an instance of game.State that's 100 x 100
# and contains a single organism with 9 cells on the square with opposite
# corners at 0, 0 and 2, 2.
def get_default_state():
	org1 = state.Organism([],100)
	
	for x in range(3):
		for y in range(3):
			org1.add_cells([(x, y)])
			
	food1 = state.Food([(1,2)])
	food1.add_cells([(2,1)])

	default_state = state.State(100, 100)
	default_state.organisms = [org1]
	default_state.foods = [food1]
	return default_state
	

def run_game():
	default_state = get_default_state()

	for turns in range(15):
		default_state.transition([])
		if len(default_state.organisms) >0:
			print default_state.organisms[0].cells
			print default_state.foods[0].cells
		else:
			print 'Game Over'

	
run_game()







    