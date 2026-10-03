from enum import Enum

class Action(Enum):
    NORTH = (0,-1)
    SOUTH = (0,1)
    EAST = (1,0)
    WEST = (-1, 0)
    STAY = (0,0)