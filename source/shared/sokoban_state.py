class SokobanState:
    def __init__(self, agent1, agent2, boxes, goals, walls, width, height, row_lengths):
        self.agent1 = agent1
        self.agent2 = agent2

        self.boxes = boxes
        self.goals = goals
        self.walls = walls

        self.width = width
        self.height = height
        self.row_lengths = row_lengths

    def get_agent(self, agent_id):
        if agent_id == 1:
            return self.agent1

        if agent_id == 2:
            return self.agent2

        return None

    def is_wall(self, position):
        if position in self.walls:
            return True

        return False

    def is_box(self, position):
        if position in self.boxes:
            return True

        return False

    def is_goal(self, position):
        if position in self.goals:
            return True

        return False

    def count_boxes_on_goals(self):
        count = 0

        for box in self.boxes:
            if box in self.goals:
                count = count + 1

        return count

    def copy(self):
        new_state = SokobanState(
            self.agent1,
            self.agent2,
            frozenset(self.boxes),
            frozenset(self.goals),
            frozenset(self.walls),
            self.width,
            self.height,
            self.row_lengths
        )

        return new_state