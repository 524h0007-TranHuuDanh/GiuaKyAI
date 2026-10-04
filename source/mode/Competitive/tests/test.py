from source.shared.action import Action
from source.shared.agent import Agent
from source.shared.box import Box
from source.mode.competitive.core.competitive_state import CompetitiveState
from source.shared.rules import Rules
from source.shared.movement import Movement

def create_state(agents, boxes, goals, walls):
    state = CompetitiveState(
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

    state, movement = create_state(
        agents,
        boxes,
        goals,
        walls
    )

    new_state = movement.apply_actions(
        state,
        Action.EAST,
        Action.STAY
    )

    assert new_state.get_agent(1).position == (1, 0)
    assert new_state.get_agent(2).position == (5, 5)

    print("PASS: normal move")

def test_stay():
    agents = [
        Agent(1, (0, 0)),
        Agent(2, (5, 5))
    ]

    state, movement = create_state(
        agents,
        [],
        [],
        set()
    )

    new_state = movement.apply_actions(
        state,
        Action.STAY,
        Action.STAY
    )

    assert new_state.get_agent(1).position == (0, 0)
    assert new_state.get_agent(2).position == (5, 5)

    assert new_state.step_count == 1

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

    state, movement = create_state(
        agents,
        boxes,
        [],
        walls
    )

    new_state = movement.apply_actions(
        state,
        Action.EAST,
        Action.STAY
    )

    assert new_state.get_agent(1).position == (0, 0)
    assert new_state.box_position((1, 0)) is not None

    print("PASS: box blocked by wall")

def test_same_target():
    agents = [
        Agent(1, (0, 0)),
        Agent(2, (2, 0))
    ]

    state, movement = create_state(
        agents,
        [],
        [],
        set()
    )

    new_state = movement.apply_actions(
        state,
        Action.EAST,
        Action.WEST
    )

    assert new_state.get_agent(1).position == (0, 0)
    assert new_state.get_agent(2).position == (2, 0)

    print("PASS: same target")

def test_swap_position():
    agents = [
        Agent(1, (0, 0)),
        Agent(2, (1, 0))
    ]

    state, movement = create_state(
        agents,
        [],
        [],
        set()
    )

    new_state = movement.apply_actions(
        state,
        Action.EAST,
        Action.WEST
    )

    assert new_state.get_agent(1).position == (0, 0)
    assert new_state.get_agent(2).position == (1, 0)

    print("PASS: swap blocked")

def test_push_box_into_agent():
    agents = [
        Agent(1, (0, 0)),
        Agent(2, (2, 0))
    ]

    boxes = [
        Box((1, 0))
    ]

    state, movement = create_state(
        agents,
        boxes,
        [],
        set()
    )

    new_state = movement.apply_actions(
        state,
        Action.EAST,
        Action.STAY
    )

    assert new_state.get_agent(1).position == (0, 0)
    assert new_state.get_agent(2).position == (2, 0)
    assert new_state.box_position((1, 0)) is not None

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

    state, movement = create_state(
        agents,
        boxes,
        goals,
        set()
    )

    new_state = movement.apply_actions(
        state,
        Action.EAST,
        Action.STAY
    )

    box = new_state.box_position((2, 0))

    assert box is not None
    assert box.owner == 1

    assert new_state.get_score(1) == 1
    assert new_state.get_score(2) == 0

    print("PASS: box owner and score")

def test_state_copy():
    agents = [
        Agent(1, (0, 0)),
        Agent(2, (5, 5))
    ]

    state, movement = create_state(
        agents,
        [],
        [],
        set()
    )

    new_state = movement.apply_actions(
        state,
        Action.EAST,
        Action.STAY
    )

    assert state.get_agent(1).position == (0, 0)
    assert new_state.get_agent(1).position == (1, 0)

    assert state.step_count == 0
    assert new_state.step_count == 1

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

    state, movement = create_state(
        agents,
        boxes,
        goals,
        set()
    )
def test_box_on_goal_has_no_owner():
    goal_position = (3, 2)

    agents = [
        Agent(1, (1, 1)),
        Agent(2, (5, 5))
    ]

    boxes = [
        Box(goal_position)
    ]

    goals = [
        goal_position
    ]

    state, movement = create_state(
        agents,
        boxes,
        goals,
        set()
    )

    box = state.box_position(goal_position)

    assert box is not None
    assert box.position == goal_position
    assert box.owner is None

    assert state.is_goal(goal_position)

    assert state.get_score(1) == 0
    assert state.get_score(2) == 0

    print("PASS: box on goal has no owner")

def test_agent2_takes_box_and_gets_owner():
    goal_position = (3, 2)

    agents = [
        Agent(1, (1, 1)),
        Agent(2, (2, 2))
    ]

    boxes = [
        Box(goal_position, owner=1)
    ]

    goals = [
        goal_position
    ]

    state, movement = create_state(
        agents,
        boxes,
        goals,
        set()
    )

    # =========================
    # BƯỚC 1:
    # Agent 2 đẩy box ra khỏi goal
    # =========================

    state = movement.apply_actions(
        state,
        Action.STAY,
        Action.EAST
    )

    box = state.box_position((4, 2))

    assert box is not None
    assert box.owner is None

    assert state.get_score(1) == 0
    assert state.get_score(2) == 0

    # =========================
    # BƯỚC 2:
    # Agent 2 đi vòng sang bên phải box
    # =========================

    state = movement.apply_actions(
        state,
        Action.STAY,
        Action.NORTH
    )

    state = movement.apply_actions(
        state,
        Action.STAY,
        Action.EAST
    )

    state = movement.apply_actions(
        state,
        Action.STAY,
        Action.EAST
    )

    state = movement.apply_actions(
        state,
        Action.STAY,
        Action.SOUTH
    )

    # =========================
    # BƯỚC 3:
    # Agent 2 đẩy box trở lại goal
    # =========================

    state = movement.apply_actions(
        state,
        Action.STAY,
        Action.WEST
    )

    box = state.box_position(goal_position)

    assert box is not None
    assert box.owner == 2

    assert state.get_score(1) == 0
    assert state.get_score(2) == 1

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