from .experiments import EXPERIMENTS

__version__ = "0.1.0"

def run(n: int):
    """Run an experiment by number."""
    if n in EXPERIMENTS:
        return EXPERIMENTS[n]()
    raise ValueError(f"Experiment {n} not found. Available: {list(EXPERIMENTS.keys())}")
