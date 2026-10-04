from .position import get_next_position


class Movement:
    def __init__(self, rules):
        self.rules = rules

    def move_agent(self, state, agent_id, action):
        can_move = self.rules.can_move_agent(state, agent_id, action)

        if can_move == False:
            new_state = state.copy()
            return new_state

        new_state = state.copy()

        agent = new_state.get_agent(agent_id)

        if action.name == "STAY":
            return new_state

        current_position = agent.position
        next_position = get_next_position(current_position, action)

        box = new_state.box_position(next_position)

        if box is not None:
            box_position = box.position
            box_next_position = get_next_position(box_position, action)

            box.position = box_next_position

            if new_state.is_goal(box_next_position):
                box.owner = agent_id
            else:
                box.owner = None

        agent.position = next_position

        new_state.step_count = new_state.step_count + 1

        return new_state