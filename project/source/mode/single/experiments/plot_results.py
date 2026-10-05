import csv

import matplotlib.pyplot as plt

from .common import RESULT_DIR


def read_csv(path):
    rows = []
    with open(path, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            rows.append(row)
    return rows


def plot(rows, metric, ylabel, title, out_path):
    maps = sorted(set(r["map"] for r in rows))
    ucs_values = []
    astar_values = []

    for m in maps:
        ucs_values.append(float(next(r[metric] for r in rows
                                     if r["map"] == m and r["algorithm"] == "UCS")))
        astar_values.append(float(next(r[metric] for r in rows
                                       if r["map"] == m and r["algorithm"] == "A*")))

    x = range(len(maps))
    width = 0.35

    plt.figure(figsize=(10, 5))
    plt.bar([i - width / 2 for i in x], ucs_values, width, label="UCS")
    plt.bar([i + width / 2 for i in x], astar_values, width, label="A*")
    plt.xticks(list(x), maps, rotation=15)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()
    print(f"Da ve: {out_path}")


def main():
    rows = read_csv(RESULT_DIR / "compare_algorithms.csv")

    plot(rows, "time_sec", "Time (s)", "Time UCS vs A*", RESULT_DIR / "time.png")
    plot(rows, "nodes_expanded", "Nodes", "Nodes UCS vs A*", RESULT_DIR / "nodes.png")
    plot(rows, "max_frontier", "Frontier", "Max frontier UCS vs A*", RESULT_DIR / "frontier.png")
    plot(rows, "memory_kb", "Memory (KB)", "Memory UCS vs A*", RESULT_DIR / "memory.png")


if __name__ == "__main__":
    main()