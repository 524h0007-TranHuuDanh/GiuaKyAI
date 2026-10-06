import csv
import matplotlib.pyplot as plt

from .common import RESULT_DIR


def read_csv(path):
    rows = []
    with open(path, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            rows.append(row)
    return rows


def plot_combined(rows, out_path):
    metrics = [
        ("time_sec", "Time"),
        ("nodes_expanded", "Nodes Expanded"),
        ("max_frontier", "Max Frontier"),
        ("memory_kb", "Memory")
    ]

    ucs_values = []
    astar_values = []

    for metric, _ in metrics:
        ucs = [float(r[metric]) for r in rows if r["algorithm"] == "UCS"]
        astar = [float(r[metric]) for r in rows if r["algorithm"] == "A*"]

        ucs_avg = sum(ucs) / len(ucs)
        astar_avg = sum(astar) / len(astar)

        ucs_values.append(100)
        astar_values.append((astar_avg / ucs_avg) * 100)

    labels = [label for _, label in metrics]

    x = range(len(labels))
    width = 0.35

    plt.figure(figsize=(10, 5.5))

    bars_ucs = plt.bar([i - width / 2 for i in x], ucs_values, width, label="UCS")
    bars_astar = plt.bar([i + width / 2 for i in x], astar_values, width, label="A*")

    plt.xticks(list(x), labels)
    plt.ylabel("Relative Performance (%)")
    plt.title("Performance Comparison: UCS vs A*")
    plt.axhline(y=100, linestyle="--", linewidth=1, alpha=0.5)
    plt.legend()

    for bars in [bars_ucs, bars_astar]:
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2, height + 2, f"{height:.0f}%", ha="center", va="bottom", fontsize=9)

    plt.tight_layout()
    plt.savefig(out_path, dpi=300)
    plt.close()

    print(f"Da ve: {out_path}")


def main():
    rows = read_csv(RESULT_DIR / "compare_algorithms.csv")
    plot_combined(rows, RESULT_DIR / "performance_comparison.png")


if __name__ == "__main__":
    main()