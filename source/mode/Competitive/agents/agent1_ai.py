from ....algorithms.astar import AStar
from ....shared.action import Action
from ..core.competitive_problem import CompetitiveProblem


class Agent1AI:
    def choose_action(self, state):
        problem = CompetitiveProblem(state, 1)
        result = AStar().solve(problem)

        if result.solved and result.actions:
            return result.actions[0]

        return Action.STAY