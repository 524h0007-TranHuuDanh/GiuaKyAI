from ....algorithms.astar import AStar
from ..core.competitive_problem import CompetitiveProblem
from .fallback import fallback_move


class Agent1AI:
    def choose_action(self, state):
        problem = CompetitiveProblem(state, 1)

        def competitive_heuristic(current_state):
            if problem.goal_test(current_state):
                return 0
            return 1

        result = AStar(
            time_limit=1000,
            heuristic_fn=competitive_heuristic
        ).solve(problem)

        if result.solved and result.actions:
            return result.actions[0]

        return fallback_move(state, problem)