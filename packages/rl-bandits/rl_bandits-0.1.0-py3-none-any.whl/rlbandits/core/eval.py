"""Multi-run evaluation and aggregation."""

from __future__ import annotations
from typing import Type, Dict, Any
import numpy as np
from .runner import Experiment
from ..agents.base_agent import BaseAgent


def run_multi_experiment(
    bandit_class: Type,
    bandit_kwargs: Dict[str, Any],
    agent: BaseAgent,
    steps: int = 1000,
    runs: int = 200,
    warm_start: bool = True,
) -> Dict[str, np.ndarray]:
    """
    Run multiple experiments and return averaged curves.

    Args:
        bandit_class: Class of bandit environment to use
        bandit_kwargs: Keyword arguments for bandit constructor
        agent: Agent instance to use (will be reset for each run)
        steps: Number of steps per run
        runs: Number of runs to average over
        warm_start: Whether to do warm start (pull each arm once)

    Returns:
        Dictionary with 'avg_reward' and 'avg_optimal' curves
    """
    # Calculate total length including warm start
    total_length = steps + (agent.k if warm_start else 0)
    avg_reward = np.zeros(total_length, dtype=float)
    avg_opt = np.zeros_like(avg_reward, dtype=float)

    for i in range(runs):
        # Fresh env & agent per run (vary env seed; keep/record agent seed as you wish)
        bandit = bandit_class(seed=i, **bandit_kwargs)
        agent.reset(seed=i)  # or keep fixed seed; just be consistent

        exp = Experiment(bandit, agent, steps=steps)
        result = exp.run(warm_start=warm_start)

        avg_reward += result.rewards
        avg_opt += result.optimal_flags.astype(float)

    avg_reward /= runs
    avg_opt /= runs

    return {"avg_reward": avg_reward, "avg_optimal": avg_opt}
