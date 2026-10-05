from ....algorithms.UCS import UCS
from ....shared.action import Action
from ..core.competitive_problem import CompetitiveProblem


class Agent2AI:
    def choose_action(self, state):
        problem = CompetitiveProblem(state, 2)
        result = UCS().solve(problem)

        if result.solved and result.actions:
            return result.actions[0]

        return Action.STAY