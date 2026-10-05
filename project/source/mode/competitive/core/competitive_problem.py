from ....shared.action import Action
from .competitive_rules import CompetitiveRules
from .competitive_move import CompetitiveMovement


class CompetitiveProblem:
    def __init__(self, initial_state, agent_id):
        self.initial_state = initial_state
        self.agent_id = agent_id
        self.rules = CompetitiveRules(initial_state.walls)
        self.movement = CompetitiveMovement(self.rules)
        self.start_score = initial_state.get_score(agent_id)

    def goal_test(self, state):
        return state.get_score(self.agent_id) > self.start_score

    def actions(self, state):
        valid = []
        for action in [Action.NORTH, Action.SOUTH, Action.EAST, Action.WEST]:
            if self.rules.can_move(state, self.agent_id, action):
                valid.append(action)
        return valid

    def result(self, state, action):
        new_state = state.copy()
        self.movement.move_one(new_state, self.agent_id, action, True)
        return new_state

    def step_cost(self, state, action, next_state):
        return 1