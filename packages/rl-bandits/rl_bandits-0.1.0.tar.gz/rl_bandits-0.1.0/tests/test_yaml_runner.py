"""Tests for YAML experiment runner."""

import os
import tempfile
import yaml
import pytest
from rlbandits.experiments.yaml_runner import YAMLExperimentRunner


class TestYAMLExperimentRunner:
    """Test YAML experiment runner functionality."""
    
    def create_test_config(self) -> str:
        """Create a minimal test configuration."""
        config = {
            "experiment": {
                "name": "Test Experiment",
                "description": "A test experiment"
            },
            "bandit": {
                "class": "Bandit",
                "k": 3,
                "reward_std": 1.0
            },
            "runs": {
                "steps": 10,
                "num_runs": 2,
                "warm_start": True
            },
            "agents": [
                {
                    "name": "Test Greedy",
                    "class": "GreedyAgent",
                    "params": {"k": 3}
                },
                {
                    "name": "Test ε-Greedy",
                    "class": "EpsilonGreedyAgent", 
                    "params": {"k": 3, "epsilon": 0.1}
                }
            ],
            "plotting": {
                "title": "Test Plot",
                "save_path": "test_plot.png"
            }
        }
        
        # Create temporary file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            yaml.dump(config, f)
            return f.name
    
    def test_config_loading(self):
        """Test YAML configuration loading."""
        config_path = self.create_test_config()
        
        try:
            runner = YAMLExperimentRunner(config_path)
            assert runner.config["experiment"]["name"] == "Test Experiment"
            assert len(runner.config["agents"]) == 2
            assert runner.config["bandit"]["class"] == "Bandit"
        finally:
            os.unlink(config_path)
    
    def test_bandit_class_creation(self):
        """Test bandit class creation from config."""
        config_path = self.create_test_config()
        
        try:
            runner = YAMLExperimentRunner(config_path)
            bandit_class = runner._create_bandit_class()
            from rlbandits.envs import Bandit
            assert bandit_class == Bandit
        finally:
            os.unlink(config_path)
    
    def test_bandit_kwargs_extraction(self):
        """Test bandit parameter extraction."""
        config_path = self.create_test_config()
        
        try:
            runner = YAMLExperimentRunner(config_path)
            kwargs = runner._get_bandit_kwargs()
            assert kwargs["k"] == 3
            assert kwargs["reward_std"] == 1.0
            assert "class" not in kwargs  # Should be removed
        finally:
            os.unlink(config_path)
    
    def test_agent_creation(self):
        """Test agent creation from config."""
        config_path = self.create_test_config()
        
        try:
            runner = YAMLExperimentRunner(config_path)
            agent_config = runner.config["agents"][0]
            agent = runner._create_agent(agent_config)
            
            from rlbandits.agents import GreedyAgent
            assert isinstance(agent, GreedyAgent)
            assert agent.k == 3
        finally:
            os.unlink(config_path)
    
    def test_invalid_bandit_class(self):
        """Test error handling for invalid bandit class."""
        config_path = self.create_test_config()
        
        try:
            runner = YAMLExperimentRunner(config_path)
            runner.config["bandit"]["class"] = "InvalidBandit"
            
            with pytest.raises(ValueError, match="Unknown bandit class"):
                runner._create_bandit_class()
        finally:
            os.unlink(config_path)
    
    def test_invalid_agent_class(self):
        """Test error handling for invalid agent class."""
        config_path = self.create_test_config()
        
        try:
            runner = YAMLExperimentRunner(config_path)
            invalid_agent_config = {
                "class": "InvalidAgent",
                "params": {}
            }
            
            with pytest.raises(ValueError, match="Unknown agent class"):
                runner._create_agent(invalid_agent_config)
        finally:
            os.unlink(config_path)
    
    def test_run_experiment_basic(self):
        """Test basic experiment running (without plotting)."""
        config_path = self.create_test_config()
        
        try:
            runner = YAMLExperimentRunner(config_path)
            results = runner.run_experiment()
            
            # Should have results for both agents
            assert len(results) == 2
            assert "Test Greedy" in results
            assert "Test ε-Greedy" in results
            
            # Each result should have the expected structure
            for agent_name, agent_results in results.items():
                assert "avg_reward" in agent_results
                assert "avg_optimal" in agent_results
                assert len(agent_results["avg_reward"]) > 0
                
        finally:
            os.unlink(config_path)
