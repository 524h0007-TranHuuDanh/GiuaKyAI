#file đang bị thừa canMoveAgent và getActionInfo cần gộp hai hàm lại
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
    def boxPosition(self, gameState, position):
        box = gameState.boxPosition(position)
        return box

    # Kiểm tra một Agent có thể di chuyển không
    def canMoveAgent(self, gameState, agentId, action):
        agent = gameState.getAgent(agentId)

        if agent is None:
            return False

        if action.name == "STAY":
            return True

        currentPosition = agent.position
        nextPosition = self.getNextPosition(currentPosition, action)

        # Agent đụng tường
        if self.isWall(nextPosition):
            return False

        # Kiểm tra phía trước có box không
        box = self.boxPosition(gameState, nextPosition)

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
        otherBox = self.boxPosition(gameState, boxNextPosition)

        if otherBox is not None:
            return False

        return True

    #Kt action cuar hai agent
    def getActionInfo(self, gameState, agentId, action):
        agent = gameState.getAgent(agentId)

        if agent is None:
            return {"valid": False, "nextPosition": None, "box": None, "boxNextPosition": None}
        #TH STAY
        if action.name == "STAY":
            return {"valid": True, "nextPosition": agent.position, "box": None, "boxNextPosition": None}

        nextPosition = self.getNextPosition(agent.position, action)

        # Kiểm tra action có hợp lệ không
        if not self.canMoveAgent(gameState, agentId, action):
            return {"valid": False, "nextPosition": nextPosition, "box": None, "boxNextPosition": None}

        # Action hợp lệ thì lấy thông tin box
        box = self.boxPosition(gameState, nextPosition)

        # Không có box
        if box is None:
            return {"valid": True, "nextPosition": nextPosition, "box": None, "boxNextPosition": None}
        # Có box -> lấy vị trí box sẽ được đẩy tới
        boxNextPosition = self.getNextPosition(box.position, action)

        return {"valid": True, "nextPosition": nextPosition, "box": box, "boxNextPosition": boxNextPosition}

    #kiểm tra xung đột giữa hai Agent
    def resolActions(self, gameState, action1, action2):
        #Lấy kế hoạch của hai Agent
        info1 = self.getActionInfo(gameState, 1, action1)
        info2 = self.getActionInfo(gameState, 2, action2)

        # Vị trí ĐẦU
        pos1 = gameState.getAgent(1).position
        pos2 = gameState.getAgent(2).position

        # Action không hợp lệ thì STAY
        if not info1["valid"]:
            info1 = {"valid": True, "nextPosition": pos1, "box": None, "boxNextPosition": None}

        if not info2["valid"]:
            info2 = {"valid": True, "nextPosition": pos2, "box": None, "boxNextPosition": None}

        # Lưu thông tin từ trạng thái bước đầu 
        nextPosition1 = info1["nextPosition"]
        nextPosition2 = info2["nextPosition"]

        boxNextPosition1 = info1["boxNextPosition"]
        boxNextPosition2 = info2["boxNextPosition"]
        # Hai A cùng đi vào một ô
        if nextPosition1 == nextPosition2:
            info1["valid"] = False
            info2["valid"] = False

        # Hai A đổi chỗ
        elif(nextPosition1 == pos2 and nextPosition2 == pos1):
            info1["valid"] = False
            info2["valid"] = False

        else:
            #TH A này vào ô A kia đang chiếm Tdat quyết định giải pháp tạm thời là ko cho nó đi theo ngay từ đầu
            if nextPosition1 == pos2:
                info1["valid"] = False
            if nextPosition2 == pos1:
                info2["valid"] = False

            # Box bị đẩy vào vị trí đầu của A kia
            if boxNextPosition1 == pos2:
                info1["valid"] = False
            if boxNextPosition2 == pos1:
                info2["valid"] = False
            # Box bị đẩy vào ô A kia muốn đi
            if boxNextPosition1 == nextPosition2:
                info1["valid"] = False
                info2["valid"] = False

            if boxNextPosition2 == nextPosition1:
                info1["valid"] = False
                info2["valid"] = False
            # Hai box bị đẩy vào cùng một ô
            if (boxNextPosition1 is not None and boxNextPosition2 is not None and boxNextPosition1 == boxNextPosition2):
                info1["valid"] = False
                info2["valid"] = False
        # Trả về kế hoạch của hai Agent
        return {
            1: info1,
            2: info2
        }