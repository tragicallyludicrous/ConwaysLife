import random



def dead_state(width, height):
	dead_board_state = [[0 for w in range(width)] for h in range(height)]
	return dead_board_state


# random_state function takes in 2 arguments - width and height - and returns a state in which every cell is either ALIVE (1) or DEAD (0)
def random_state(width, height):
	random_board_state = [[random.randint(0,1) for w in range(width)] for h in range(height)]
	return random_board_state


# def next_board_state(initial_state):
# #	Any live cell with 0 or 1 live neighbors becomes dead, because of underpopulation
# 	for y in initial_state:
# 		for x in y:
# 			if initial_state[x] == 1:
# 				if 0 <=	count_neighbors(initial_state, x, y) <= 1:
# 					next_state[x] = 0
# 
# 				elif 2 <= count_neighbors(initial_state, x, y) <= 3:
# 					next_state[x] = 1
# #	Any live cell with more than 3 live neighbors becomes dead, because of overpopulation
# 				elif 3 < count_neighbors(initial_state, x, y):
# 					next_state[x] = 0

# 			elif initial_state[x] == 0:
# 				if 3 == count_neighbors(initial_state, x, y):
# 					next_state[x] = 1
# 	return next_state

def next_board_state(grid):
	h = len(grid)
	w = len(grid[0])
	next_grid = [[0 for _ in range(w)] for _ in range(h)]
	for y in range(h):
		for x in range(w):
			n = count_neighbors(grid, y, x)
			cell = grid[y][x]
			if cell == 1:
#	Any live cell with 0 or 1 live neighbors becomes dead, because of underpopulation
				if n == (1 or 0):
					next_grid[y][x] = 0
#	Any live cell with more than 3 live neighbors becomes dead, because of overpopulation
				elif n == (2 or 3):
					next_grid[y][x] = 1
#	Any live cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right
				elif n > 3:
					next_grid[y][x] = 0
#	Any dead cell with exactly 3 live neighbors becomes alive, by reproduction
			elif cell == 0:
				if n == 3:
					next_grid[y][x] = 1
	return next_grid

def count_neighbors(grid, y, x):
	h = len(grid)		# number of rows
	w = len(grid[0])	# number of columns
	total = 0
	for dy in (-1, 0, 1):
		for dx in (-1, 0 ,1):
			if dy == 0 and dx == 0:
				continue	#skip the cell itself
			ny = (y + dy) % h
			nx = (x + dx) % w
			total += grid[ny][nx]
	return total


# def neighbor_sum(initial_state):
# 	for y in initial_state:
# 		for x in y:
# 			return sum([x - 1] + [x + 1] + [x - 1][y - 1] + [x][y - 1] + [x + 1][y - 1] + [x - 1][y + 1] + [x][y + 1] + [x + 1][y + 1])


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





width = 10 # int(input("Width?"))
height = 10 # int(input("Height?"))
stretch = 3
alive_cell = " \u25AF "
dead_cell = " \u2800 "
random_board_state = random_state(width, height)
dead_board_state = dead_state(width, height)
initial_state = random_board_state
state2 = next_board_state(initial_state)
state3 = next_board_state(state2)
grid = [
	[0,0,0],
	[1,0,1],
	[0,1,0]
]
# Middle cell at (1,1) should see 4 neighbors.
# Top-middle at (0,1) has below at (1,1) and diagonals, etc.

# x = int(input("x coord?")) - 1
# y = int(input("y coord?")) - 1







render(random_board_state)
render(state2)
render(state3)