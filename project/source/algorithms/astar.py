import heapq
import time

from .node import Node
from .search_base import SearchAlgorithm, SearchResult
from .heuristic import heuristic
from ..shared.action import Action


class AStar(SearchAlgorithm):
    def __init__(self, time_limit=0, heuristic_fn=None):
        self.time_limit = time_limit

        if heuristic_fn is None:
            self.heuristic_fn = heuristic
        else:
            self.heuristic_fn = heuristic_fn

    def solve(self, problem):
        start_node = Node(state=problem.initial_state, cost=0)

        frontier = [(self.heuristic_fn(problem.initial_state), 0, start_node)] # lưu f = g + h, counter, node

        counter = 1
        explored = set()
        nodes_expanded = 0
        max_frontier = 1

        start_time = time.time()   

        while frontier:
            #check thời gian 
            if self.time_limit > 0:
                elapsed_ms = (time.time() - start_time) * 1000
                if elapsed_ms > self.time_limit:
                    return SearchResult(
                        solved=False,
                        actions=[],
                        total_cost=0,
                        nodes_expanded=nodes_expanded,
                        max_frontier=max_frontier,
                    )

            #lấy node có f nhỏ nhất
            f, _, node = heapq.heappop(frontier)
            key = node.state.key()

            if key in explored:
                continue

            explored.add(key)
            nodes_expanded += 1

            #tìm thấy goal 
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

                next_h = self.heuristic_fn(next_state)
                #h vô cực thì bỏ qua
                if next_h == float("inf"):
                    continue

                next_g = node.cost + problem.step_cost(node.state, action, next_state)
                next_node = Node(state=next_state, parent=node, action=action, cost=next_g)

                #f(n') = g(n') + h(n')
                heapq.heappush(frontier, (next_g + next_h, counter, next_node))
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