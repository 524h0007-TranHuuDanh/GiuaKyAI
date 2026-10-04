from collections import deque

from ..shared.action import Action


class Heuristic:
    def __init__(self, goals, walls, width, height):
        self.goals = goals
        self.walls = walls
        self.width = width
        self.height = height
        self.push_dist = self.compute_push_dist()

    def in_bounds(self, position):
        x, y = position
        return 0 <= x < self.width and 0 <= y < self.height

    def compute_push_dist(self):
        push_dist = {}
        queue = deque()

        for goal in self.goals:
            push_dist[goal] = 0
            queue.append(goal)

        directions = [Action.NORTH, Action.SOUTH, Action.EAST, Action.WEST]

        while queue:
            cell = queue.popleft()
            dist = push_dist[cell]

            for action in directions:
                dx, dy = action.value

                prev_cell = (cell[0] - dx, cell[1] - dy)
                agent_pos = (cell[0] - 2 * dx, cell[1] - 2 * dy)

                if not self.in_bounds(prev_cell):
                    continue
                if not self.in_bounds(agent_pos):
                    continue
                if prev_cell in self.walls:
                    continue
                if agent_pos in self.walls:
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
                return float("inf")

        return total