from ....shared.rules import Rules
from ....shared.position import get_next_position


class CompetitiveRules(Rules):
    def get_next_position(self, state, agent_id, action):
        agent = state.get_agent(agent_id)

        if agent is None:
            return None

        if action.name == "STAY":
            return agent

        return get_next_position(agent, action)

    def get_box_next_position(self, state, agent_id, action):
        agent = state.get_agent(agent_id)

        if agent is None or action.name == "STAY":
            return None

        next_position = get_next_position(agent, action)

        if next_position not in state.boxes:
            return None

        return get_next_position(next_position, action)

    def resolve_actions(self, state, action1, action2):
        can_move_1 = self.can_move_agent(state, 1, action1)
        can_move_2 = self.can_move_agent(state, 2, action2)

        next_1 = self.get_next_position(state, 1, action1)
        next_2 = self.get_next_position(state, 2, action2)
        box_next_1 = self.get_box_next_position(state, 1, action1)
        box_next_2 = self.get_box_next_position(state, 2, action2)

        if can_move_1 and can_move_2:
            if next_1 == next_2:
                can_move_1 = False
                can_move_2 = False

            if next_1 == state.agent2 and next_2 == state.agent1:
                can_move_1 = False
                can_move_2 = False

            if box_next_1 is not None and box_next_1 == next_2:
                can_move_1 = False
                can_move_2 = False

            if box_next_2 is not None and box_next_2 == next_1:
                can_move_1 = False
                can_move_2 = False

            if box_next_1 is not None and box_next_1 == box_next_2:
                can_move_1 = False
                can_move_2 = False

        return can_move_1, can_move_2
