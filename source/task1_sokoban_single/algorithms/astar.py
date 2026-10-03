import heapq
import time
import tracemalloc
from core.node import Node
from algorithms.search_base import SearchAlgorithm, SearchResult
from algorithms.heuristic import Heuristic


class AStar(SearchAlgorithm):
    def solve(self, problem):
        tracemalloc.start()
        start_time = time.perf_counter()

        # Tạo heuristic 1 lần
        h_func = Heuristic(
            problem.initial_state.goals,
            problem.initial_state.walls,
            problem.initial_state.width,
            problem.initial_state.height,
        )

        frontier = []
        explored = set()
        counter = 0

        start_node = Node(state=problem.initial_state, cost=0)
        h_start = h_func(problem.initial_state)
        heapq.heappush(frontier, (h_start, counter, start_node))

        max_frontier = 1
        nodes_expanded = 0

        while frontier:
            _, _, node = heapq.heappop(frontier)

            if node.state in explored:
                continue
            explored.add(node.state)
            nodes_expanded += 1

            if problem.goal_test(node.state):
                actions = []
                current = node
                while current.parent is not None:
                    actions.append(current.action)
                    current = current.parent
                actions.reverse()

                _, peak = tracemalloc.get_traced_memory()
                tracemalloc.stop()

                return SearchResult(
                    actions=actions,
                    total_cost=node.cost,
                    nodes_expanded=nodes_expanded,
                    time=time.perf_counter() - start_time,
                    max_frontier=max_frontier,
                    memory=peak / (1024 * 1024),
                    solved=True,
                )

            for action in problem.actions(node.state):
                next_state = problem.result(node.state, action)
                if next_state in explored:
                    continue

                step_cost = problem.step_cost(node.state, action, next_state)
                new_g = node.cost + step_cost
                new_h = h_func(next_state)
                new_f = new_g + new_h

                child = Node(
                    state=next_state,
                    parent=node,
                    action=action,
                    cost=new_g,
                )

                counter += 1
                heapq.heappush(frontier, (new_f, counter, child))
                if len(frontier) > max_frontier:
                    max_frontier = len(frontier)

        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        return SearchResult(
            nodes_expanded=nodes_expanded,
            time=time.perf_counter() - start_time,
            max_frontier=max_frontier,
            memory=peak / (1024 * 1024),
            solved=False,
        )