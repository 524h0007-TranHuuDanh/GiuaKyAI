import heapq

from .node import Node
from .search_base import SearchAlgorithm, SearchResult
from .heuristic import Heuristic


class AStar(SearchAlgorithm):
    def __init__(self, record=False, node_limit=None):
        self.record = record
        self.node_limit = node_limit

    def solve(self, problem):
        init = problem.initial_state

        h_func = Heuristic(init.goals, init.walls, init.width, init.height)
        start_node = Node(state=init, cost=0)
        h_start = h_func(init)

        frontier = [(h_start, 0, 0, start_node)]
        counter = 1

        best_cost = {init.key(): 0}
        explored_states = [] if self.record else None
        nodes_expanded = 0
        max_frontier = 1

        while frontier:
            f, neg_g, _, node = heapq.heappop(frontier)
            g = -neg_g
            key = node.state.key()

            if key in best_cost and g > best_cost[key]:
                continue

            nodes_expanded += 1

            if self.record:
                explored_states.append(key)

            if problem.goal_test(node.state):
                actions = self.reconstruct(node)
                return SearchResult(
                    solved=True,
                    actions=actions,
                    total_cost=node.cost,
                    nodes_expanded=nodes_expanded,
                    max_frontier=max_frontier,
                    explored_states=explored_states,
                )

            if self.node_limit is not None and nodes_expanded >= self.node_limit:
                break

            for action in problem.actions(node.state):
                next_state = problem.result(node.state, action)
                next_key = next_state.key()
                next_g = node.cost + problem.step_cost(node.state, action, next_state)

                if next_key in best_cost and next_g >= best_cost[next_key]:
                    continue

                next_h = h_func(next_state)
                if next_h == float("inf"):
                    continue

                best_cost[next_key] = next_g
                next_node = Node(state=next_state, parent=node, action=action, cost=next_g)
                heapq.heappush(frontier, (next_g + next_h, -next_g, counter, next_node))
                counter += 1

            if len(frontier) > max_frontier:
                max_frontier = len(frontier)

        return SearchResult(
            solved=False,
            actions=[],
            total_cost=0,
            nodes_expanded=nodes_expanded,
            max_frontier=max_frontier,
            explored_states=explored_states,
        )