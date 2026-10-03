from .agent import Agent
from .box import Box

class GameState:
    def __init__(self, agents, boxes, goals, stepCount = 0):
        self.agents = agents
        self.boxes = boxes
        self.goals = goals
        self.stepCount = stepCount
    #lấy agent
    def getAgent(self, agentId):
        for agent in self.agents:
            if agent.agentId == agentId:
                return agent
        return None

    #check vị trí box
    def boxPosition(self, position):
        for box in self.boxes:
            #VD: state.boxPosition((3,4)) --> nếu có box ở 3,4 thì trả về box
            if box.position == position:
                return box
        return None

    def isGoal(self, position):
        return position in self.goals #state.is_goal((3, 4)): nếu true thì 3,4 là goal

    #số lượng box nằm trên goal
    def countBoxesOnGoals(self):
        count = 0
        for box in self.boxes:
            if box.position in self.goals:
                count += 1
        return count
    #hàm tạo bản sau
    def copy(self):
        agents = [
            Agent(agent.agentId, agent.position)
            for agent in self.agents
        ]

        boxes = [
            Box(box.position, box.owner)
            for box in self.boxes
        ]

        return GameState(
            agents=agents,
            boxes=boxes,
            goals=list(self.goals),
            stepCount=self.stepCount
        )
    #điểm của 1 Agent
    def getScore(self, agentId):
        score = 0
        for box in self.boxes:
            if (box.position in self.goals and box.owner == agentId):
                score += 1
        return score
    #chênh lệch điểm
    def getScoreDifference(self):
        return self.getScore(1) - self.getScore(2)
