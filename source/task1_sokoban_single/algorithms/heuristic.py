from collections import deque

from shared.constants import MOVE_DELTAS


class Heuristic:
    def __init__(self, goals, walls, width, height):
        self.push_dist = self.compute_push_dist(goals, walls, width, height)

    def in_bounds(self, position, width, height):
        x, y = position
        return 0 <= x < width and 0 <= y < height

    def compute_push_dist(self, goals, walls, width, height):
        push_dist = {}
        queue = deque()

        for goal in goals:
            push_dist[goal] = 0
            queue.append(goal)

        while queue:
            cell = queue.popleft()
            dist = push_dist[cell]

            for dx, dy in MOVE_DELTAS.values():
                # Box ở prev_cell, bị đẩy theo (dx, dy) để đến cell
                prev_cell = (cell[0] - dx, cell[1] - dy)

                # Agent phải đứng sau box để đẩy
                agent_pos = (cell[0] - 2 * dx, cell[1] - 2 * dy)

                if not self.in_bounds(prev_cell, width, height):
                    continue
                if not self.in_bounds(agent_pos, width, height):
                    continue
                if prev_cell in walls:
                    continue
                if agent_pos in walls:
                    continue
                if prev_cell in push_dist:
                    continue

                push_dist[prev_cell] = dist + 1
                queue.append(prev_cell)

        return push_dist

    def __call__(self, state):
        total = 0

        for box in state.boxes:
            if box in state.goals:
                continue

            if box in self.push_dist:
                total += self.push_dist[box]
            else:
                return float('inf')

        return total