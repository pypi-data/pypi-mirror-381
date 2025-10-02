"""Upper Confidence Bound (UCB) bandit agent."""

from __future__ import annotations
import numpy as np
from .base_agent import BaseAgent


class UCBAgent(BaseAgent):
    """Upper Confidence Bound (UCB) action selection with sample-average updates."""

    def __init__(self, k: int = 10, c: float = 2.0, seed: int | None = None):
        super().__init__(k=k, seed=seed)
        self.Q = np.zeros(k, dtype=float)
        self.N = np.zeros(k, dtype=int)
        self.c = c
        self.total_steps = 0

    def select_action(self) -> int:
        """Select action using UCB policy."""
        # Check for unvisited actions first
        for a in range(self.k):
            if self.N[a] == 0:
                return a  # Explore unvisited actions first

        self.total_steps += 1
        ucb_values = np.zeros(self.k, dtype=float)

        for a in range(self.k):
            ucb_values[a] = self.Q[a] + self.c * np.sqrt(
                np.log(self.total_steps) / self.N[a]
            )

        max_ucb = np.max(ucb_values)
        candidates = np.where(ucb_values == max_ucb)[0]
        return int(self.rng.choice(candidates))

    def update(self, action: int, reward: float) -> None:
        """Update Q-value using sample average."""
        n = self.N[action]
        self.Q[action] += 1.0 / (n + 1) * (reward - self.Q[action])
        self.N[action] += 1

    def reset(self, seed: int | None = None) -> None:
        """Reset agent state."""
        super().reset(seed)
        self.Q[:] = 0.0
        self.N[:] = 0
        self.total_steps = 0
