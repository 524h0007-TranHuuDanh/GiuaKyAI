from .action import Action
from .gameState import GameState
"""Luật:
không đụng wall
Có đẩy box không
Box phía trước có wall không
Hai agent có đụng nhau không
Hai agent có đổi chỗ cho nhau không
Sau khi thực hiện action, box nằm ở đâu
Cập nhật GameState."""
class Rules:
    def __init__(self, walls):
        self.walls = walls

#vị trí di chuyển mới
    def getNextPosition(self, position, action):
        dx, dy = action.value
        x, y = position
        return x + dx, y + dy
#xđ có phải tường ko
    def isWall(self, position):
        return position in self.walls

#vị trí box
    def boxPosition(self, state, position):
        return state.boxPosition(position)

    def can_move_agent(self, state, agentId, action):
        agent = state.getAgent(agentId)
        if agent is None:
            return False
        #di chuyển
        nextPosition = self.getNextPosition(agent.position, action)
        #KT tường
        if self.isWall(nextPosition):
            return False

        box = self.boxPosition(state, nextPosition)
        if box is None:
            return True

        boxNextPosition = self.getNextPosition(nextPosition, action)

        if self.isWall(boxNextPosition):
            return False

        if self.boxPosition(state, boxNextPosition) is not None:
            return False
        return True

#xly di chuyeenr của một Agent
    def applyAgentAction(self, state, agentId, action):
        agent = state.getAgent(agentId)

        if agent is None:
            return False

        if not self.can_move_agent(state, agentId, action):
            return False

        nextPosition = self.getNextPosition(agent.position, action)

        box = self.boxPosition(state, nextPosition)

        if box is not None:
            box.position = self.getNextPosition(nextPosition, action)
            agent.position = nextPosition
        agent.position = nextPosition
        return True
#xly di chuyển cho 2 Agent cùng lúc
    def applyAction(self, state, action1, action2):
        newState = state.copy()

        agent1 = newState.getAgent(1)
        agent2 = newState.getAgent(2)

        move1 = self.getNextPosition(agent1.position, action1)
        move2 = self.getNextPosition(agent2.position, action2)

        valid1 = True
        valid2 = True
#check tường
        if self.isWall(move1):
            valid1 = False

        if self.isWall(move2):
            valid2 = False

#đi vào chung 1 ô
        if move1 == move2:
            valid1 = False
            valid2 = False

#chặn hai agent đổi chổ cho nhau
        if move1 == agent2.position and move2 == agent1.position:
            valid1 = False
            valid2 = False
#kt box của A1
        box1 = self.boxPosition(newState, move1)
        if valid1 and box1 is not None:
            box1Next = self.getNextPosition(move1, action1)
            if self.isWall(box1Next):
                valid1 = False
            elif self.boxPosition(newState, box1Next) is not None:
                valid1 = False
            elif box1Next == move2:
                valid1 = False
#KT box của A2
        box2 = self.boxPosition(newState, move2)
        if valid2 and box2 is not None:
            box2Next = self.getNextPosition(move2, action2)
            if self.isWall(box2Next):
                valid2 = False
            elif self.boxPosition(newState, box2Next) is not None:
                valid2 = False
            elif box2Next == move1:
                valid2 = False

#cập nhật agent
        if valid1:
            if box1 is not None:
                box1.position = self.getNextPosition(box1.position, action1)

        if valid2:
            if box2 is not None:
                box2.position = self.getNextPosition(box2.position, action2)
        newState.stepCount += 1
        return newState

