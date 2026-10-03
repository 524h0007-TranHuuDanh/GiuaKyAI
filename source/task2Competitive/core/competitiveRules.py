from ...shared.position import getNextPosition


class CompetitiveRules:
    def __init__(self, rules):
        self.rules = rules

    def getNextPosition(self, state, agentId, action):
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

        canMove1 = self.rules.canMoveAgent(state, 1, action1)
        canMove2 = self.rules.canMoveAgent(state, 2, action2)

        position1 = agent1.position
        position2 = agent2.position

        # Nếu action không hợp lệ thì xem như Agent đứng yên
        if canMove1:
            nextPosition1 = self.getNextPosition(state, 1, action1)
            box1 = self.getBox(state, 1, action1)
            boxNextPosition1 = self.getBoxNextPosition(state, 1, action1)
        else:
            nextPosition1 = position1
            box1 = None
            boxNextPosition1 = None

        if canMove2:
            nextPosition2 = self.getNextPosition(state, 2, action2)
            box2 = self.getBox(state, 2, action2)
            boxNextPosition2 = self.getBoxNextPosition(state, 2, action2)
        else:
            nextPosition2 = position2
            box2 = None
            boxNextPosition2 = None

        # Hai Agent cùng muốn vào một ô
        if nextPosition1 == nextPosition2:
            if nextPosition1 != position1 or nextPosition2 != position2:
                canMove1 = False
                canMove2 = False

        # Hai Agent đổi chỗ cho nhau
        if nextPosition1 == position2:
            if nextPosition2 == position1:
                canMove1 = False
                canMove2 = False

        # Agent 1 đi vào vị trí hiện tại của Agent 2
        if nextPosition1 == position2:
            if nextPosition2 != position2:
                canMove1 = False

        # Agent 2 đi vào vị trí hiện tại của Agent 1
        if nextPosition2 == position1:
            if nextPosition1 != position1:
                canMove2 = False

        # Box do Agent 1 đẩy vào vị trí Agent 2
        if boxNextPosition1 is not None:
            if boxNextPosition1 == position2:
                canMove1 = False

        # Box do Agent 2 đẩy vào vị trí Agent 1
        if boxNextPosition2 is not None:
            if boxNextPosition2 == position1:
                canMove2 = False

        # Box Agent 1 đi vào nơi Agent 2 muốn đi
        if boxNextPosition1 is not None:
            if boxNextPosition1 == nextPosition2:
                canMove1 = False
                canMove2 = False

        # Box Agent 2 đi vào nơi Agent 1 muốn đi
        if boxNextPosition2 is not None:
            if boxNextPosition2 == nextPosition1:
                canMove1 = False
                canMove2 = False

        # Hai Agent cùng đẩy một box
        if box1 is not None:
            if box2 is not None:
                if box1 is box2:
                    canMove1 = False
                    canMove2 = False

        # Hai box bị đẩy vào cùng một ô
        if boxNextPosition1 is not None:
            if boxNextPosition2 is not None:
                if boxNextPosition1 == boxNextPosition2:
                    canMove1 = False
                    canMove2 = False

        return canMove1, canMove2