from ....shared.rules import Rules
from ....shared.position import get_next_position


class CompetitiveRules(Rules):
    def __init__(self, walls):
        super().__init__(walls)

    def get_agent_next_position(self, state, agent_id, action):
        agent = state.get_agent(agent_id)

        if agent is None:
            return None

        if action.name == "STAY":
            return agent.position

        next_position = get_next_position(agent.position, action)

        return next_position

    def get_box(self, state, agent_id, action):
        agent = state.get_agent(agent_id)

        if agent is None:
            return None

        if action.name == "STAY":
            return None

        next_position = get_next_position(agent.position, action)

        box = state.box_position(next_position)

        return box

    def get_box_next_position(self, state, agent_id, action):
        box = self.get_box(state, agent_id, action)

        if box is None:
            return None

        box_next_position = get_next_position(box.position, action)

        return box_next_position

    def resolve_actions(self, state, action1, action2):
        agent1 = state.get_agent(1)
        agent2 = state.get_agent(2)

        position1 = agent1.position
        position2 = agent2.position

        # Dùng luôn hàm của Rules cha
        can_move_1 = self.can_move_agent(state, 1, action1)
        can_move_2 = self.can_move_agent(state, 2, action2)

        # Nếu Agent 1 đi được thì tính vị trí tiếp theo
        if can_move_1:
            next_position_1 = self.get_agent_next_position(state, 1, action1)
            box1 = self.get_box(state, 1, action1)
            box_next_position_1 = self.get_box_next_position(state, 1, action1)
        else:
            next_position_1 = position1
            box1 = None
            box_next_position_1 = None

        # Nếu Agent 2 đi được thì tính vị trí tiếp theo
        if can_move_2:
            next_position_2 = self.get_agent_next_position(state, 2, action2)
            box2 = self.get_box(state, 2, action2)
            box_next_position_2 = self.get_box_next_position(state, 2, action2)
        else:
            next_position_2 = position2
            box2 = None
            box_next_position_2 = None

        # Hai Agent cùng đi vào một ô
        if next_position_1 == next_position_2:
            can_move_1 = False
            can_move_2 = False

        # Hai Agent đổi chỗ cho nhau
        if next_position_1 == position2:
            if next_position_2 == position1:
                can_move_1 = False
                can_move_2 = False

        # Hai Agent cùng đẩy một box
        if box1 is not None:
            if box2 is not None:
                if box1 is box2:
                    can_move_1 = False
                    can_move_2 = False

        # Box của Agent 1 đi vào vị trí Agent 2 sẽ đứng
        if box_next_position_1 is not None:
            if box_next_position_1 == next_position_2:
                can_move_1 = False
                can_move_2 = False

        # Box của Agent 2 đi vào vị trí Agent 1 sẽ đứng
        if box_next_position_2 is not None:
            if box_next_position_2 == next_position_1:
                can_move_1 = False
                can_move_2 = False

        # Hai box bị đẩy vào cùng một ô
        if box_next_position_1 is not None:
            if box_next_position_2 is not None:
                if box_next_position_1 == box_next_position_2:
                    can_move_1 = False
                    can_move_2 = False

        return can_move_1, can_move_2