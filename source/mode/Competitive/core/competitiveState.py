from ....shared.sokobanState import SokobanState


class CompetitiveState(SokobanState):
    def getScore(self, agentId):
        score = 0

        for box in self.boxes:
            if box.position in self.goals:
                if box.owner == agentId:
                    score += 1

        return score