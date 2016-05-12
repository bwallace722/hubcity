import state

# get_default_state returns an instance of game.State that's 100 x 100
# and contains a single organism with 9 cells on the square with opposite
# corners at 0, 0 and 2, 2.
def get_default_state():
	sta = state.State(100, 100)
	org = state.Organism([])
	for x in range(3):
		for y in range(3):
			org.add_cells([(x, y)])
	return org

org = get_default_state()

print org.cells



    