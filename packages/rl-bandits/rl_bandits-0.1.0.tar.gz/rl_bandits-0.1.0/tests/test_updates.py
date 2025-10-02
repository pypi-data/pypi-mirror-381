"""Tests for agent update rules."""

import numpy as np
from rlbandits.agents import (
    GreedyAgent,
    EpsilonGreedyAgent,
    UCBAgent,
    GradientBanditAgent,
)


class TestGreedyAgent:
    """Test greedy agent update rules."""

    def test_initialization(self):
        """Test agent initialization."""
        agent = GreedyAgent(k=5, seed=42)
        assert agent.k == 5
        assert len(agent.Q) == 5
        assert len(agent.N) == 5
        np.testing.assert_array_equal(agent.Q, np.zeros(5))
        np.testing.assert_array_equal(agent.N, np.zeros(5))

    def test_sample_average_update(self):
        """Test sample average update rule."""
        agent = GreedyAgent(k=10, alpha=None, seed=42)

        # First update
        agent.update(0, 1.0)
        assert agent.Q[0] == 1.0
        assert agent.N[0] == 1

        # Second update
        agent.update(0, 3.0)
        assert agent.Q[0] == 2.0  # (1.0 + 3.0) / 2
        assert agent.N[0] == 2

    def test_constant_step_size_update(self):
        """Test constant step-size update rule."""
        agent = GreedyAgent(k=10, alpha=0.1, seed=42)

        # First update
        agent.update(0, 1.0)
        assert agent.Q[0] == 0.1  # 0 + 0.1 * (1.0 - 0)
        assert agent.N[0] == 1

        # Second update
        agent.update(0, 2.0)
        expected = 0.1 + 0.1 * (2.0 - 0.1)  # Q + α * (R - Q)
        assert abs(agent.Q[0] - expected) < 1e-10

    def test_greedy_action_selection(self):
        """Test greedy action selection."""
        agent = GreedyAgent(k=3, seed=42)
        agent.Q = np.array([1.0, 3.0, 2.0])

        # Should select action 1 (highest Q-value)
        action = agent.select_action()
        assert action == 1

    def test_tie_breaking(self):
        """Test random tie breaking in action selection."""
        agent = GreedyAgent(k=3, seed=42)
        agent.Q = np.array([2.0, 2.0, 1.0])  # Tie between actions 0 and 1

        # Should select either 0 or 1
        actions = [agent.select_action() for _ in range(100)]
        unique_actions = set(actions)
        assert unique_actions.issubset({0, 1})
        assert len(unique_actions) > 1  # Should see both actions due to randomness


class TestEpsilonGreedyAgent:
    """Test epsilon-greedy agent."""

    def test_epsilon_exploration(self):
        """Test epsilon exploration behavior."""
        agent = EpsilonGreedyAgent(k=10, epsilon=1.0, seed=42)  # Always explore
        agent.Q = np.array([10.0] + [0.0] * 9)  # Action 0 is clearly best

        # With ε=1.0, should never select greedy action consistently
        actions = [agent.select_action() for _ in range(100)]
        unique_actions = set(actions)
        assert len(unique_actions) > 1  # Should explore multiple actions

    def test_greedy_exploitation(self):
        """Test greedy exploitation when ε=0."""
        agent = EpsilonGreedyAgent(k=10, epsilon=0.0, seed=42)  # Never explore
        agent.Q = np.array([10.0] + [0.0] * 9)  # Action 0 is clearly best

        # With ε=0.0, should always select greedy action
        actions = [agent.select_action() for _ in range(100)]
        assert all(action == 0 for action in actions)


class TestUCBAgent:
    """Test UCB agent."""

    def test_unvisited_actions_first(self):
        """Test that unvisited actions are selected first."""
        agent = UCBAgent(k=5, c=2.0, seed=42)

        # First 5 actions should be 0, 1, 2, 3, 4 (in some order)
        actions = []
        for _ in range(5):
            action = agent.select_action()
            actions.append(action)
            agent.update(action, 1.0)  # Update to increment N[action]

        assert set(actions) == {0, 1, 2, 3, 4}

    def test_ucb_calculation(self):
        """Test UCB value calculation."""
        agent = UCBAgent(k=3, c=2.0, seed=42)

        # Manually set up state
        agent.Q = np.array([1.0, 2.0, 0.5])
        agent.N = np.array([10, 5, 20])
        agent.total_steps = 35

        # Calculate expected UCB values
        # UCB = Q + c * sqrt(ln(t) / N)
        expected_ucb = agent.Q + agent.c * np.sqrt(
            np.log(agent.total_steps + 1) / agent.N
        )

        # Select action and verify it's the one with highest UCB
        action = agent.select_action()
        assert action == np.argmax(expected_ucb)


class TestGradientBanditAgent:
    """Test gradient bandit agent."""

    def test_initialization(self):
        """Test gradient bandit initialization."""
        agent = GradientBanditAgent(k=5, alpha=0.1, seed=42)
        assert agent.k == 5
        assert agent.alpha == 0.1
        np.testing.assert_array_equal(agent.H, np.zeros(5))
        np.testing.assert_array_almost_equal(agent.pi, np.ones(5) / 5)

    def test_preference_updates(self):
        """Test preference updates."""
        agent = GradientBanditAgent(k=3, alpha=0.1, seed=42)

        # Take an action and update with first reward
        action = agent.select_action()
        agent.update(action, 1.0)

        # Take another action and update with different reward
        initial_H = agent.H.copy()
        action = agent.select_action()
        agent.update(action, 2.0)  # Different reward should cause preference change

        # Preferences should have changed
        assert not np.array_equal(initial_H, agent.H)

    def test_probability_normalization(self):
        """Test that action probabilities sum to 1."""
        agent = GradientBanditAgent(k=10, alpha=0.1, seed=42)

        for _ in range(100):
            action = agent.select_action()
            agent.update(action, np.random.randn())
            # Probabilities should always sum to 1
            assert abs(agent.pi.sum() - 1.0) < 1e-10
