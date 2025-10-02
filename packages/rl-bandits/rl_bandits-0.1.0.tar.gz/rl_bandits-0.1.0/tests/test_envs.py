"""Tests for bandit environments."""

import numpy as np
from rlbandits.envs import Bandit, NonStationaryBandit


class TestBandit:
    """Test stationary bandit environment."""

    def test_initialization(self):
        """Test bandit initialization."""
        bandit = Bandit(k=5, reward_std=0.5, seed=42)
        assert bandit.k == 5
        assert bandit.reward_std == 0.5
        assert len(bandit.q_true) == 5

    def test_deterministic_with_seed(self):
        """Test that same seed produces same q_true values."""
        bandit1 = Bandit(k=10, seed=42)
        bandit2 = Bandit(k=10, seed=42)
        np.testing.assert_array_equal(bandit1.q_true, bandit2.q_true)

    def test_step_returns_float(self):
        """Test that step returns a float reward."""
        bandit = Bandit(k=10, seed=42)
        reward = bandit.step(0)
        assert isinstance(reward, (float, np.floating))

    def test_optimal_action(self):
        """Test optimal action identification."""
        bandit = Bandit(k=10, seed=42)
        optimal = bandit.optimal_action()
        assert 0 <= optimal < 10
        assert optimal == np.argmax(bandit.q_true)

    def test_reward_distribution(self):
        """Test that rewards follow expected distribution."""
        bandit = Bandit(k=10, reward_std=1.0, seed=42)
        action = 0
        rewards = [bandit.step(action) for _ in range(1000)]

        # Should be approximately normal around q_true[action]
        mean_reward = np.mean(rewards)
        assert (
            abs(mean_reward - bandit.q_true[action]) < 0.1
        )  # Within reasonable tolerance


class TestNonStationaryBandit:
    """Test non-stationary bandit environment."""

    def test_initialization(self):
        """Test non-stationary bandit initialization."""
        bandit = NonStationaryBandit(k=5, walk_std=0.01, seed=42)
        assert bandit.k == 5
        assert bandit.walk_std == 0.01

    def test_q_values_change(self):
        """Test that q* values change over time."""
        bandit = NonStationaryBandit(k=10, walk_std=0.1, seed=42)
        initial_q = bandit.q_true.copy()

        # Take several steps
        for _ in range(100):
            bandit.step(0)

        # Q values should have changed
        assert not np.allclose(initial_q, bandit.q_true, atol=0.01)

    def test_inheritance(self):
        """Test that NonStationaryBandit inherits from Bandit."""
        bandit = NonStationaryBandit(k=10, seed=42)
        assert isinstance(bandit, Bandit)
        assert hasattr(bandit, "optimal_action")
        assert hasattr(bandit, "step")
