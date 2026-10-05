from ....algorithms.ucs import Ucs
from ....shared.action import Action
from ..core.competitive_problem import CompetitiveProblem


class Agent2AI:
    def choose_action(self, state):
        problem = CompetitiveProblem(state, 2)
        result = Ucs(time_limit=1000).solve(problem)

        if result.actions:
            return result.actions[0]

        return Action.STAY