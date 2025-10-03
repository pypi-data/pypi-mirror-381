"""
Dataset utilities for Graph Alignment/Matching tasks.

This module exposes:
- ``GADatasetItem``: a lightweight container bundling a base graph with its
  corresponding corrupted graph as PyG ``Data`` objects.
- ``GADataset``: an indexable dataset that loads graphs from safetensors files
  stored on disk and returns ``GADatasetItem`` instances. An optional
  ``transform`` callable can be provided to map ``pyg_data.Data -> pyg_data.Data``
  and will be applied on-the-fly in ``__getitem__``.
"""

import os
import os.path
from pathlib import Path
from typing import Callable
from typing import NamedTuple
from typing import Self
from typing import override

from safetensors.torch import load_file
import torch.utils.data
import torch_geometric.data as pyg_data


class GADatasetItem(NamedTuple):
    base_graph: pyg_data.Data
    corrupted_graph: pyg_data.Data


class GADataset(torch.utils.data.Dataset):
    """
    Graph Matching dataset abstraction class.

    Loads graph pairs from safetensors files under a given ``root`` directory.
    Items are returned as ``GADatasetItem(base_graph, corrupted_graph)``.

    If a ``transform`` is provided, it will be applied to both ``base_graph`` and
    ``corrupted_graph`` at retrieval time.
    """

    base_graphs: dict[int, pyg_data.Data]
    corrupted_graphs: dict[int, pyg_data.Data]
    transform: Callable[[pyg_data.Data], pyg_data.Data] | None
    _split: str

    def __init__(
        self,
        root: str | os.PathLike,
        *,
        validation: bool = False,
        transform: Callable[[pyg_data.Data], pyg_data.Data] | None = None,
    ) -> None:
        """
        Initialize the Graph Matching dataset.

        Arguments:
        - root: Path to the dataset directory containing safetensors files.
        - validation: If True, load the validation split; otherwise, the training split.
        - transform: Optional callable applied to graphs on retrieval
          (``pyg_data.Data -> pyg_data.Data``).
        """
        super().__init__()
        prefix = "val" if validation else "train"
        self._split = prefix
        self.transform = transform
        try:
            orders = {
                int(k): v
                for k, v in load_file(
                    os.path.join(root, f"{prefix}-orders.safetensors")
                ).items()
            }
            self.base_graphs = {
                int(k): pyg_data.Data(edge_index=v, num_nodes=int(orders[int(k)][0]))
                for k, v in load_file(
                    os.path.join(root, f"{prefix}-base-graphs.safetensors")
                ).items()
            }
            self.corrupted_graphs = {
                int(k): pyg_data.Data(edge_index=v, num_nodes=int(orders[int(k)][1]))
                for k, v in load_file(
                    os.path.join(root, f"{prefix}-corrupted-graphs.safetensors")
                ).items()
            }
            print(len(self.base_graphs))
            print(max(self.base_graphs.keys()))
            print(len(self.corrupted_graphs))
            print(max(self.corrupted_graphs.keys()))

        except Exception as e:  # noqa: BLE001
            raise RuntimeError("Unable to load dataset from safetensors files") from e

    @override
    def __len__(self) -> int:
        """
        Number of GADatasetItem into the dataset.
        """
        return len(self.corrupted_graphs)

    @override
    def __getitem__(self, index) -> GADatasetItem:
        """
        Return the index-th ``GADatasetItem`` in the dataset.
        """
        base_graph = self.base_graphs[index]
        corrupted_graph = self.corrupted_graphs[index]

        if self.transform is not None:
            base_graph = self.transform(base_graph)
            corrupted_graph = self.transform(corrupted_graph)

        return GADatasetItem(base_graph, corrupted_graph)

    @override
    def __iter__(self) -> Self:
        self.iter_index = 0
        return self

    @override
    def __next__(
        self,
    ) -> GADatasetItem:
        if self.iter_index < len(self):
            res = self[self.iter_index]
            self.iter_index += 1
            return res
        else:
            raise StopIteration

    @override
    def __repr__(self) -> str:
        return f"GADataset(size={len(self)}, split={self._split})"

def download_dataset(name: str, root: str | os.PathLike = "graph-alignment-benchmark-data") -> str | os.PathLike:
    """
    Download a dataset from the Hugging Face Hub.
    """
    required_files = (
        "train-base-graphs.safetensors",
        "train-corrupted-graphs.safetensors",
        "train-orders.safetensors",
        "val-base-graphs.safetensors",
        "val-corrupted-graphs.safetensors",
        "val-orders.safetensors",
    )

    root_path = Path(root)
    dataset_dir = root_path / name

    def has_all_required_files(directory: Path) -> bool:
        return all((directory / fname).is_file() for fname in required_files)

    # If locally available and complete, return the path immediately
    if has_all_required_files(dataset_dir):
        return str(dataset_dir)

    # Otherwise, download only that subdataset from HF
    from huggingface_hub import snapshot_download

    repo_id = "alagesse/graph-alignment-benchmark-data"
    root_path.mkdir(parents=True, exist_ok=True)

    snapshot_download(
        repo_id=repo_id,
        repo_type="dataset",
        allow_patterns=[f"{name}/{fname}" for fname in required_files],
        local_dir=str(root_path),
        local_dir_use_symlinks=False,
    )

    # Validate again; if still missing, the subdataset likely doesn't exist
    if not has_all_required_files(dataset_dir):
        raise FileNotFoundError(
            f"Subdataset '{name}' not found or incomplete in '{repo_id}'."
        )

    return str(dataset_dir)
