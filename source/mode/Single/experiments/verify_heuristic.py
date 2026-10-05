import csv
from collections import deque

from .common import list_maps, make_problem, RESULT_DIR
from ....algorithms.ucs import UCS
from ....algorithms.heuristic import heuristic


def get_reachable_states(problem, limit=150):
    """Lấy một số state reachable bằng BFS (đơn giản)."""
    start = problem.initial_state
    visited = {start.key(): start}
    queue = deque([start])

    while queue and len(visited) < limit:
        s = queue.popleft()
        for a in problem.actions(s):
            s2 = problem.result(s, a)
            k = s2.key()
            if k not in visited:
                visited[k] = s2
                queue.append(s2)

    return list(visited.values())


def verify_one(map_path):
    problem = make_problem(map_path)
    states = get_reachable_states(problem, limit=150)

    adm_ok = 0
    adm_fail = 0
    cons_ok = 0
    cons_fail = 0

    for s in states:
        # Admissibility ucs từ state s để lấy cost tối ưu h*(s)
        sub = type(problem)(s)
        res = UCS().solve(sub)

        if not res.solved:
            continue          

        h_star = res.total_cost
        h = heuristic(s)

        if h <= h_star:
            adm_ok += 1
        else:
            adm_fail += 1

        # kt ConsistencyVới mọi action hợp lệ: h(s) <= 1 + h(s')
        for a in problem.actions(s):
            s2 = problem.result(s, a)
            if heuristic(s) <= 1 + heuristic(s2):
                cons_ok += 1
            else:
                cons_fail += 1

    return {
        "map": map_path.name,
        "states_checked": adm_ok + adm_fail,
        "admissible_ok": adm_ok,
        "admissible_fail": adm_fail,
        "consistent_ok": cons_ok,
        "consistent_fail": cons_fail,
    }


def main():
    RESULT_DIR.mkdir(parents=True, exist_ok=True)
    out = RESULT_DIR / "verify_heuristic.csv"

    rows = []
    for m in list_maps():
        print("Kiem tra:", m.name)
        rows.append(verify_one(m))

    fields = [
        "map",
        "states_checked",
        "admissible_ok",
        "admissible_fail",
        "consistent_ok",
        "consistent_fail",
    ]

    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    print("Da ghi:", out)


if __name__ == "__main__":
    main()