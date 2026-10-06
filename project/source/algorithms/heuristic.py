def is_dead_corner(state, box):
    if box in state.goals:
        return False

    x, y = box

    up = (x, y - 1) in state.walls
    down = (x, y + 1) in state.walls
    left = (x - 1, y) in state.walls
    right = (x + 1, y) in state.walls

    return (up or down) and (left or right)


def heuristic(state):
    count = 0

    for box in state.boxes:
        if box in state.goals:
            continue

        if is_dead_corner(state, box):
            return float("inf")

        count += 1

    return count


def competitive_heuristic(state, agent_id):
    agent = state.agent1 if agent_id == 1 else state.agent2

    best = float("inf")

    for box in state.boxes:
        if box in state.goals:
            continue

        box_to_goal = min(abs(box[0] - goal[0]) + abs(box[1] - goal[1]) for goal in state.goals)
        agent_to_box = abs(agent[0] - box[0]) + abs(agent[1] - box[1])

        distance = agent_to_box + box_to_goal

        if distance < best:
            best = distance

    return best