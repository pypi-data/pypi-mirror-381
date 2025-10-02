"""Greedy and epsilon-greedy bandit agents."""

from __future__ import annotations
import numpy as np
from .base_agent import BaseAgent


class GreedyAgent(BaseAgent):
    """Pure greedy with sample-average updates (α_n = 1/n) or constant step-size."""

    def __init__(
        self, k: int = 10, seed: int | None = None, alpha: float | None = None
    ):
        super().__init__(k=k, seed=seed)
        self.Q = np.zeros(k, dtype=float)
        self.N = np.zeros(k, dtype=int)
        self.alpha = alpha

    def select_action(self) -> int:
        """Select action greedily (ties broken randomly)."""
        max_q = np.max(self.Q)
        candidates = np.where(self.Q == max_q)[0]
        return int(self.rng.choice(candidates))

    def update(self, action: int, reward: float) -> None:
        """Update Q-value using sample average or constant step-size."""
        n = self.N[action]
        if self.alpha is None:
            # Sample average update
            self.Q[action] += 1.0 / (n + 1) * (reward - self.Q[action])
        else:
            # Constant step-size update
            self.Q[action] += self.alpha * (reward - self.Q[action])
        self.N[action] += 1

    def reset(self, seed: int | None = None) -> None:
        """Reset agent state."""
        super().reset(seed)
        self.Q[:] = 0.0
        self.N[:] = 0


class EpsilonGreedyAgent(GreedyAgent):
    """ε-greedy action selection with sample-average or constant step-size updates."""

    def __init__(
        self,
        k: int = 10,
        epsilon: float = 0.1,
        seed: int | None = None,
        alpha: float | None = None,
    ):
        super().__init__(k=k, seed=seed, alpha=alpha)
        self.epsilon = epsilon

    def select_action(self) -> int:
        """Select action using ε-greedy policy."""
        if self.rng.random() < self.epsilon:
            return int(self.rng.integers(0, self.k))
        return super().select_action()

    def decay_epsilon(self, t: int, T: int) -> None:
        """Decay epsilon over time (optional feature)."""
        self.epsilon = self.epsilon * (1 - t / T)
        self.epsilon = max(self.epsilon, 0.01)  # Optional: set a minimum epsilon
