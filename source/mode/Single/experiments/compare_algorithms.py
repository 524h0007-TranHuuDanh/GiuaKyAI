import csv

from .common import list_maps, make_problem, RESULT_DIR, REPEATS, NODE_LIMIT
from .measure import make_factory, measure_time, measure_memory, run_once


def main():
    RESULT_DIR.mkdir(parents=True, exist_ok=True)
    out_file = RESULT_DIR / "compare_algorithms.csv"

    rows = []

    for map_path in list_maps():
        print(f"Dang chay: {map_path.name}")
        problem = make_problem(map_path)

        for algo in ["UCS", "A*"]:
            factory = make_factory(algo, node_limit=NODE_LIMIT)
            result = run_once(factory, problem)
            t = measure_time(factory, problem, REPEATS)
            mem = measure_memory(factory, problem)

            depth = len(result.actions)
            branching = result.nodes_expanded ** (1.0 / depth) if depth > 0 else 0
            nps = result.nodes_expanded / t if t > 0 else 0

            rows.append({
                "map": map_path.name,
                "algorithm": algo,
                "solved": result.solved,
                "cost": result.total_cost,
                "depth": depth,
                "nodes_expanded": result.nodes_expanded,
                "max_frontier": result.max_frontier,
                "time_sec": round(t, 4),
                "peak_memory_kb": round(mem, 2),
                "branching": round(branching, 3),
                "nodes_per_sec": round(nps, 1),
            })

    fields = ["map", "algorithm", "solved", "cost", "depth", "nodes_expanded",
              "max_frontier", "time_sec", "peak_memory_kb", "branching", "nodes_per_sec"]

    with out_file.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Da ghi: {out_file}")


if __name__ == "__main__":
    main()