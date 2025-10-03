"""
GridWorldPy - A Python package for creating and visualizing grid world environments.

This package provides a flexible and interactive grid world environment
for reinforcement learning experiments and educational purposes.
"""

from .gridworld import GridWorldEnv
from .utils import policy_to_transition_matrix

__version__ = "0.1.1"
__author__ = "LIC"
__email__ = "liuchen.lic@gmail.com"

__all__ = ["GridWorldEnv", "policy_to_transition_matrix"]
