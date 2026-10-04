from ....shared.sokoban_state import SokobanState


class CompetitiveState(SokobanState):
    def get_score(self, agent_id):
        return self.count_boxes_on_goals()
