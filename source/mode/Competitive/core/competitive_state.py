from ....shared.sokoban_state import SokobanState


class CompetitiveState(SokobanState):
    def get_score(self, agent_id):
        score = 0

        for box in self.boxes:
            if box.position in self.goals:
                if box.owner == agent_id:
                    score += 1

        return score