import random, time, os


# random_state function takes in width and height and returns a state in which every cell is either ALIVE (1) or DEAD (0)
def random_state(width, height, alive_prob = 0.5, seed = None):
    """Generate a random game state of 0s and 1s.
    alive_prob is the chance of a cell being alive (default 0.5)."""
    if seed is not None:
        random.seed(seed)
    return [[1 if random.random() < alive_prob else 0 for _ in range(width)] for _ in range(height)]


ALIVE, DEAD = 1, 0

def next_board_state(grid):
    """Compute next generation from a 2D 0/1 grid using Conway's rules."""
    h = len(grid)
    if h == 0:
        return[]
    w = len(grid[0])
    next_grid = [[DEAD for _ in range(w)] for _ in range(h)]

    for y in range(h):
        for x in range(w):
            n = count_neighbors(grid, y, x)
            cell = grid[y][x]
            if cell == ALIVE:
                if n == 2 or n == 3:
                    next_grid[y][x] = ALIVE
            else:
                if n == 3:
                    next_grid[y][x] = ALIVE 
    return next_grid

def count_neighbors(grid, y, x):
    h = len(grid)       # number of rows
    w = len(grid[0])    # number of columns
    total = 0
    for dy in (-1, 0, 1):
        for dx in (-1, 0 ,1):
            if dy == 0 and dx == 0:
                continue    #skip the cell itself
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w:
                total += grid[ny][nx]
    return total

def count_neighbors_wrap(grid, y, x):
    h = len(grid)       # number of rows
    w = len(grid[0])    # number of columns
    total = 0
    for dy in (-1, 0, 1):
        for dx in (-1, 0 ,1):
            if dy == 0 and dx == 0:
                continue    #skip the cell itself
            ny = (y + dy) % h
            nx = (x + dx) % w
            total += grid[ny][nx]
    return total


def render(state):
    """Render the grid with border and stretch settings."""
    h = len(state)
    w = len(state[0]) if h > 0  else 0

    # Top border
    print(border_top_bottom * (stretch * w + 2))
    
    # Each row
    for row in state:
        print(border_wall, end="")
        for cell in row:
            print(alive_cell if cell else dead_cell, end="")
        print(border_wall)
    
    # Bottom border
    print(border_top_bottom * (stretch * w + 2))

def load_board_state(filename):
    two_d_list = []
    with open(filename, 'r') as file:
        for line in file:
            two_d_list.append(list(map(int, line.strip())))

    return two_d_list


width = 50 # int(input("Width?"))
height = 40 # int(input("Height?"))
alive_prob = 0.75
seed = None
stretch = 3
alive_cell = "\u2588" * stretch
dead_cell = "\u2800" * stretch
border_top_bottom = "-"
border_wall = "|"
random_board_state = random_state(width, height)
test_grid = [
    [0,0,0,0,0],
    [0,0,1,1,0],
    [0,0,1,1,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
]
initial_state = random_state(width, height, alive_prob, seed)

# Middle cell at (1,1) should see 4 neighbors.
# Top-middle at (0,1) has below at (1,1) and diagonals, etc.


if __name__ == "__main__":

    # ##IMPORT MODE###
    # import_file = input("Import filename?")
    # import_file_contents = open(import_file, 'r').read()
    # width = len(import_file_contents.split('\n')[0])
    # height = len(import_file_contents.splitlines())
    # initial_state = load_board_state(import_file)

    ##  RANDOM MODE ###
        # parse args / set params
        # build initial_state
        # run loop
    prev = None
    state = initial_state
    try:
        while True:
            print("\n" * 20)
            render(state)
            new_state = next_board_state(state)

            # all dead
            if sum(sum(row) for row in new_state) == 0:
                print("All cells dead — stopping.")
                break

            # static
            if new_state == state:
                print("Static pattern — stopping.")
                break

            # period-2 oscillator
            if prev is not None and new_state == prev:
                print("Period-2 oscillator — stopping.")
                break

            prev, state = state, new_state
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("Bye!")