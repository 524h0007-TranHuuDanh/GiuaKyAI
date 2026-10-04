from ....shared.rules import Rules
from ....shared.position import getNextPosition


class CompetitiveRules(Rules):
    def __init__(self, walls):
        super().__init__(walls)

    def getAgentNextPosition(self, state, agentId, action):
        agent = state.getAgent(agentId)

        if agent is None:
            return None

        if action.name == "STAY":
            return agent.position

        nextPosition = getNextPosition(agent.position, action)

        return nextPosition

    def getBox(self, state, agentId, action):
        agent = state.getAgent(agentId)

        if agent is None:
            return None

        if action.name == "STAY":
            return None

        nextPosition = getNextPosition(agent.position, action)

        box = state.boxPosition(nextPosition)

        return box

    def getBoxNextPosition(self, state, agentId, action):
        box = self.getBox(state, agentId, action)

        if box is None:
            return None

        boxNextPosition = getNextPosition(box.position, action)

        return boxNextPosition

    def resolveActions(self, state, action1, action2):
        agent1 = state.getAgent(1)
        agent2 = state.getAgent(2)

        position1 = agent1.position
        position2 = agent2.position

        # Dùng luôn hàm của Rules cha
        canMove1 = self.canMoveAgent(state, 1, action1)
        canMove2 = self.canMoveAgent(state, 2, action2)

        # Nếu Agent 1 đi được thì tính vị trí tiếp theo
        if canMove1:
            nextPosition1 = self.getAgentNextPosition(state, 1, action1)
            box1 = self.getBox(state, 1, action1)
            boxNextPosition1 = self.getBoxNextPosition(state, 1, action1)
        else:
            nextPosition1 = position1
            box1 = None
            boxNextPosition1 = None

        # Nếu Agent 2 đi được thì tính vị trí tiếp theo
        if canMove2:
            nextPosition2 = self.getAgentNextPosition(state, 2, action2)
            box2 = self.getBox(state, 2, action2)
            boxNextPosition2 = self.getBoxNextPosition(state, 2, action2)
        else:
            nextPosition2 = position2
            box2 = None
            boxNextPosition2 = None

        # Hai Agent cùng đi vào một ô
        if nextPosition1 == nextPosition2:
            canMove1 = False
            canMove2 = False

        # Hai Agent đổi chỗ cho nhau
        if nextPosition1 == position2:
            if nextPosition2 == position1:
                canMove1 = False
                canMove2 = False

        # Hai Agent cùng đẩy một box
        if box1 is not None:
            if box2 is not None:
                if box1 is box2:
                    canMove1 = False
                    canMove2 = False

        # Box của Agent 1 đi vào vị trí Agent 2 sẽ đứng
        if boxNextPosition1 is not None:
            if boxNextPosition1 == nextPosition2:
                canMove1 = False
                canMove2 = False

        # Box của Agent 2 đi vào vị trí Agent 1 sẽ đứng
        if boxNextPosition2 is not None:
            if boxNextPosition2 == nextPosition1:
                canMove1 = False
                canMove2 = False

        # Hai box bị đẩy vào cùng một ô
        if boxNextPosition1 is not None:
            if boxNextPosition2 is not None:
                if boxNextPosition1 == boxNextPosition2:
                    canMove1 = False
                    canMove2 = False

        return canMove1, canMove2