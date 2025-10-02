"""Single-run experiment runner and result container."""

from __future__ import annotations
from dataclasses import dataclass
import numpy as np
from ..agents.base_agent import BaseAgent


@dataclass
class RunResult:
    """Container for single experiment run results."""

    rewards: np.ndarray  # shape [T]
    optimal_flags: np.ndarray  # bool, shape [T]
    Q: np.ndarray  # final Q estimates
    N: np.ndarray  # final action counts

    @property
    def avg_reward(self) -> float:
        """Average reward over entire run."""
        return float(self.rewards.mean())

    @property
    def avg_reward_last200(self) -> float:
        """Average reward over last 200 steps."""
        tail = self.rewards[-200:] if len(self.rewards) >= 200 else self.rewards
        return float(tail.mean())

    @property
    def frac_optimal(self) -> float:
        """Fraction of optimal actions over entire run."""
        return float(self.optimal_flags.mean())

    @property
    def frac_optimal_last200(self) -> float:
        """Fraction of optimal actions over last 200 steps."""
        tail = (
            self.optimal_flags[-200:]
            if len(self.optimal_flags) >= 200
            else self.optimal_flags
        )
        return float(tail.mean())


class Experiment:
    """Single- and multi-run evaluation for a bandit + agent."""

    def __init__(self, bandit, agent: BaseAgent, steps: int = 1000):
        self.bandit = bandit
        self.agent = agent
        self.steps = steps

    def run(self, warm_start: bool = False) -> RunResult:
        """Run a single experiment."""
        rewards = []
        optimal_flags = []

        if warm_start:
            # Pull each arm once to avoid unlucky lock-in; does NOT count toward 'steps'.
            for a in range(self.agent.k):
                optimal_flags.append(self.bandit.optimal_action() == a)
                r = self.bandit.step(a)
                self.agent.update(a, r)
                rewards.append(r)

        # Main loop
        for t in range(self.steps):
            a = self.agent.select_action()
            optimal_flags.append(self.bandit.optimal_action() == a)
            r = self.bandit.step(a)
            rewards.append(r)
            self.agent.update(a, r)

        rewards = np.asarray(rewards, dtype=float)
        optimal_flags = np.asarray(optimal_flags, dtype=bool)

        # Agents may not have N (e.g., gradient bandit); fall back gracefully
        N = getattr(self.agent, "N", np.zeros(self.agent.k, dtype=int))
        Q = getattr(self.agent, "Q", np.zeros(self.agent.k, dtype=float))

        return RunResult(
            rewards=rewards, optimal_flags=optimal_flags, Q=Q.copy(), N=N.copy()
        )
