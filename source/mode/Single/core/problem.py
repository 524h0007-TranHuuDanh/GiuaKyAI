from ....shared.action import Action
from ....shared.position import get_next_position


class SokobanProblem:
    def __init__(self, initial_state):
        self.initial_state = initial_state

    def goal_test(self, state):
        return state.is_solved()

    def actions(self, state):
        valid_actions = []

        for action in [Action.NORTH, Action.SOUTH, Action.EAST, Action.WEST]:
            next_position = get_next_position(state.agent1, action)

            if not state.is_inside(next_position):
                continue

            if next_position in state.walls:
                continue

            if next_position in state.boxes:
                box_next = get_next_position(next_position, action)

                if not state.is_inside(box_next):
                    continue
                if box_next in state.walls:
                    continue
                if box_next in state.boxes:
                    continue

            valid_actions.append(action)

        return valid_actions

    def result(self, state, action):
        new_state = state.copy()
        next_position = get_next_position(new_state.agent1, action)

        if next_position in new_state.boxes:
            box_next = get_next_position(next_position, action)
            new_state.boxes.remove(next_position)
            new_state.boxes.add(box_next)

        new_state.agent1 = next_position
        return new_state

    def step_cost(self, state, action, next_state):
        return 1
