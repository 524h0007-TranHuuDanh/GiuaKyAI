from pathlib import Path

from .sokoban_state import SokobanState
from .constants import WALL, AGENT, BOX, GOAL, BOX_ON_GOAL, EMPTY


def parse_map(filepath):
    path = Path(filepath)

    if not path.exists():
        raise FileNotFoundError(f"Khong tim thay file: {filepath}")

    with open(filepath, encoding="utf-8-sig") as file:
        lines = file.read().splitlines()

    if not lines:
        raise ValueError("File map rong")

    width = max(len(line) for line in lines)
    height = len(lines)
    row_lengths = tuple(len(line) for line in lines)

    walls = set()
    boxes = set()
    goals = set()

    agent1 = None
    agent2 = None

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            position = (x, y)

            if char == WALL:
                walls.add(position)

            elif char == AGENT:
                if agent1 is not None:
                    raise ValueError("Map co nhieu Agent 1")

                agent1 = position

            elif char == "1":
                if agent1 is not None:
                    raise ValueError("Map co nhieu Agent 1")

                agent1 = position

            elif char == "2":
                if agent2 is not None:
                    raise ValueError("Map co nhieu Agent 2")

                agent2 = position

            elif char == BOX:
                boxes.add(position)

            elif char == GOAL:
                goals.add(position)

            elif char == BOX_ON_GOAL:
                boxes.add(position)
                goals.add(position)

            elif char == EMPTY:
                pass

            else:
                raise ValueError(f"Ky tu khong hop le '{char}' tai ({x}, {y})")

    if agent1 is None:
        raise ValueError("Map khong co Agent 1")

    if len(boxes) != len(goals):
        raise ValueError("So box khong bang so goal")

    state = SokobanState(
        agent1,
        agent2,
        frozenset(boxes),
        frozenset(goals),
        frozenset(walls),
        width,
        height,
        row_lengths
    )

    return state