import random

# random_state function takes in 2 arguments - width and height - and returns a state in which every cell is either ALIVE (1) or DEAD (0)

def dead_state(width, height):
	dead_board_state = [[0 for w in range(width)] for h in range(height)]
	return dead_board_state

def random_state(width, height):
	random_board_state = [[random.randint(0,1) for w in range(width)] for h in range(height)]
	return random_board_state


width = 10 # int(input("Width?"))
height = 10 # int(input("Height?"))
stretch = 3
alive_cell = "\u2588" * stretch
dead_cell = "\u2800" * stretch
board_state = random_state(width, height)
# x = int(input("x coord?")) - 1
# y = int(input("y coord?")) - 1


def render(board_state):
	print(" "+("#" * stretch * width)+" ")
	for row in board_state:
		print("#", end = "")
		for element in row:
			if element == 1:
				print(alive_cell, end = "")
			elif element == 0:
				print(dead_cell, end = "")
			else:
				print("ugh")
		print("#", end = "")
		print()
	print(" "+("#" * stretch * width)+" ")
# print(board_state)



render(board_state)

