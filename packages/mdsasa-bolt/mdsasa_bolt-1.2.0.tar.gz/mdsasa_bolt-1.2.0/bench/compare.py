# Copyright (C) 2025 Maxwell J. Campbell
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr


def load_results(filename: str) -> np.ndarray:
    """Load SASA results from a text file."""
    with Path.open(Path("bench") / Path(filename)) as f:
        results = [float(line.strip()) for line in f]
    return np.array(results)


def main() -> None:
    """Compare SASA results from old and new implementations."""
    # Load results from both implementations
    old_results = load_results("old_sasa_results.txt")
    new_results = load_results("new_sasa_results.txt")

    # Calculate Pearson correlation
    correlation, p_value = pearsonr(old_results, new_results)

    # Create scatter plot
    plt.figure(figsize=(8, 8))
    plt.scatter(old_results, new_results, alpha=0.6, s=20)

    # Get current axis limits after scatter plot
    xlim = plt.xlim()
    ylim = plt.ylim()

    # Add perfect correlation line spanning the full diagonal
    line_min = min(xlim[0], ylim[0])
    line_max = max(xlim[1], ylim[1])
    plt.plot([line_min, line_max], [line_min, line_max], "r--", alpha=0.8, label="Perfect correlation")

    # Add labels and title
    plt.xlabel("Old SASA Implementation")
    plt.ylabel("New SASA Implementation")
    plt.title(f"SASA Results Comparison\nPearson r = {correlation:.6f}, p = {p_value:.2e}")
    plt.legend()

    # Add grid
    plt.grid(True, alpha=0.3)

    # Add some statistics as text
    mean_diff = np.mean(new_results - old_results)
    rmse = np.sqrt(np.mean((new_results - old_results) ** 2))

    stats_text = f"Mean difference: {mean_diff:.3f} Ų\nRMSE: {rmse:.3f} Ų\nN points: {len(old_results)}"
    plt.text(
        0.05,
        0.95,
        stats_text,
        transform=plt.gca().transAxes,
        verticalalignment="top",
        bbox={"boxstyle": "round", "facecolor": "wheat", "alpha": 0.8},
    )

    plt.tight_layout()
    plt.savefig("bench/sasa_comparison.png", dpi=300, bbox_inches="tight")
    plt.show()

    # Print summary statistics


if __name__ == "__main__":
    main()
