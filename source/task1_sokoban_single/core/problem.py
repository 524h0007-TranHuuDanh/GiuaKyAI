from core.state import SokobanState
from shared.constants import MOVE_DELTAS


class SokobanProblem:
    def __init__(self, initial_state):
        self.initial_state = initial_state

    def goal_test(self, state):
        return state.is_goal()
    def actions(self, state):
        valid = []
        ax, ay = state.agent
        for action, (dx, dy) in MOVE_DELTAS.items():
            nx, ny = ax + dx, ay + dy

            # Check biên theo row_lengths
            if not (0 <= ny < state.height):
                continue
            if not (0 <= nx < state.row_lengths[ny]):   
                continue

            next_pos = (nx, ny)
            if next_pos in state.walls:
                continue

            if next_pos in state.boxes:
                bx, by = nx + dx, ny + dy
                # Check biên cho box
                if not (0 <= by < state.height):
                    continue
                if not (0 <= bx < state.row_lengths[by]):  
                    continue
                box_next = (bx, by)
                if box_next in state.walls:
                    continue
                if box_next in state.boxes:
                    continue

            valid.append(action)
        return valid
    def result(self, state, action):
        dx, dy = MOVE_DELTAS[action]
        ax, ay = state.agent
        next_pos = (ax + dx, ay + dy)
        new_boxes = set(state.boxes)

        if next_pos in state.boxes:
            bx, by = next_pos
            box_next = (bx + dx, by + dy)
            new_boxes.remove(next_pos)
            new_boxes.add(box_next)

        return SokobanState(
            agent=next_pos,
            boxes=frozenset(new_boxes),
            goals=state.goals,
            walls=state.walls,
            width=state.width,
            height=state.height,
            row_lengths=state.row_lengths,
        )

    def step_cost(self, state, action, next_state):
        return 1