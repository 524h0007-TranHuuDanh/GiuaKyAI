import gc
import time
import tracemalloc

from ....algorithms.UCS import UCS
from ....algorithms.astar import AStar


def make_factory(algorithm):
    def factory():
        if algorithm == "UCS":
            return UCS()
        return AStar()
    return factory


def measure_time(factory, problem, repeats):
    times = []
    for _ in range(repeats):
        gc.collect()
        solver = factory()
        t0 = time.perf_counter()
        solver.solve(problem)
        t1 = time.perf_counter()
        times.append(t1 - t0)
    return sum(times) / len(times)


def measure_memory(factory, problem):
    gc.collect()
    tracemalloc.start()
    try:
        solver = factory()
        solver.solve(problem)
        _, peak = tracemalloc.get_traced_memory()
    finally:
        tracemalloc.stop()
    return peak / 1024


def run_once(factory, problem):
    solver = factory()
    return solver.solve(problem)