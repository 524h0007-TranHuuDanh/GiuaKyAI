from pathlib import Path
from core.state import SokobanState
from shared.constants import WALL, AGENT, BOX, GOAL, BOX_ON_GOAL, EMPTY


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
    agent = None

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == WALL:
                walls.add((x, y))
            elif char == AGENT:
                if agent is not None:
                    raise ValueError(f"Nhieu agent 'A' tai ({x}, {y})")
                agent = (x, y)
            elif char == BOX:
                boxes.add((x, y))
            elif char == GOAL:
                goals.add((x, y))
            elif char == BOX_ON_GOAL:
                boxes.add((x, y))
                goals.add((x, y))
            elif char == EMPTY:
                pass
            else:
                raise ValueError(f"Ky tu khong hop le '{char}' tai ({x}, {y})")

    if agent is None:
        raise ValueError("Map khong co agent 'A'")

    if len(boxes) != len(goals):
        raise ValueError("So box khong bang so goal")

    return SokobanState(
        agent=agent,
        boxes=frozenset(boxes),
        goals=frozenset(goals),
        walls=frozenset(walls),
        width=width,
        height=height,
        row_lengths=row_lengths,   
    )