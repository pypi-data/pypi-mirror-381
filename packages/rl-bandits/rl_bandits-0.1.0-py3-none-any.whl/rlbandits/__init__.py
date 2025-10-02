"""RL Bandits: A modular library for multi-armed bandit algorithms."""

from .envs import Bandit, NonStationaryBandit
from .agents import (
    BaseAgent,
    GreedyAgent,
    EpsilonGreedyAgent,
    UCBAgent,
    GradientBanditAgent,
)
from .core import (
    Experiment,
    RunResult,
    run_multi_experiment,
    plot_curves,
    plot_comparison,
    plot_parameter_study,
    set_global_seed,
    print_summary,
)

__version__ = "0.1.0"
__author__ = "Meeran Malik"

__all__ = [
    # Environments
    "Bandit",
    "NonStationaryBandit",
    # Agents
    "BaseAgent",
    "GreedyAgent",
    "EpsilonGreedyAgent",
    "UCBAgent",
    "GradientBanditAgent",
    # Core
    "Experiment",
    "RunResult",
    "run_multi_experiment",
    "plot_curves",
    "plot_comparison",
    "plot_parameter_study",
    "set_global_seed",
    "print_summary",
]
