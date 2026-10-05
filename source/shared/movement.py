from .position import get_next_position


class Movement:
    def __init__(self, rules):
        self.rules = rules

    def move_agent(self, state, agent_id, action):
        new_state = state.copy()

        if not self.rules.can_move_agent(state, agent_id, action):
            return new_state

        if action.name == "STAY":
            return new_state

        agent = new_state.get_agent(agent_id)
        next_position = get_next_position(agent, action)

        if next_position in new_state.boxes:
            box_next_position = get_next_position(next_position, action)
            new_state.boxes.remove(next_position)
            new_state.boxes.add(box_next_position)

        new_state.set_agent(agent_id, next_position)
        return new_state