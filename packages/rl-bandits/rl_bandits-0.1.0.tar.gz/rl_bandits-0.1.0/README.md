# RL Bandits

A modular Python library for multi-armed bandit algorithms, designed for research and experimentation.

## Features

- **Environments**: Stationary and non-stationary k-armed bandits
- **Agents**: ε-greedy, UCB, gradient bandit algorithms
- **Evaluation**: Single and multi-run experiment framework
- **Utilities**: Plotting, seeding, and configuration management

## Installation

```bash
# Clone the repository
git clone https://github.com/meeran03/rl-bandits.git
cd rl-bandits

# Install in development mode
pip install -e .

# Or install with development dependencies
pip install -e ".[dev]"
```

## Quick Start

```python
from rlbandits import Bandit, EpsilonGreedyAgent, run_multi_experiment, plot_curves

# Create environment and agent
bandit_kwargs = {"k": 10, "reward_std": 1.0}
agent = EpsilonGreedyAgent(k=10, epsilon=0.1)

# Run experiment
results = run_multi_experiment(
    bandit_class=Bandit,
    bandit_kwargs=bandit_kwargs,
    agent=agent,
    steps=1000,
    runs=200
)

# Plot results
plot_curves(results, title="ε-Greedy Performance")
```

## Project Structure

```
rl-bandits/
├── README.md
├── pyproject.toml
├── requirements.txt
├── rlbandits/
│   ├── __init__.py
│   ├── envs/                    # Bandit environments
│   │   ├── stationary_bandit.py
│   │   └── nonstationary_bandit.py
│   ├── agents/                  # Bandit algorithms
│   │   ├── epsilon_greedy.py
│   │   ├── ucb.py
│   │   └── gradient_bandit.py
│   ├── core/                    # Experiment framework
│   │   ├── runner.py
│   │   ├── eval.py
│   │   └── utils.py
│   └── experiments/             # Configuration files
├── notebooks/                   # Jupyter notebooks
├── tests/                       # Unit tests
└── .github/workflows/           # CI/CD
```

## Algorithms Implemented

- **Greedy**: Pure greedy action selection
- **ε-Greedy**: Epsilon-greedy with exploration
- **UCB**: Upper Confidence Bound
- **Gradient Bandit**: Preference-based policy gradient

## Development

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Format code
black rlbandits/ tests/

# Type checking
mypy rlbandits/
```

## License

MIT License
