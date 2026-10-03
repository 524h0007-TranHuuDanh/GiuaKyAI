from dataclasses import dataclass, field
from abc import ABC, abstractmethod
@dataclass
class SearchResult:
    actions: list = field(default_factory = list)
    total_cost: int = 0
    nodes_expanded: int = 0
    time: float = 0.0
    max_frontier: int = 0
    memory: float = 0.0
    solved: bool = False


class SearchAlgorithm(ABC):
    @abstractmethod
    def solve(self, problem):
        pass