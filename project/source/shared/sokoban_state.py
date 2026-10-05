class SokobanState:
    def __init__(self, agent1, agent2, boxes, goals, walls, width, height):
        self.agent1 = agent1
        self.agent2 = agent2
        self.boxes = set(boxes)
        self.goals = set(goals)
        self.walls = set(walls)
        self.width = width
        self.height = height

    def get_agent(self, agent_id):
        if agent_id == 1:
            return self.agent1
        if agent_id == 2:
            return self.agent2
        return None

    def set_agent(self, agent_id, position):
        if agent_id == 1:
            self.agent1 = position
        elif agent_id == 2:
            self.agent2 = position

    def is_inside(self, position):
        x, y = position
        return 0 <= x < self.width and 0 <= y < self.height

    def is_wall(self, position):
        return position in self.walls

    def is_box(self, position):
        return position in self.boxes

    def is_solved(self):
        return self.boxes == self.goals

    def key(self):
        return (self.agent1, tuple(sorted(self.boxes)))

    def copy(self):
        return SokobanState(self.agent1, self.agent2, self.boxes, self.goals, self.walls, self.width, self.height)