"""
Noisy Graph Alignment Benchmark (NGAB) - a library for benchmarking GNNs on graph alignment tasks and generating positional encodings.
"""

__all__ = [
    "GADataset",
    "GADatasetItem",
    "download_dataset",
    "TrainConfig",
    "train_loop",
    "GADatasetBatch",
    "setup_data",
]


from . import chem
from . import models
from . import random
from ._dataset import GADataset
from ._dataset import GADatasetItem
from ._dataset import download_dataset
from ._train import TrainConfig
from ._train import train as train_loop
from ._train_utils import GADatasetBatch
from ._train_utils import setup_data
