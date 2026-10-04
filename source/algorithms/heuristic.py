def heuristic(state):
    count = 0
    for box in state.boxes:
        if box in state.goals:
            continue

        x, y = box
        up = (x, y - 1) in state.walls
        down = (x, y + 1) in state.walls
        left = (x - 1, y) in state.walls
        right = (x + 1, y) in state.walls

        if (up or down) and (left or right):
            return float("inf")

        count += 1

    return count