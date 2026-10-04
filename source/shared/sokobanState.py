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

    def getAgent(self, agentId):
        if agentId == 1:
            return self.agent1

        if agentId == 2:
            return self.agent2

        return None

    def isWall(self, position):
        if position in self.walls:
            return True

        return False

    def isBox(self, position):
        if position in self.boxes:
            return True

        return False

    def isGoal(self, position):
        if position in self.goals:
            return True

        return False

    def countBoxesOnGoals(self):
        count = 0

        for box in self.boxes:
            if box in self.goals:
                count = count + 1

        return count

    def copy(self):
        newState = SokobanState(
            self.agent1,
            self.agent2,
            frozenset(self.boxes),
            frozenset(self.goals),
            frozenset(self.walls),
            self.width,
            self.height,
            self.row_lengths
        )

        return newState