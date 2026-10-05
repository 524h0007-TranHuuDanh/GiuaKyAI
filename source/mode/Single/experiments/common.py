from pathlib import Path

from ....shared.map_parser import parse_map
from ..core.problem import SokobanProblem


MAP_DIR = Path(__file__).resolve().parents[3] / "map" / "one_agent"
RESULT_DIR = Path(__file__).resolve().parent / "results"
REPEATS = 5


def list_maps():
    return sorted(MAP_DIR.glob("single_*.txt"))


def make_problem(path):
    state = parse_map(path)
    return SokobanProblem(state)