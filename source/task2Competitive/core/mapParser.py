from source.shared.constants import(WALL, AGENT1, AGENT2, BOX, GOAL, BOX_ON_GOAL)

class MapParser:
    def __init__(self, file_path):
        self.file_path = file_path

    def parse(self):
        walls = set()
        agents ={}
        boxes = []
        goals = []

        with open(self.file_path, "r") as file:
            lines = [line.rstrip("\n") for line in file]
        for y, line in enumerate(lines):
            for x, cell in enumerate(line):
                position = (x, y)
                if cell == WALL:
                    walls.add(position)
                elif cell == AGENT1:
                    agents[1] = position
                elif cell == AGENT2:
                    agents[2] = position
                elif cell == BOX:
                    boxes.append(position)
                elif cell == GOAL:
                    goals.append(position)
                elif cell == BOX_ON_GOAL:
                    boxes.append(position)
                    goals.append(position)
        return {"walls": walls, "agents": agents, "boxes": boxes,"goals": goals,}