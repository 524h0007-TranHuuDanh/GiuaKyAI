class Rules:
    def __init__(self, walls):
        self.walls = walls

    # Lấy vị trí mới sau khi di chuyển
    def getNextPosition(self, position, action):
        x, y = position
        dx, dy = action.value

        newX = x + dx
        newY = y + dy

        newPosition = (newX, newY)
        return newPosition

    # Kiểm tra có phải tường không
    def isWall(self, position):
        if position in self.walls:
            return True

        return False

    # Tìm box tại vị trí
    def boxPosition(self, state, position):
        box = state.boxPosition(position)
        return box

    # Kiểm tra một Agent có thể di chuyển không
    def canMoveAgent(self, state, agentId, action):
        agent = state.getAgent(agentId)

        if agent is None:
            return False

        currentPosition = agent.position
        nextPosition = self.getNextPosition(currentPosition, action)

        # Agent đụng tường
        if self.isWall(nextPosition):
            return False

        # Kiểm tra phía trước có box không
        box = self.boxPosition(state, nextPosition)

        # Không có box -> đi được
        if box is None:
            return True

        # Có box -> kiểm tra vị trí phía sau box
        boxPosition = box.position
        boxNextPosition = self.getNextPosition(boxPosition, action)

        # Box đụng tường
        if self.isWall(boxNextPosition):
            return False

        # Box đụng box khác
        otherBox = self.boxPosition(state, boxNextPosition)

        if otherBox is not None:
            return False

        return True