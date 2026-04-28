import random, time, sys

ALIVE, DEAD = 1, 0

# ---------------------------------------------------------
# GRID GENERATION
# ---------------------------------------------------------

#  takes in width and height and returns a grid in which every cell is either ALIVE (1) or DEAD (0)
def random_grid(width, height, alive_prob = 0.5):
    """Generate a random game grid of 0s and 1s.
    alive_prob is the chance of a cell being alive (default 0.5)."""
    grid = []
    for _ in range(height):
        grid.append([])
        for _ in range(width):
            grid[-1].append(ALIVE if random.random() < alive_prob else DEAD)
    return grid

def next_board_grid(grid):
    """Compute next generation from a 2D 0/1 grid using Conway's rules."""
    h = len(grid)
    if h == 0:
        return
    w = len(grid[0])
    # Initialize next grid to all dead so we can just determine which cells are alive
    next_grid = [[DEAD for _ in range(w)] for _ in range(h)]

    for y in range(h):
        for x in range(w):
            n = vn_count_neighbors(grid, y, x)
            cell = grid[y][x]
            if cell == ALIVE:
                # This is one of Conway's rules - if a cell has 2 or 3 neighbors it survives
                if n == 2 or n == 3:
                    next_grid[y][x] = ALIVE
            # Another rule: if any empty cell has 3 living neighbors it comes to life
            else:
                if n == 3:
                    next_grid[y][x] = ALIVE
    return next_grid

# ---------------------------------------------------------
# HELPERS
# ---------------------------------------------------------

# Counts neighbors ignoring off-border neighbors
def count_neighbors(grid, y, x):
    h = len(grid)       # number of rows
    w = len(grid[0])    # number of columns
    total = 0
    for dy in (-1, 0, 1):
        for dx in (-1, 0 ,1):
            if dy == 0 and dx == 0:
                continue    #skip the cell itself
            # ny, nx (neighbors y and x)
            ny, nx = y + dy, x + dx
            # if the neighbor isn't off the grid, ignore it
            if 0 <= ny < h and 0 <= nx < w:
                total += grid[ny][nx]
    return total

# Count neighbors with the Von Neumann diamond method (no wrap)
def vn_count_neighbors(grid, y, x):
    h = len(grid)       # number of rows
    w = len(grid[0])    # number of columns
    total = 0
    for dy in range(-2,3):
        for dx in range(-2,3):
            if dy == 0 and dx == 0:
                continue    #skip the cell itself
            # ny, nx (neighbors y and x)
            ny, nx = y + dy, x + dx

            # if the neighbor is off the grid, ignore it
            if abs(dx) + abs(dy) <= 2:
                if 0 <= ny < h and 0 <= nx < w:
                    total += grid[ny][nx]

    return total


# Count neighbors with the Von Neumann diamond method (no wrap)
def vn_count_neighbors_wrap(grid, y, x):
    h = len(grid)       # number of rows
    w = len(grid[0])    # number of columns
    total = 0
    for dy in range(-2,3):
        for dx in range(-2,3):
            if dy == 0 and dx == 0:
                continue    #skip the cell itself
            # ny, nx (neighbors y and x)
            ny = (y + dy) % h
            nx = (x + dx) % w
            # if the neighbor is off the grid, ignore it
            if abs(dx) + abs(dy) <= 2:
                if 0 <= ny < h and 0 <= nx < w:
                    total += grid[ny][nx]
    return total


# Counts neighbors with wrapping
def count_neighbors_wrap(grid, y, x):
    h = len(grid)       # number of rows
    w = len(grid[0])    # number of columns
    total = 0
    for dy in (-1, 0, 1):
        for dx in (-1, 0 ,1):
            if dy == 0 and dx == 0:
                continue    #skip the cell itself
            # neighbors y and x, remaindered from the total height/width allows for wrapping
            ny = (y + dy) % h
            nx = (x + dx) % w
            total += grid[ny][nx]
    return total

# ---------------------------------------------------------
# RENDERING
# ---------------------------------------------------------

def render(grid):
    """Render the grid with border and stretch settings."""
    h = len(grid)
    w = len(grid[0]) if h > 0  else 0

    # Top border, stretch to compensate for terminal blocks being 3x taller than wide.
    print(border_top_bottom * (stretch * w + 2))
    
    # Each row
    for row in grid:
        print(border_wall, end="")
        for cell in row:
            print(alive_cell if cell else dead_cell, end="")
        print(border_wall)
    
    # Bottom border
    print(border_top_bottom * (stretch * w + 2))

# ---------------------------------------------------------
# LOADING FILES
# ---------------------------------------------------------

# Parses txt files that are grids of 0s, 1s
def load_board_grid(filename):
    grid = []
    with open(filename, 'r') as file:
        for line in file:
            if set(line.strip()) <= {ALIVE, DEAD}:
                print("File must contain only 1s and 0s.")
                return
            grid.append(list(map(int, line.strip())))

    return grid


width = 50 # int(input("Width?"))
height = 40 # int(input("Height?"))
alive_prob = .5
seed = None
stretch = 3
alive_cell = "\u2588" * stretch
dead_cell = "\u2800" * stretch
border_top_bottom = "-"
border_wall = "|"
random_board_grid = random_grid(width, height)
test_grid = [
    [0,0,0,0,0],
    [0,0,1,1,0],
    [0,0,1,1,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
]
initial_grid = random_grid(width, height, alive_prob)


if __name__ == "__main__":

    if len(sys.argv) > 1:
        grid = load_board_grid(sys.argv[1])
    else:
        grid = initial_grid
    prev = None
    try:
        while True:
            # Arbitrary spacer to push the previous generation out of the window
            print("\n" * 20)
            render(grid)
            new_grid = next_board_grid(grid)

            # all dead
            if sum(sum(row) for row in new_grid) == 0:
                print("All cells dead — stopping.")
                break

            # static
            if new_grid == grid:
                print("Static pattern — stopping.")
                break

            # period-2 oscillator
            if prev is not None and new_grid == prev:
                print("Period-2 oscillator — stopping.")
                break

            prev, grid = grid, new_grid
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("Bye!")