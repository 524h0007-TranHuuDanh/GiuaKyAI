import csv

from .common import list_maps, make_problem, RESULT_DIR
from .state_graph import build_state_graph, true_costs
from ....algorithms.heuristic import Heuristic


LIMIT = 50000


def make_alt_heuristic(base, mode):
    if mode == "zero":
        return lambda s: 0

    if mode == "double":
        def h(s):
            v = base(s)
            return float("inf") if v == float("inf") else 2 * v
        return h

    if mode == "plus3":
        def h(s):
            v = base(s)
            return float("inf") if v == float("inf") else v + 3
        return h

    return base


def verify_one(map_path, h_func):
    problem = make_problem(map_path)
    init = problem.initial_state

    states, edges, partial, key_to_id = build_state_graph(problem, LIMIT)
    h_star = true_costs(states, edges, problem)

    adm_viol = 0
    con_viol = 0
    goal_viol = 0
    inf_states = 0
    inf_correct = 0

    for i, s in enumerate(states):
        hv = h_func(s)
        hsv = h_star[i]

        if hv == float("inf"):
            inf_states += 1
            if hsv == float("inf"):
                inf_correct += 1

        if hsv != float("inf") and hv > hsv:
            adm_viol += 1

        if problem.goal_test(s) and hv != 0:
            goal_viol += 1

    for u, v in edges:
        hu = h_func(states[u])
        hv = h_func(states[v])
        if hu != float("inf") and hu > 1 + hv:
            con_viol += 1

    h0 = h_func(init)
    hs0 = h_star[key_to_id[init.key()]]

    if hs0 in (0, float("inf")):
        ratio = None
    else:
        ratio = round(h0 / hs0, 3)

    return {
        "states": len(states),
        "edges": len(edges),
        "partial": partial,
        "admissible_violations": adm_viol,
        "consistent_violations": con_viol,
        "goal_violations": goal_viol,
        "inf_states": inf_states,
        "inf_correct": inf_correct,
        "h0_over_hstar0": ratio,
    }


def main():
    RESULT_DIR.mkdir(parents=True, exist_ok=True)
    out_file = RESULT_DIR / "verify_heuristic.csv"

    rows = []

    for map_path in list_maps():
        print(f"Kiem tra: {map_path.name}")
        problem = make_problem(map_path)
        init = problem.initial_state

        base = Heuristic(init.goals, init.walls, init.width, init.height)

        for mode in ["push_dist", "zero", "double", "plus3"]:
            h_func = make_alt_heuristic(base, mode)
            stats = verify_one(map_path, h_func)
            stats["map"] = map_path.name
            stats["heuristic"] = mode
            rows.append(stats)

    fields = ["map", "heuristic", "states", "edges", "partial",
              "admissible_violations", "consistent_violations", "goal_violations",
              "inf_states", "inf_correct", "h0_over_hstar0"]

    with out_file.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for r in rows:
            writer.writerow({k: r.get(k) for k in fields})

    print(f"Da ghi: {out_file}")


if __name__ == "__main__":
    main()