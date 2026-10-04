from ....shared.movement import Movement
from ....shared.position import getNextPosition


class CompetitiveMovement(Movement):
    def __init__(self, rules):
        super().__init__(rules)

    def moveTwoAgents(self, state, action1, action2):
        canMove1, canMove2 = self.rules.resolveActions(state, action1, action2)

        newState = state.copy()

        agent1 = newState.getAgent(1)
        agent2 = newState.getAgent(2)

        nextPosition1 = agent1.position
        nextPosition2 = agent2.position

        box1 = None
        box2 = None

        boxNextPosition1 = None
        boxNextPosition2 = None

        # Tính trước nước đi của Agent 1
        if canMove1:
            if action1.name != "STAY":
                nextPosition1 = getNextPosition(agent1.position, action1)

                box1 = newState.boxPosition(nextPosition1)

                if box1 is not None:
                    boxNextPosition1 = getNextPosition(box1.position, action1)

        # Tính trước nước đi của Agent 2
        if canMove2:
            if action2.name != "STAY":
                nextPosition2 = getNextPosition(agent2.position, action2)

                box2 = newState.boxPosition(nextPosition2)

                if box2 is not None:
                    boxNextPosition2 = getNextPosition(box2.position, action2)

        # Di chuyển box của Agent 1
        if canMove1:
            if box1 is not None:
                box1.position = boxNextPosition1

                if newState.isGoal(boxNextPosition1):
                    box1.owner = 1
                else:
                    box1.owner = None

        # Di chuyển box của Agent 2
        if canMove2:
            if box2 is not None:
                box2.position = boxNextPosition2

                if newState.isGoal(boxNextPosition2):
                    box2.owner = 2
                else:
                    box2.owner = None

        # Di chuyển Agent 1
        if canMove1:
            agent1.position = nextPosition1

        # Di chuyển Agent 2
        if canMove2:
            agent2.position = nextPosition2

        newState.stepCount = newState.stepCount + 1

        return newState