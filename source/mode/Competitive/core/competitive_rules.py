from ....shared.position import get_next_position


class CompetitiveRules:
    # THÊM: __init__ nhận walls. Code cũ không có __init__ nên gọi
    # CompetitiveRules(state.walls) sẽ lỗi "takes no arguments"
    def __init__(self, walls):
        self.walls = set(walls)

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
            # SỬA: code cũ gán can_move_1 = False, can_move_2 = False rồi rơi xuống return
            # Đổi thành return False, False để thoát ngay
            if next1 == next2:
                return False, False

            # SỬA: code cũ dùng elif. Vì đã return ở trên nên đổi thành if
            if next1 == state.agent2 and next2 == state.agent1:
                return False, False

            # THÊM: code cũ thiếu. Box của agent 1 đẩy vào ô agent 2 sẽ đứng
            # -> box và agent 2 trùng ô, vi phạm "không đi xuyên qua nhau"
            if next1 in state.boxes:
                box1_next = get_next_position(next1, action1)
                if box1_next == next2:
                    return False, False

            # THÊM: code cũ thiếu. Box của agent 2 đẩy vào ô agent 1 sẽ đứng
            if next2 in state.boxes:
                box2_next = get_next_position(next2, action2)
                if box2_next == next1:
                    return False, False

            # THÊM: code cũ thiếu. Hai box đẩy vào cùng 1 ô
            # boxes là set nên 2 box cùng ô sẽ mất 1 -> phải hủy cả 2 action
            if next1 in state.boxes and next2 in state.boxes:
                box1_next = get_next_position(next1, action1)
                box2_next = get_next_position(next2, action2)
                if box1_next == box2_next:
                    return False, False

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