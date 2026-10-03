
from dataclasses import dataclass

@dataclass(frozen=True)
class  SokobanState:
    agent: tuple
    boxes: frozenset
    goals: frozenset
    walls: frozenset
    width: int
    height: int
    row_lengths: tuple

    def is_goal(self):
        return self.boxes == self.goals