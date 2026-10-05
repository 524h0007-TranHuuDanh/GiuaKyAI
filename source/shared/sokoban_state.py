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

    def is_goal(self, position):
        return position in self.goals

    def box_position(self, position):
        if position in self.boxes:
            return position
        return None

    def is_solved(self):
        return self.boxes == self.goals

    def count_boxes_on_goals(self):
        count = 0
        for box in self.boxes:
            if box in self.goals:
                count += 1
        return count

    def key(self):
        return (self.agent1, tuple(sorted(self.boxes)))

    def copy(self):
        return SokobanState(
            self.agent1,
            self.agent2,
            set(self.boxes),
            set(self.goals),
            set(self.walls),
            self.width,
            self.height
        )