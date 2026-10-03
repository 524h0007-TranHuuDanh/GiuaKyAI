import sys
import csv
from pathlib import Path

HERE = Path(__file__).parent.parent       # task1_sokoban_single/
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))      # source/

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from core.map_parser import parse_map
from core.problem import SokobanProblem
from algorithms.ucs import UCS
from algorithms.astar import AStar


MAPS = [
    'maps/example_map.txt',
    'maps/test_maps/map_easy.txt',
    'maps/test_maps/map_medium.txt',
]

RESULT_DIR = Path(__file__).parent / 'results'
RESULT_DIR.mkdir(exist_ok=True)


def run_one(map_path):
    state = parse_map(map_path)
    problem = SokobanProblem(state)

    ucs = UCS()
    r_ucs = ucs.solve(problem)

    astar = AStar()
    r_astar = astar.solve(problem)

    return {
        'map': Path(map_path).name,
        'ucs_cost': r_ucs.total_cost,
        'ucs_nodes': r_ucs.nodes_expanded,
        'ucs_time': r_ucs.time,
        'ucs_mem': r_ucs.memory,
        'ucs_frontier': r_ucs.max_frontier,
        'astar_cost': r_astar.total_cost,
        'astar_nodes': r_astar.nodes_expanded,
        'astar_time': r_astar.time,
        'astar_mem': r_astar.memory,
        'astar_frontier': r_astar.max_frontier,
        'same_cost': r_ucs.total_cost == r_astar.total_cost,
    }


def main():
    rows = []

    for map_path in MAPS:
        print(f"Running {map_path} ...")
        try:
            row = run_one(map_path)
            rows.append(row)
            print(f"  UCS  : cost={row['ucs_cost']}, nodes={row['ucs_nodes']}, time={row['ucs_time']:.4f}s")
            print(f"  A*   : cost={row['astar_cost']}, nodes={row['astar_nodes']}, time={row['astar_time']:.4f}s")
            print(f"  Same cost? {row['same_cost']}")
        except Exception as e:
            print(f"  Loi: {e}")

    # Ghi CSV
    if rows:
        csv_path = RESULT_DIR / 'compare_results.csv'
        keys = rows[0].keys()
        with open(csv_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            for r in rows:
                writer.writerow(r)
        print(f"\nDa ghi CSV: {csv_path}")

    # In bang tom tat
    print("\n=== TOM TAT ===")
    print(f"{'Map':<20} {'UCS nodes':>10} {'A* nodes':>10} {'UCS time':>10} {'A* time':>10}")
    for r in rows:
        print(f"{r['map']:<20} {r['ucs_nodes']:>10} {r['astar_nodes']:>10} "
              f"{r['ucs_time']:>10.4f} {r['astar_time']:>10.4f}")


if __name__ == "__main__":
    main()