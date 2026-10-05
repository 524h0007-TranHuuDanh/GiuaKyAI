from .core.competitive_state import CompetitiveState
from .core.competitive_rules import CompetitiveRules
from .core.competitive_move import CompetitiveMovement
from .agents.agent1_ai import Agent1AI
from .agents.agent2_ai import Agent2AI


class CompetitiveMain:
    def __init__(self):
        self.agent1_ai = Agent1AI()
        self.agent2_ai = Agent2AI()

    def run(self, state, max_steps):
        state = CompetitiveState(state.agent1, state.agent2, state.boxes, state.goals, state.walls, state.width, state.height)

        self.rules = CompetitiveRules(state.walls)
        self.movement = CompetitiveMovement(self.rules)

        actions = []

        for step in range(max_steps):
            action1 = self.agent1_ai.choose_action(state.copy())
            action2 = self.agent2_ai.choose_action(state.copy())

            actions.append((action1, action2))

            state = self.movement.move_two_agents(state, action1, action2)

        return actions