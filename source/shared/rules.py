from .position import get_next_position


class Rules:
    def __init__(self, walls):
        self.walls = walls

    def is_wall(self, position):
        if position in self.walls:
            return True

        return False

    def can_move_agent(self, state, agent_id, action):
        agent = state.get_agent(agent_id)

        if agent is None:
            return False

        if action.name == "STAY":
            return True

        current_position = agent.position
        next_position = get_next_position(current_position, action)

        if self.is_wall(next_position):
            return False

        box = state.box_position(next_position)

        if box is None:
            return True

        box_position = box.position
        box_next_position = get_next_position(box_position, action)

        if self.is_wall(box_next_position):
            return False

        other_box = state.box_position(box_next_position)

        if other_box is not None:
            return False

        return True