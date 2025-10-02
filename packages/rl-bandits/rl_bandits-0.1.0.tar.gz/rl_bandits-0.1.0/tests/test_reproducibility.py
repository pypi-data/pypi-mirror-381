"""Tests for reproducibility and seeding."""

import numpy as np
from rlbandits import (
    Bandit,
    EpsilonGreedyAgent,
    Experiment,
    run_multi_experiment,
    set_global_seed,
)


class TestReproducibility:
    """Test reproducibility of experiments."""

    def test_bandit_reproducibility(self):
        """Test that bandit environments are reproducible with same seed."""
        bandit1 = Bandit(k=10, seed=42)
        bandit2 = Bandit(k=10, seed=42)

        # Same q_true values
        np.testing.assert_array_equal(bandit1.q_true, bandit2.q_true)

        # Same reward sequences
        rewards1 = [bandit1.step(0) for _ in range(100)]
        rewards2 = [bandit2.step(0) for _ in range(100)]
        np.testing.assert_array_equal(rewards1, rewards2)

    def test_agent_reproducibility(self):
        """Test that agents are reproducible with same seed."""
        agent1 = EpsilonGreedyAgent(k=10, epsilon=0.1, seed=42)
        agent2 = EpsilonGreedyAgent(k=10, epsilon=0.1, seed=42)

        # Same action sequences
        actions1 = [agent1.select_action() for _ in range(100)]
        actions2 = [agent2.select_action() for _ in range(100)]
        np.testing.assert_array_equal(actions1, actions2)

    def test_experiment_reproducibility(self):
        """Test that full experiments are reproducible."""
        # Run same experiment twice
        bandit1 = Bandit(k=10, seed=42)
        agent1 = EpsilonGreedyAgent(k=10, epsilon=0.1, seed=123)
        exp1 = Experiment(bandit1, agent1, steps=100)
        result1 = exp1.run()

        bandit2 = Bandit(k=10, seed=42)
        agent2 = EpsilonGreedyAgent(k=10, epsilon=0.1, seed=123)
        exp2 = Experiment(bandit2, agent2, steps=100)
        result2 = exp2.run()

        # Results should be identical
        np.testing.assert_array_equal(result1.rewards, result2.rewards)
        np.testing.assert_array_equal(result1.optimal_flags, result2.optimal_flags)

    def test_multi_run_reproducibility(self):
        """Test that multi-run experiments are reproducible."""
        agent1 = EpsilonGreedyAgent(k=10, epsilon=0.1)
        results1 = run_multi_experiment(
            bandit_class=Bandit,
            bandit_kwargs={"k": 10, "reward_std": 1.0},
            agent=agent1,
            steps=100,
            runs=10,
            warm_start=True,
        )

        agent2 = EpsilonGreedyAgent(k=10, epsilon=0.1)
        results2 = run_multi_experiment(
            bandit_class=Bandit,
            bandit_kwargs={"k": 10, "reward_std": 1.0},
            agent=agent2,
            steps=100,
            runs=10,
            warm_start=True,
        )

        # Results should be identical (same seeds used internally)
        np.testing.assert_array_equal(results1["avg_reward"], results2["avg_reward"])
        np.testing.assert_array_equal(results1["avg_optimal"], results2["avg_optimal"])

    def test_different_seeds_different_results(self):
        """Test that different seeds produce different results."""
        bandit1 = Bandit(k=10, seed=42)
        bandit2 = Bandit(k=10, seed=123)

        # Different q_true values
        assert not np.array_equal(bandit1.q_true, bandit2.q_true)

        # Different reward sequences
        rewards1 = [bandit1.step(0) for _ in range(100)]
        rewards2 = [bandit2.step(0) for _ in range(100)]
        assert not np.array_equal(rewards1, rewards2)

    def test_global_seed_function(self):
        """Test global seed setting function."""
        set_global_seed(42)

        # Create objects that depend on numpy random state
        arr1 = np.random.randn(10)

        set_global_seed(42)
        arr2 = np.random.randn(10)

        # Should be identical
        np.testing.assert_array_equal(arr1, arr2)

    def test_agent_reset_functionality(self):
        """Test that agent reset works correctly."""
        agent = EpsilonGreedyAgent(k=10, epsilon=0.1, seed=42)

        # Modify agent state
        agent.update(0, 1.0)
        agent.update(1, 2.0)

        # Reset should restore initial state
        agent.reset(seed=42)
        np.testing.assert_array_equal(agent.Q, np.zeros(10))
        np.testing.assert_array_equal(agent.N, np.zeros(10))

        # Should produce same action sequence as fresh agent
        fresh_agent = EpsilonGreedyAgent(k=10, epsilon=0.1, seed=42)

        actions_reset = [agent.select_action() for _ in range(50)]
        actions_fresh = [fresh_agent.select_action() for _ in range(50)]

        np.testing.assert_array_equal(actions_reset, actions_fresh)
