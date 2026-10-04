from ....shared.movement import Movement
from ....shared.position import get_next_position


class CompetitiveMovement(Movement):
    def __init__(self, rules):
        super().__init__(rules)

    def move_two_agents(self, state, action1, action2):
        can_move_1, can_move_2 = self.rules.resolve_actions(state, action1, action2)

        new_state = state.copy()

        agent1 = new_state.get_agent(1)
        agent2 = new_state.get_agent(2)

        next_position_1 = agent1.position
        next_position_2 = agent2.position

        box1 = None
        box2 = None

        box_next_position_1 = None
        box_next_position_2 = None

        # Tính trước nước đi của Agent 1
        if can_move_1:
            if action1.name != "STAY":
                next_position_1 = get_next_position(agent1.position, action1)

                box1 = new_state.box_position(next_position_1)

                if box1 is not None:
                    box_next_position_1 = get_next_position(box1.position, action1)

        # Tính trước nước đi của Agent 2
        if can_move_2:
            if action2.name != "STAY":
                next_position_2 = get_next_position(agent2.position, action2)

                box2 = new_state.box_position(next_position_2)

                if box2 is not None:
                    box_next_position_2 = get_next_position(box2.position, action2)

        # Di chuyển box của Agent 1
        if can_move_1:
            if box1 is not None:
                box1.position = box_next_position_1

                if new_state.is_goal(box_next_position_1):
                    box1.owner = 1
                else:
                    box1.owner = None

        # Di chuyển box của Agent 2
        if can_move_2:
            if box2 is not None:
                box2.position = box_next_position_2

                if new_state.is_goal(box_next_position_2):
                    box2.owner = 2
                else:
                    box2.owner = None

        # Di chuyển Agent 1
        if can_move_1:
            agent1.position = next_position_1

        # Di chuyển Agent 2
        if can_move_2:
            agent2.position = next_position_2

        new_state.step_count = new_state.step_count + 1

        return new_state