import csv

from .common import list_maps, make_problem, RESULT_DIR
from ....algorithms.ucs import UCS
from ....algorithms.astar import AStar
from ....algorithms.heuristic import heuristic


def check_consistent(problem, actions):
    state = problem.initial_state
    violations = 0

    for action in actions:
        next_state = problem.result(state, action)
        cost = problem.step_cost(state, action, next_state)

        if heuristic(state) > cost + heuristic(next_state):
            violations += 1

        state = next_state

    return violations


def verify_one(map_path):
    problem = make_problem(map_path)

    ucs = UCS().solve(problem)
    astar = AStar().solve(problem)

    if not ucs.solved or not astar.solved:
        return {
            "map": map_path.name,
            "ucs_cost": -1,
            "astar_cost": -1,
            "admissible": False,
            "violations": -1,
        }

    return {
        "map": map_path.name,
        "ucs_cost": ucs.total_cost,
        "astar_cost": astar.total_cost,
        "admissible": astar.total_cost == ucs.total_cost,
        "violations": check_consistent(problem, astar.actions),
    }


def main():
    RESULT_DIR.mkdir(parents=True, exist_ok=True)
    out_file = RESULT_DIR / "verify_heuristic.csv"

    rows = []

    for map_path in list_maps():
        print(f"Kiem tra: {map_path.name}")
        rows.append(verify_one(map_path))

    fields = ["map", "ucs_cost", "astar_cost", "admissible", "violations"]

    with out_file.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Da ghi: {out_file}")


if __name__ == "__main__":
    main()