"""
Random graph utilities for generating and perturbing graphs.

This subpackage exposes helpers built on top of PyTorch and PyG to:
- generate Erdős–Rényi graphs (``erdos_renyi``)
- apply Bernoulli edge corruption (``bernoulli_corruption``)
- sample induced subgraphs uniformly (``uniform_sub_sampling``)
- sample induced subgraphs via BFS expansion (``bfs_sub_sampling``)
"""

__all__ = [
    "bernoulli_corruption",
    "bfs_sub_sampling",
    "erdos_renyi",
    "uniform_sub_sampling",
]

from ._random import bernoulli_corruption
from ._random import bfs_sub_sampling
from ._random import erdos_renyi
from ._random import uniform_sub_sampling
