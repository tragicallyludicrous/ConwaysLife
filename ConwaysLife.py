import random



def dead_state(width, height):
	dead_board_state = [[0 for w in range(width)] for h in range(height)]
	return dead_board_state


# random_state function takes in 2 arguments - width and height - and returns a state in which every cell is either ALIVE (1) or DEAD (0)
def random_state(width, height):
	random_board_state = [[random.randint(0,1) for w in range(width)] for h in range(height)]
	return random_board_state


def next_board_state(initial_state):
#	Any live cell with 0 or 1 live neighbors becomes dead, because of underpopulation
	for y in initial_state:
		for x in y:
			if initial_state[x] == 1:
				if 0 <=	neighbor_sum <= 1:
					next_state[x] = 0
#	Any live cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right
				elif 2 <= neighbor_sum <= 3:
					next_state[x] = 1
#	Any live cell with more than 3 live neighbors becomes dead, because of overpopulation
				elif 3 < neighbor_sum:
					next_state[x] = 0
#	Any dead cell with exactly 3 live neighbors becomes alive, by reproduction
			elif initial_state[x] == 0:
				if 3 == neighbor_sum:
					next_state[x] = 1
	return initial_state

def neighbor_sum(initial_state):
	for y in initial_state:
		for x in y:
			return sum([x - 1] + [x + 1] + [x - 1][y - 1] + [x][y - 1] + [x + 1][y - 1] + [x - 1][y + 1] + [x][y + 1] + [x + 1][y + 1])


def render(initial_state):
	print("\u2588"+("\u2588" * stretch * width)+"\u2588")
	for row in initial_state:
		print("\u2588", end = "")
		for element in row:
			if element == 1:
				print(alive_cell, end = "")
			elif element == 0:
				print(dead_cell, end = "")
			else:
				print("ugh")
		print("\u2588", end = "")
		print()
	print("\u2588"+("\u2588" * stretch * width)+"\u2588")





width = 3 # int(input("Width?"))
height = 3 # int(input("Height?"))
stretch = 3
alive_cell = "\u25AF" * stretch
dead_cell = "\u2800" * stretch
random_board_state = random_state(width, height)
dead_board_state = dead_state(width, height)
initial_state = random_board_state
next_state = 0

# x = int(input("x coord?")) - 1
# y = int(input("y coord?")) - 1







#render(board_state)
render(initial_state)
print(neighbor_sum(initial_state))
next_board_state(initial_state)
render(initial_state)