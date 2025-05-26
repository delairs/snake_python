# Dimensions
WIDTH = 612
HEIGHT = 612
ROWS = 17
SQUARE_SIZE = WIDTH // ROWS
GAP_SIZE = 2

# Colors
SURFACE_CLR = (15, 15, 15)
GRID_CLR = (20, 20, 20)
SNAKE_CLR = (50, 255, 50)
APPLE_CLR = (255, 255, 0)
HEAD_CLR = (0, 150, 0)
VIRTUAL_SNAKE_CLR = (255, 0, 0)
BUTTON_CLR = (70, 70, 70)
BUTTON_HOVER_CLR = (100, 100, 100)
TEXT_CLR = (255, 255, 255)
STATS_CLR = (200, 200, 200)

# Game Settings
FPS = 15
INITIAL_SNAKE_LENGTH = 3
WAIT_SECONDS_AFTER_WIN = 3
MAX_MOVES_WITHOUT_EATING = ROWS * ROWS * ROWS * 2
SNAKE_MAX_LENGTH = ROWS * ROWS - INITIAL_SNAKE_LENGTH

# Grid and pathfinding setup
GRID = [[i, j] for i in range(ROWS) for j in range(ROWS)]

def get_neighbors(position):
    neighbors = [[position[0] + 1, position[1]],
                 [position[0] - 1, position[1]],
                 [position[0], position[1] + 1],
                 [position[0], position[1] - 1]]
    in_grid_neighbors = []
    for pos in neighbors:
        if pos in GRID:
            in_grid_neighbors.append(pos)
    return in_grid_neighbors

def distance(pos1, pos2):
    x1, x2 = pos1[0], pos2[0]
    y1, y2 = pos1[1], pos2[1]
    return abs(x2 - x1) + abs(y2 - y1)

ADJACENCY_DICT = {tuple(pos): get_neighbors(pos) for pos in GRID}