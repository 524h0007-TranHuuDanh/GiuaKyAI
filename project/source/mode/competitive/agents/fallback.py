from ....shared.action import Action


def fallback_move(state, problem):
    actions = problem.actions(state)

    for action in actions:
        if action != Action.STAY:
            return action

    return Action.STAY