"""YAML-based experiment configuration runner."""

from __future__ import annotations
from typing import Dict, Any, Type
import os
import yaml
from ..envs import Bandit, NonStationaryBandit
from ..agents import (
    BaseAgent,
    GreedyAgent,
    EpsilonGreedyAgent,
    UCBAgent,
    GradientBanditAgent,
)
from ..core import run_multi_experiment, plot_comparison, print_summary


class YAMLExperimentRunner:
    """Runner for YAML-configured bandit experiments."""

    # Map string names to classes
    BANDIT_CLASSES = {
        "Bandit": Bandit,
        "NonStationaryBandit": NonStationaryBandit,
    }

    AGENT_CLASSES = {
        "GreedyAgent": GreedyAgent,
        "EpsilonGreedyAgent": EpsilonGreedyAgent,
        "UCBAgent": UCBAgent,
        "GradientBanditAgent": GradientBanditAgent,
    }

    def __init__(self, config_path: str):
        """Initialize runner with YAML config file."""
        self.config_path = config_path
        self.config = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        """Load YAML configuration file."""
        with open(self.config_path, "r") as f:
            return yaml.safe_load(f)

    def _create_bandit_class(self) -> Type:
        """Get bandit class from config."""
        bandit_name = self.config["bandit"]["class"]
        if bandit_name not in self.BANDIT_CLASSES:
            raise ValueError(f"Unknown bandit class: {bandit_name}")
        return self.BANDIT_CLASSES[bandit_name]

    def _get_bandit_kwargs(self) -> Dict[str, Any]:
        """Extract bandit parameters from config."""
        bandit_config = self.config["bandit"].copy()
        del bandit_config["class"]  # Remove class name
        return bandit_config

    def _create_agent(self, agent_config: Dict[str, Any]) -> BaseAgent:
        """Create agent instance from config."""
        agent_name = agent_config["class"]
        if agent_name not in self.AGENT_CLASSES:
            raise ValueError(f"Unknown agent class: {agent_name}")

        agent_class = self.AGENT_CLASSES[agent_name]
        params = agent_config.get("params", {})
        return agent_class(**params)

    def run_experiment(self) -> Dict[str, Dict[str, Any]]:
        """Run the full experiment defined in YAML config."""
        print(f"🎯 Running experiment: {self.config['experiment']['name']}")
        print(f"📝 Description: {self.config['experiment']['description']}")
        print("=" * 60)

        # Get experiment parameters
        bandit_class = self._create_bandit_class()
        bandit_kwargs = self._get_bandit_kwargs()
        runs_config = self.config["runs"]

        # Run experiments for each agent
        results = {}
        for agent_config in self.config["agents"]:
            agent_name = agent_config["name"]
            print(f"\n🤖 Running {agent_name}...")

            agent = self._create_agent(agent_config)

            # Run multi-experiment
            agent_results = run_multi_experiment(
                bandit_class=bandit_class,
                bandit_kwargs=bandit_kwargs,
                agent=agent,
                steps=runs_config["steps"],
                runs=runs_config["num_runs"],
                warm_start=runs_config.get("warm_start", True),
            )

            results[agent_name] = agent_results
            print_summary(agent_results, agent_name)

        return results

    def plot_results(self, results: Dict[str, Dict[str, Any]]) -> None:
        """Plot experiment results using enhanced plotting."""
        plotting_config = self.config.get("plotting", {})
        title = plotting_config.get("title", self.config["experiment"]["name"])
        save_path = plotting_config.get("save_path")
        figsize = tuple(plotting_config.get("figsize", [16, 8]))
        plot_style = plotting_config.get("style", "comparison")

        # Create results directory if needed
        if save_path:
            os.makedirs(os.path.dirname(save_path), exist_ok=True)

        # Choose plotting function based on style
        if plot_style == "parameter_study":
            from ..core.utils import plot_parameter_study

            # Extract parameter name from experiment description or title
            param_name = "Parameter"
            if "learning rate" in title.lower() or "alpha" in title.lower():
                param_name = "Learning Rate (α)"
            elif "epsilon" in title.lower():
                param_name = "Epsilon (ε)"
            elif "confidence" in title.lower() or "ucb" in title.lower():
                param_name = "UCB Confidence (c)"

            plot_parameter_study(
                results=results,
                parameter_name=param_name,
                title=title,
                save_path=save_path,
            )
        else:
            # Default to comparison plot
            plot_comparison(
                results=results, title=title, save_path=save_path, figsize=figsize
            )

        if save_path:
            print(f"📊 Plot saved to: {save_path}")

    def run_and_plot(self) -> Dict[str, Dict[str, Any]]:
        """Run experiment and generate plots."""
        results = self.run_experiment()

        print("\n📊 Generating plots...")
        self.plot_results(results)

        print(f"\n✅ Experiment '{self.config['experiment']['name']}' completed!")
        return results


def run_yaml_experiment(config_path: str) -> Dict[str, Dict[str, Any]]:
    """Convenience function to run a YAML experiment."""
    runner = YAMLExperimentRunner(config_path)
    return runner.run_and_plot()


def run_all_experiments(experiments_dir: str = None) -> None:
    """Run all YAML experiments in the experiments directory."""
    if experiments_dir is None:
        experiments_dir = os.path.dirname(__file__)

    yaml_files = [f for f in os.listdir(experiments_dir) if f.endswith(".yaml")]

    print(f"🚀 Running {len(yaml_files)} experiments from {experiments_dir}")
    print("=" * 70)

    for yaml_file in sorted(yaml_files):
        config_path = os.path.join(experiments_dir, yaml_file)
        print(f"\n📋 Processing: {yaml_file}")
        try:
            run_yaml_experiment(config_path)
        except Exception as e:
            print(f"❌ Error running {yaml_file}: {e}")
            continue

    print("\n🎉 All experiments completed!")


if __name__ == "__main__":
    # Run all experiments in this directory
    run_all_experiments()
