from .position import getNextPosition


class Movement:
    def __init__(self, rules):
        self.rules = rules

    def moveAgent(self, state, agentId, action):
        canMove = self.rules.canMoveAgent(state, agentId, action)

        if canMove == False:
            newState = state.copy()
            return newState

        newState = state.copy()

        agent = newState.getAgent(agentId)

        if action.name == "STAY":
            return newState

        currentPosition = agent.position
        nextPosition = getNextPosition(currentPosition, action)

        box = newState.boxPosition(nextPosition)

        if box is not None:
            boxPosition = box.position
            boxNextPosition = getNextPosition(boxPosition, action)

            box.position = boxNextPosition

            if newState.isGoal(boxNextPosition):
                box.owner = agentId
            else:
                box.owner = None

        agent.position = nextPosition

        newState.stepCount = newState.stepCount + 1

        return newState