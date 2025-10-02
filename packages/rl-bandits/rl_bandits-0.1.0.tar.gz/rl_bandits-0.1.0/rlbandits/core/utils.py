"""Utility functions for seeding, logging, and plotting."""

from __future__ import annotations
from typing import Dict, List, Optional, Tuple, Union
import numpy as np


def set_global_seed(seed: int) -> None:
    """Set global random seed for reproducibility."""
    np.random.seed(seed)


def plot_curves(
    curves: Union[Dict[str, np.ndarray], List[Dict[str, np.ndarray]]],
    title: str = "Bandit Performance",
    labels: Optional[List[str]] = None,
    save_path: Optional[str] = None,
    figsize: Tuple[int, int] = (12, 6),
    show: bool = True,
) -> None:
    """
    Enhanced plotting utility for bandit performance curves.

    Args:
        curves: Single curve dict or list of curve dicts with 'avg_reward' and 'avg_optimal' keys
        title: Title for the plot
        labels: Labels for multiple curves (if curves is a list)
        save_path: Path to save the plot (optional)
        figsize: Figure size tuple
        show: Whether to display the plot
    """
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib not available for plotting")
        return

    # Handle single curve vs multiple curves
    if isinstance(curves, dict):
        curves_list = [curves]
        labels = labels or [""]
    else:
        curves_list = curves
        labels = labels or [f"Agent {i+1}" for i in range(len(curves_list))]

    plt.figure(figsize=figsize)

    # Plot average reward
    plt.subplot(1, 2, 1)
    plt.title("Average Reward")
    for i, curve in enumerate(curves_list):
        plt.plot(curve["avg_reward"], label=labels[i], linewidth=2)
    plt.xlabel("Steps")
    plt.ylabel("Average Reward")
    plt.grid(True, alpha=0.3)
    if len(curves_list) > 1:
        plt.legend()

    # Plot fraction optimal
    plt.subplot(1, 2, 2)
    plt.title("Fraction Optimal Action")
    for i, curve in enumerate(curves_list):
        plt.plot(curve["avg_optimal"], label=labels[i], linewidth=2)
    plt.xlabel("Steps")
    plt.ylabel("Fraction Optimal Action")
    plt.grid(True, alpha=0.3)
    if len(curves_list) > 1:
        plt.legend()

    plt.suptitle(title, fontsize=14, fontweight="bold")
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
        print(f"Plot saved to {save_path}")

    if show:
        plt.show()


def plot_comparison(
    results: Dict[str, Dict[str, np.ndarray]],
    title: str = "Agent Comparison",
    save_path: Optional[str] = None,
    figsize: Tuple[int, int] = (15, 6),
) -> None:
    """
    Plot comparison of multiple agents.

    Args:
        results: Dictionary mapping agent names to their curve results
        title: Title for the plot
        save_path: Path to save the plot (optional)
        figsize: Figure size tuple
    """
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib not available for plotting")
        return

    plt.figure(figsize=figsize)

    # Plot average reward comparison
    plt.subplot(1, 2, 1)
    plt.title("Average Reward Comparison")
    for agent_name, curves in results.items():
        plt.plot(curves["avg_reward"], label=agent_name, linewidth=2)
    plt.xlabel("Steps")
    plt.ylabel("Average Reward")
    plt.grid(True, alpha=0.3)
    plt.legend()

    # Plot fraction optimal comparison
    plt.subplot(1, 2, 2)
    plt.title("Fraction Optimal Action Comparison")
    for agent_name, curves in results.items():
        plt.plot(curves["avg_optimal"], label=agent_name, linewidth=2)
    plt.xlabel("Steps")
    plt.ylabel("Fraction Optimal Action")
    plt.grid(True, alpha=0.3)
    plt.legend()

    plt.suptitle(title, fontsize=14, fontweight="bold")
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
        print(f"Comparison plot saved to {save_path}")

    plt.show()


def plot_parameter_study(
    results: Dict[str, Dict[str, np.ndarray]],
    parameter_name: str,
    title: Optional[str] = None,
    save_path: Optional[str] = None,
) -> None:
    """
    Plot results for parameter studies (e.g., different epsilon values).

    Args:
        results: Dictionary mapping parameter values to their curve results
        parameter_name: Name of the parameter being studied
        title: Title for the plot
        save_path: Path to save the plot (optional)
    """
    if title is None:
        title = f"{parameter_name} Parameter Study"

    plot_comparison(results, title=title, save_path=save_path)


def print_summary(curves: Dict[str, np.ndarray], agent_name: str) -> None:
    """Print summary statistics for experiment results."""
    avg_reward_last200 = curves["avg_reward"][-200:].mean()
    frac_optimal_last200 = curves["avg_optimal"][-200:].mean()

    print(f"{agent_name} multi-run avg reward last200: {avg_reward_last200:.4f}")
    print(f"{agent_name} multi-run frac optimal last200: {frac_optimal_last200:.4f}")
