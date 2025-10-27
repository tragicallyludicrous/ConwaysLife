import random, time



def dead_state(width, height):
	dead_board_state = [[0 for w in range(width)] for h in range(height)]
	return dead_board_state


# random_state function takes in 2 arguments - width and height - and returns a state in which every cell is either ALIVE (1) or DEAD (0)
def random_state(width, height):
	random_board_state = [[random.randint(0,1) for w in range(width)] for h in range(height)]
	return random_board_state


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


def render(initial_state):
	print(border_top_bottom + (border_top_bottom * stretch * width) + border_top_bottom)
	for row in initial_state:
		print(border_wall, end = "")
		for element in row:
			if element == 1:
				print(alive_cell, end = "")
			elif element == 0:
				print(dead_cell, end = "")
			else:
				print("ugh")
		print(border_wall, end = "")
		print()
	print(border_top_bottom + (border_top_bottom * stretch * width) + border_top_bottom)


width = 50 # int(input("Width?"))
height = 40 # int(input("Height?"))
stretch = 3
alive_cell = "\u2588" * stretch
dead_cell = "\u2800" * stretch
border_top_bottom = "-"
border_wall = "|"
random_board_state = random_state(width, height)
dead_board_state = dead_state(width, height)
initial_state = random_board_state
state2 = next_board_state(initial_state)
state3 = next_board_state(state2)
state = [
    [0,0,0,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,0,0,0],
]
# Middle cell at (1,1) should see 4 neighbors.
# Top-middle at (0,1) has below at (1,1) and diagonals, etc.

# x = int(input("x coord?")) - 1
# y = int(input("y coord?")) - 1

# render(initial_state)
# render(next_board_state(initial_state))
# render(next_board_state(next_board_state(initial_state)))


state = initial_state
while True:
	render(state)
	new_state = next_board_state(state)
	state = new_state
	time.sleep(.25)