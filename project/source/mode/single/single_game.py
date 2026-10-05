from ...algorithms.astar import AStar
from ...algorithms.ucs import UCS
from .core.problem import SokobanProblem


class SingleMain:
    def run(self, state, algorithm_name):
        problem = SokobanProblem(state)

        if algorithm_name == "A*":
            algorithm = AStar()
        elif algorithm_name == "UCS":
            algorithm = UCS()
        else:
            return []

        result = algorithm.solve(problem)

        return result.actions