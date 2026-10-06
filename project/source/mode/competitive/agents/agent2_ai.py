from ....algorithms.ucs import Ucs
from ..core.competitive_problem import CompetitiveProblem
from .fallback import fallback_move


class Agent2AI:
    def choose_action(self, state):
        problem = CompetitiveProblem(state, 2)
        result = Ucs(time_limit=1000).solve(problem)

        if result.solved and result.actions:
            return result.actions[0]

        return fallback_move(state, problem)