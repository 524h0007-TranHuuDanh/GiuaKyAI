from ....shared.action import Action
from ....shared.rules import Rules
from ....shared.movement import Movement


class SokobanProblem:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.rules = Rules(initial_state.walls)
        self.movement = Movement(self.rules)

    def actions(self, state):
        valid = []
        for action in [Action.NORTH, Action.SOUTH, Action.EAST, Action.WEST]:
            if self.rules.can_move_agent(state, 1, action):
                valid.append(action)
        return valid

    def result(self, state, action):
        return self.movement.move_agent(state, 1, action)
        
    def goal_test(self, state):
        return state.is_solved()

    def step_cost(self, state, action, next_state):
        return 1