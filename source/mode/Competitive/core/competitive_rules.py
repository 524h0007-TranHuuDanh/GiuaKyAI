from ....shared.position import get_next_position


class CompetitiveRules:
    def resolve_actions(self, state, action1, action2):
        can_move_1 = self.can_move(state, 1, action1)
        can_move_2 = self.can_move(state, 2, action2)

        next1 = state.agent1
        next2 = state.agent2

        if action1.name != "STAY":
            next1 = get_next_position(state.agent1, action1)

        if action2.name != "STAY":
            next2 = get_next_position(state.agent2, action2)

        if can_move_1 and can_move_2:
            if next1 == next2:
                can_move_1 = False
                can_move_2 = False

            elif next1 == state.agent2 and next2 == state.agent1:
                can_move_1 = False
                can_move_2 = False

        return can_move_1, can_move_2

    def can_move(self, state, agent_id, action):
        if action.name == "STAY":
            return True

        agent = state.get_agent(agent_id)
        next_position = get_next_position(agent, action)

        if not state.is_inside(next_position):
            return False

        if state.is_wall(next_position):
            return False

        other_agent = state.agent2 if agent_id == 1 else state.agent1

        if next_position == other_agent:
            return False

        if next_position in state.boxes:
            box_next = get_next_position(next_position, action)
            if not state.is_inside(box_next): return False
            if state.is_wall(box_next): return False
            if box_next in state.boxes: return False
            if box_next == other_agent: return False

        return True