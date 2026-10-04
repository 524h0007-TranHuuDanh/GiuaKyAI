from .core.competitive_state import CompetitiveState
from .core.competitive_rules import CompetitiveRules
from .core.competitive_movement import CompetitiveMovement
from ...shared.action import Action


class CompetitiveMain:
    def __init__(self):
        self.rules = CompetitiveRules()
        self.movement = CompetitiveMovement(self.rules)

    def run(self, state, max_steps):
        state = CompetitiveState(state.agent1, state.agent2, state.boxes, state.goals, state.walls, state.width, state.height)

        actions = []

        for step in range(max_steps):
            action1 = self.get_action_agent1(state)
            action2 = self.get_action_agent2(state)

            actions.append((action1, action2))

            state = self.movement.move_two_agents(state, action1, action2)

        return actions

    def get_action_agent1(self, state):
        return Action.STAY

    def get_action_agent2(self, state):
        return Action.STAY