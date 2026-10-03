from source.shared.action import Action
from source.shared.agent import Agent
from source.shared.box import Box
from core.gameState import GameState
from source.shared.rules import Rules
from source.shared.movement import Movement

def createState(agents, boxes, goals, walls):
    state = GameState(
        agents=agents,
        boxes=boxes,
        goals=goals
    )

    rules = Rules(walls)
    movement = Movement(rules)

    return state, movement

def test_normal_move():
    agents = [
        Agent(1, (0, 0)),
        Agent(2, (5, 5))
    ]

    boxes = []

    goals = []

    walls = set()

    state, movement = createState(
        agents,
        boxes,
        goals,
        walls
    )

    newState = movement.applyActions(
        state,
        Action.EAST,
        Action.STAY
    )

    assert newState.getAgent(1).position == (1, 0)
    assert newState.getAgent(2).position == (5, 5)

    print("PASS: normal move")

def test_stay():
    agents = [
        Agent(1, (0, 0)),
        Agent(2, (5, 5))
    ]

    state, movement = createState(
        agents,
        [],
        [],
        set()
    )

    newState = movement.applyActions(
        state,
        Action.STAY,
        Action.STAY
    )

    assert newState.getAgent(1).position == (0, 0)
    assert newState.getAgent(2).position == (5, 5)

    assert newState.stepCount == 1

    print("PASS: stay")

def test_box_wall():
    agents = [
        Agent(1, (0, 0)),
        Agent(2, (5, 5))
    ]

    boxes = [
        Box((1, 0))
    ]

    walls = {
        (2, 0)
    }

    state, movement = createState(
        agents,
        boxes,
        [],
        walls
    )

    newState = movement.applyActions(
        state,
        Action.EAST,
        Action.STAY
    )

    assert newState.getAgent(1).position == (0, 0)
    assert newState.boxPosition((1, 0)) is not None

    print("PASS: box blocked by wall")

def test_same_target():
    agents = [
        Agent(1, (0, 0)),
        Agent(2, (2, 0))
    ]

    state, movement = createState(
        agents,
        [],
        [],
        set()
    )

    newState = movement.applyActions(
        state,
        Action.EAST,
        Action.WEST
    )

    assert newState.getAgent(1).position == (0, 0)
    assert newState.getAgent(2).position == (2, 0)

    print("PASS: same target")

def test_swap_position():
    agents = [
        Agent(1, (0, 0)),
        Agent(2, (1, 0))
    ]

    state, movement = createState(
        agents,
        [],
        [],
        set()
    )

    newState = movement.applyActions(
        state,
        Action.EAST,
        Action.WEST
    )

    assert newState.getAgent(1).position == (0, 0)
    assert newState.getAgent(2).position == (1, 0)

    print("PASS: swap blocked")

def test_push_box_into_agent():
    agents = [
        Agent(1, (0, 0)),
        Agent(2, (2, 0))
    ]

    boxes = [
        Box((1, 0))
    ]

    state, movement = createState(
        agents,
        boxes,
        [],
        set()
    )

    newState = movement.applyActions(
        state,
        Action.EAST,
        Action.STAY
    )

    assert newState.getAgent(1).position == (0, 0)
    assert newState.getAgent(2).position == (2, 0)
    assert newState.boxPosition((1, 0)) is not None

    print("PASS: box into agent blocked")

def test_box_owner():
    agents = [
        Agent(1, (0, 0)),
        Agent(2, (5, 5))
    ]

    boxes = [
        Box((1, 0))
    ]

    goals = [
        (2, 0)
    ]

    state, movement = createState(
        agents,
        boxes,
        goals,
        set()
    )

    newState = movement.applyActions(
        state,
        Action.EAST,
        Action.STAY
    )

    box = newState.boxPosition((2, 0))

    assert box is not None
    assert box.owner == 1

    assert newState.getScore(1) == 1
    assert newState.getScore(2) == 0

    print("PASS: box owner and score")

def test_state_copy():
    agents = [
        Agent(1, (0, 0)),
        Agent(2, (5, 5))
    ]

    state, movement = createState(
        agents,
        [],
        [],
        set()
    )

    newState = movement.applyActions(
        state,
        Action.EAST,
        Action.STAY
    )

    assert state.getAgent(1).position == (0, 0)
    assert newState.getAgent(1).position == (1, 0)

    assert state.stepCount == 0
    assert newState.stepCount == 1

    print("PASS: state copy")

def test_agent2_takes_box_and_gets_owner():
    agents = [
        Agent(1, (1, 1)),
        Agent(2, (2, 2))
    ]

    boxes = [
        Box((3, 2), owner=1)
    ]

    goals = [
        (3, 2)
    ]

    state, movement = createState(
        agents,
        boxes,
        goals,
        set()
    )
def test_box_on_goal_has_no_owner():
    goalPosition = (3, 2)

    agents = [
        Agent(1, (1, 1)),
        Agent(2, (5, 5))
    ]

    boxes = [
        Box(goalPosition)
    ]

    goals = [
        goalPosition
    ]

    state, movement = createState(
        agents,
        boxes,
        goals,
        set()
    )

    box = state.boxPosition(goalPosition)

    assert box is not None
    assert box.position == goalPosition
    assert box.owner is None

    assert state.isGoal(goalPosition)

    assert state.getScore(1) == 0
    assert state.getScore(2) == 0

    print("PASS: box on goal has no owner")

def test_agent2_takes_box_and_gets_owner():
    goalPosition = (3, 2)

    agents = [
        Agent(1, (1, 1)),
        Agent(2, (2, 2))
    ]

    boxes = [
        Box(goalPosition, owner=1)
    ]

    goals = [
        goalPosition
    ]

    state, movement = createState(
        agents,
        boxes,
        goals,
        set()
    )

    # =========================
    # BƯỚC 1:
    # Agent 2 đẩy box ra khỏi goal
    # =========================

    state = movement.applyActions(
        state,
        Action.STAY,
        Action.EAST
    )

    box = state.boxPosition((4, 2))

    assert box is not None
    assert box.owner is None

    assert state.getScore(1) == 0
    assert state.getScore(2) == 0

    # =========================
    # BƯỚC 2:
    # Agent 2 đi vòng sang bên phải box
    # =========================

    state = movement.applyActions(
        state,
        Action.STAY,
        Action.NORTH
    )

    state = movement.applyActions(
        state,
        Action.STAY,
        Action.EAST
    )

    state = movement.applyActions(
        state,
        Action.STAY,
        Action.EAST
    )

    state = movement.applyActions(
        state,
        Action.STAY,
        Action.SOUTH
    )

    # =========================
    # BƯỚC 3:
    # Agent 2 đẩy box trở lại goal
    # =========================

    state = movement.applyActions(
        state,
        Action.STAY,
        Action.WEST
    )

    box = state.boxPosition(goalPosition)

    assert box is not None
    assert box.owner == 2

    assert state.getScore(1) == 0
    assert state.getScore(2) == 1

    print("PASS: agent 2 takes box and gets owner")
if __name__ == "__main__":
    test_normal_move()
    test_stay()
    test_box_wall()
    test_same_target()
    test_swap_position()
    test_push_box_into_agent()
    test_box_owner()
    test_state_copy()
    test_box_on_goal_has_no_owner()
    test_agent2_takes_box_and_gets_owner()

    print()
    print("ALL TESTS PASSED")