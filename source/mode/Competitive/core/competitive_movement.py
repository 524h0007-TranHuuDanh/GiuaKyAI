from ....shared.position import get_next_position


class CompetitiveMovement:
    def __init__(self, rules):
        self.rules = rules

    def move_two_agents(self, state, action1, action2):
        can_move_1, can_move_2 = self.rules.resolve_actions(state, action1, action2)
        new_state = state.copy()

        self.move_one(new_state, 1, action1, can_move_1)
        self.move_one(new_state, 2, action2, can_move_2)

        return new_state

    def move_one(self, state, agent_id, action, can_move):
        if not can_move or action.name == "STAY":
            return

        agent = state.get_agent(agent_id)
        next_position = get_next_position(agent, action)

        if next_position in state.boxes:
            box_next = get_next_position(next_position, action)
            state.boxes.remove(next_position)
            state.boxes.add(box_next)

        state.set_agent(agent_id, next_position)
