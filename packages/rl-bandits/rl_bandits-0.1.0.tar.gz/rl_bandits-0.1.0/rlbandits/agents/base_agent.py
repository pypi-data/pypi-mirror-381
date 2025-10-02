"""Base agent interface for bandit algorithms."""

from __future__ import annotations
import numpy as np


class BaseAgent:
    """Common interface all bandit agents must implement."""

    def __init__(self, k: int = 10, seed: int | None = None):
        self.k = k
        self.rng = np.random.default_rng(seed)

    def select_action(self) -> int:
        """Select an action based on current policy."""
        raise NotImplementedError

    def update(self, action: int, reward: float) -> None:
        """Update internal state based on action and reward."""
        raise NotImplementedError

    def reset(self, seed: int | None = None) -> None:
        """Reset internal state (called before each run in multi-run eval)."""
        self.rng = np.random.default_rng(seed)
