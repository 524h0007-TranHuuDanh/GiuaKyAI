import sys
from pathlib import Path

HERE = Path(__file__).parent.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from core.map_parser import parse_map
from core.problem import SokobanProblem
from algorithms.heuristic import Heuristic
from algorithms.ucs import UCS


def compute_true_cost(state, problem):
    """Dùng UCS để tính cost thực từ state hiện tại đến goal."""
    sub_problem = SokobanProblem(state)
    r = UCS().solve(sub_problem)
    if r.solved:
        return r.total_cost
    return float('inf')


def verify_admissible(state, problem, h_func):
    """Kiểm tra h(state) <= h*(state) (cost thực)."""
    h_value = h_func(state)
    true_cost = compute_true_cost(state, problem)
    ok = h_value <= true_cost
    return ok, h_value, true_cost


def verify_consistent(state, problem, h_func):
    """Kiểm tra h(state) <= cost(state,next) + h(next) với mọi next."""
    violations = 0
    h_state = h_func(state)

    for action in problem.actions(state):
        next_state = problem.result(state, action)
        step_cost = problem.step_cost(state, action, next_state)
        h_next = h_func(next_state)

        if h_state > step_cost + h_next:
            violations += 1
            print(f"  VI PHAM: h={h_state}, step={step_cost}, h_next={h_next}")

    return violations == 0, violations


def main():
    map_path = 'maps/example_map.txt'
    state = parse_map(map_path)
    problem = SokobanProblem(state)

    h_func = Heuristic(state.goals, state.walls, state.width, state.height)

    print("=== VERIFY ADMISSIBLE ===")
    ok, h_val, h_star = verify_admissible(state, problem, h_func)
    print(f"  h(initial)  = {h_val}")
    print(f"  h*(initial) = {h_star}")
    print(f"  Admissible? {ok}")
    print()

    print("=== VERIFY CONSISTENT ===")
    ok2, violations = verify_consistent(state, problem, h_func)
    print(f"  Vi pham: {violations}")
    print(f"  Consistent? {ok2}")
    print()

    # Test them tren nhieu state
    print("=== TEST TREN NHIEU STATE (BFS mo rong) ===")
    from collections import deque

    queue = deque([state])
    visited = set([state])
    total = 0
    adm_ok = 0
    cons_ok = 0

    while queue and total < 50:
        s = queue.popleft()
        total += 1

        ok_a, _, _ = verify_admissible(s, problem, h_func)
        if ok_a:
            adm_ok += 1

        ok_c, _ = verify_consistent(s, problem, h_func)
        if ok_c:
            cons_ok += 1

        for action in problem.actions(s):
            ns = problem.result(s, action)
            if ns not in visited:
                visited.add(ns)
                queue.append(ns)

    print(f"  So state kiem tra: {total}")
    print(f"  Admissible OK    : {adm_ok}/{total}")
    print(f"  Consistent OK    : {cons_ok}/{total}")


if __name__ == "__main__":
    main()