import csv

from .common import MAP_DIR, make_problem, RESULT_DIR, REPEATS
from .measure import make_factory, measure_time, measure_memory, run_once


def main():
    RESULT_DIR.mkdir(parents=True, exist_ok=True)
    out_file = RESULT_DIR / "compare_algorithms.csv"

    map_path = MAP_DIR / "example_map.txt"
    problem = make_problem(map_path)

    rows = []

    print(f"Dang chay: {map_path.name}")

    # so sánh UCS và A*
    for algo in ["UCS", "A*"]:
        factory = make_factory(algo)
        result = run_once(factory, problem)
        t = measure_time(factory, problem, REPEATS)
        mem = measure_memory(factory, problem)

        rows.append({
            "map": map_path.name,
            "algorithm": algo,
            "solved": result.solved,
            "cost": result.total_cost,
            "depth": len(result.actions),
            "nodes_expanded": result.nodes_expanded,
            "max_frontier": result.max_frontier,
            "time_sec": round(t, 4),
            "memory_kb": round(mem, 2),
        })

    fields = ["map", "algorithm", "solved", "cost", "depth",
              "nodes_expanded", "max_frontier", "time_sec", "memory_kb"]

    with out_file.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Da ghi: {out_file}")


if __name__ == "__main__":
    main()