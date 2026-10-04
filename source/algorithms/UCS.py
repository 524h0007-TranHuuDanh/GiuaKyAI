import heapq

from .node import Node
from .search_base import SearchAlgorithm, SearchResult


class UCS(SearchAlgorithm):
    def __init__(self, max_nodes=None):
        self.max_nodes = max_nodes

    def solve(self, problem):
        start_node = Node(state=problem.initial_state, cost=0)

        frontier = [(0, 0, start_node)]
        counter = 1
        explored = set()
        nodes_expanded = 0
        max_frontier = 1

        while frontier:
            if self.max_nodes is not None and nodes_expanded >= self.max_nodes:
                break

            g, _, node = heapq.heappop(frontier)
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
                    max_frontier=max_frontier,
                )

            for action in problem.actions(node.state):
                next_state = problem.result(node.state, action)
                next_key = next_state.key()

                if next_key in explored:
                    continue

                next_g = node.cost + problem.step_cost(node.state, action, next_state)
                next_node = Node(state=next_state, parent=node, action=action, cost=next_g)

                heapq.heappush(frontier, (next_g, counter, next_node))
                counter += 1

            if len(frontier) > max_frontier:
                max_frontier = len(frontier)

        return SearchResult(
            solved=False,
            actions=[],
            total_cost=0,
            nodes_expanded=nodes_expanded,
            max_frontier=max_frontier,
        )