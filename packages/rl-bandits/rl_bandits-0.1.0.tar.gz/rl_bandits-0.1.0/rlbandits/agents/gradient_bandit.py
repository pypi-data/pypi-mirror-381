"""Gradient bandit agent with preference-based updates."""

from __future__ import annotations
import numpy as np
from .base_agent import BaseAgent


class GradientBanditAgent(BaseAgent):
    """Gradient bandit with preference-based updates."""

    def __init__(self, k: int = 10, alpha: float = 0.1, seed: int | None = None):
        super().__init__(k=k, seed=seed)
        self.H = np.zeros(k, dtype=float)  # Preferences
        self.pi = np.ones(k, dtype=float) / k  # Action probabilities
        self.alpha = alpha
        self.avg_reward = 0.0
        self.time_step = 0

    def select_action(self) -> int:
        """Select action using softmax policy based on preferences."""
        exp_H = np.exp(self.H - np.max(self.H))  # for numerical stability
        self.pi = exp_H / exp_H.sum()
        return int(self.rng.choice(self.k, p=self.pi))

    def update(self, action: int, reward: float) -> None:
        """Update preferences using gradient ascent."""
        self.time_step += 1
        self.avg_reward += (
            reward - self.avg_reward
        ) / self.time_step  # Incremental average

        for a in range(self.k):
            if a == action:
                self.H[a] += self.alpha * (reward - self.avg_reward) * (1 - self.pi[a])
            else:
                self.H[a] -= self.alpha * (reward - self.avg_reward) * self.pi[a]

    def reset(self, seed: int | None = None) -> None:
        """Reset agent state."""
        super().reset(seed)
        self.H[:] = 0.0
        self.pi[:] = 1.0 / self.k
        self.avg_reward = 0.0
        self.time_step = 0
