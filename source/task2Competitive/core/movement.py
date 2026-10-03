class Movement:
    def __init__(self, rules):
        self.rules = rules

    # Di chuyển một Agent
    def moveAgent(self, gameState, agentId, action):
        agent = gameState.getAgent(agentId)

        if agent is None:
            return False

        # Hỏi Rules xem có đi được không
        canMove = self.rules.canMoveAgent(gameState, agentId, action)

        if canMove == False:
            return False

        # Tính vị trí mới
        currentPosition = agent.position

        nextPosition = self.rules.getNextPosition(currentPosition, action)

        # Kiểm tra phía trước có box không
        box = gameState.boxPosition(nextPosition)

        # Nếu có box thì đẩy box
        if box is not None:
            boxPosition = box.position

            boxNextPosition = self.rules.getNextPosition(boxPosition, action)

            box.position = boxNextPosition

        # Di chuyển Agent
        agent.position = nextPosition

        return True