# Map symbols
WALL = '%'
AGENT = 'A'
AGENT1 = '1'
AGENT2 = '2'
BOX = 'B'
GOAL = 'D'
BOX_ON_GOAL = 'C'
EMPTY = ' '

# Actions
NORTH = 'North'
SOUTH = 'South'
EAST = 'East'
WEST = 'West'

MOVE_DELTAS = {
    NORTH: (0, -1),
    SOUTH: (0, 1),
    EAST: (1, 0),
    WEST: (-1, 0),
}

# GUI
CELL_SIZE = 40
FPS = 60

# Colors (RGB)
COLOR_FLOOR = (255, 255, 255)
COLOR_WALL = (128, 128, 128)
COLOR_BOX = (255, 165, 0)
COLOR_BOX_GOAL = (139, 69, 19)
COLOR_GOAL = (255, 0, 0)
COLOR_AGENT = (0, 0, 255)
COLOR_TEXT = (0, 0, 0)