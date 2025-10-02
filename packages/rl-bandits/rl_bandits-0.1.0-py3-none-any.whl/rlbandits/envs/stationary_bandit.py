"""Stationary k-armed bandit environment."""

from __future__ import annotations
import numpy as np


class Bandit:
    """Stationary k-armed Gaussian bandit with q* ~ N(0,1), reward ~ N(q*[a], sigma^2)."""

    def __init__(self, k: int = 10, reward_std: float = 1.0, seed: int | None = None):
        self.k = k
        self.reward_std = reward_std
        self.rng = np.random.default_rng(seed)
        self.q_true = self.rng.normal(0.0, 1.0, size=k)

    def step(self, action: int) -> float:
        """Take an action and return the reward."""
        return self.rng.normal(self.q_true[action], self.reward_std)

    def optimal_action(self) -> int:
        """Return the optimal action (highest true value)."""
        return int(np.argmax(self.q_true))
