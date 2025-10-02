"""Non-stationary k-armed bandit environment."""

from __future__ import annotations
from .stationary_bandit import Bandit


class NonStationaryBandit(Bandit):
    """Non-stationary k-armed Gaussian bandit with q* ~ N(0,1), reward ~ N(q*[a], sigma^2)."""

    def __init__(
        self,
        k: int = 10,
        reward_std: float = 1.0,
        walk_std: float = 0.01,
        seed: int | None = None,
    ):
        super().__init__(k=k, reward_std=reward_std, seed=seed)
        self.walk_std = walk_std

    def step(self, action: int) -> float:
        """Take an action and return the reward. Updates q* values via random walk."""
        # Get reward before updating q* values
        result = self.rng.normal(self.q_true[action], self.reward_std)
        # Random walk all q* values
        self.q_true += self.rng.normal(0.0, self.walk_std, size=self.k)
        return result
