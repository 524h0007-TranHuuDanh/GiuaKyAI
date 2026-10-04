import heapq

from .node import Node
from .search_base import SearchAlgorithm, SearchResult
from .heuristic import heuristic


class AStar(SearchAlgorithm):
    def solve(self, problem):
        start_node = Node(state=problem.initial_state, cost=0)

        frontier = [(heuristic(problem.initial_state), 0, start_node)]
        counter = 1
        explored = set()
        nodes_expanded = 0
        max_frontier = 1

        while frontier:
            f, _, node = heapq.heappop(frontier)
            key = node.state.key()

            if key in explored:
                continue

            explored.add(key)
            nodes_expanded += 1

            if problem.goal_test(node.state):
                actions = self.reconstruct(node)

                return SearchResult(
                    solved=True,
                    actions=actions,
                    total_cost=node.cost,
                    nodes_expanded=nodes_expanded,
                    max_frontier=max_frontier
                )

            for action in problem.actions(node.state):
                next_state = problem.result(node.state, action)
                next_key = next_state.key()

                if next_key in explored:
                    continue

                next_h = heuristic(next_state)

                if next_h == float("inf"):
                    continue

                next_g = node.cost + problem.step_cost(node.state, action, next_state)
                next_node = Node(state=next_state, parent=node, action=action, cost=next_g)

                heapq.heappush(frontier, (next_g + next_h, counter, next_node))
                counter += 1

            if len(frontier) > max_frontier:
                max_frontier = len(frontier)

        return SearchResult(
            solved=False,
            actions=[],
            total_cost=0,
            nodes_expanded=nodes_expanded,
            max_frontier=max_frontier
        )