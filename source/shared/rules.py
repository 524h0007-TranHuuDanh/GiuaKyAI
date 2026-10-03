from .position import getNextPosition


class Rules:
    def __init__(self, walls):
        self.walls = walls

    def isWall(self, position):
        if position in self.walls:
            return True

        return False

    def canMoveAgent(self, state, agentId, action):
        agent = state.getAgent(agentId)

        if agent is None:
            return False

        if action.name == "STAY":
            return True

        currentPosition = agent.position
        nextPosition = getNextPosition(currentPosition, action)

        if self.isWall(nextPosition):
            return False

        box = state.boxPosition(nextPosition)

        if box is None:
            return True

        boxPosition = box.position
        boxNextPosition = getNextPosition(boxPosition, action)

        if self.isWall(boxNextPosition):
            return False

        otherBox = state.boxPosition(boxNextPosition)

        if otherBox is not None:
            return False

        return True