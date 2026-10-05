from .position import get_next_position


class Rules:
    def __init__(self, walls):
        self.walls = set(walls)

    def is_wall(self, position):
        return position in self.walls

    def can_move_agent(self, state, agent_id, action):
        agent = state.get_agent(agent_id)

        if agent is None:
            return False

        if action.name == "STAY":
            return True

        next_position = get_next_position(agent, action)

        if not state.is_inside(next_position):
            return False

        if self.is_wall(next_position):
            return False

        if not state.is_box(next_position):
            return True

        box_next_position = get_next_position(next_position, action)

        if not state.is_inside(box_next_position):
            return False

        if self.is_wall(box_next_position):
            return False

        if state.is_box(box_next_position):
            return False

        return True