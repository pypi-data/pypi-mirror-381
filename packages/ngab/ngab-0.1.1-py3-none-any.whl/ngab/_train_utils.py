import pathlib
from typing import NamedTuple
from typing import Self

import torch
import torch.utils.data
import torch_geometric.data as pyg_data

from ._dataset import GADataset
from ._dataset import GADatasetItem


class GADatasetBatch(NamedTuple):
    base_graphs: pyg_data.Data
    base_node_masks: torch.BoolTensor

    corrupted_graphs: pyg_data.Data
    corrupted_node_masks: torch.BoolTensor

    def to(self, device: torch.device) -> Self:
        return GADatasetBatch(
            self.base_graphs.to(device),
            self.base_node_masks.to(device),
            self.corrupted_graphs.to(device),
            self.corrupted_node_masks.to(device),
        )

    def __len__(self) -> int:
        return len(self.base_graphs)


def _get_masks(data: pyg_data.Data) -> torch.BoolTensor:
    """
    Return a mask where where masks[i] = [True*nb_node, False*(max_node - nb_node)]
    """
    orders = torch.bincount(data.batch)
    num_graphs = len(orders)
    masks = torch.arange(int(torch.max(orders))).repeat(num_graphs).reshape(
        (num_graphs, -1)
    ) < orders.reshape((-1, 1))

    return masks


def collate_fn(
    batch_l: list[GADatasetItem],
) -> GADatasetBatch:
    base_batch = pyg_data.Batch.from_data_list([item.base_graph for item in batch_l])
    corrupted_batch = pyg_data.Batch.from_data_list(
        [item.corrupted_graph for item in batch_l]
    )

    return GADatasetBatch(
        base_graphs=base_batch,
        base_node_masks=_get_masks(base_batch),
        corrupted_graphs=corrupted_batch,
        corrupted_node_masks=_get_masks(corrupted_batch),
    )


def setup_data(
    *,
    dataset_path: pathlib.Path,
    batch_size: int,
    pin_memory: bool = True,
    shuffle: bool = True,
    num_workers: int = 8,
    prefetch_factor: int = 6,
    persistent_workers: bool = True,
) -> tuple[
    GADataset,
    GADataset,
    torch.utils.data.DataLoader[GADatasetBatch],
    torch.utils.data.DataLoader[GADatasetBatch],
]:
    train_dataset = GADataset(root=dataset_path)
    val_dataset = GADataset(root=dataset_path, validation=True)

    train_loader = torch.utils.data.DataLoader(
        train_dataset,
        batch_size=batch_size,
        collate_fn=collate_fn,
        pin_memory=pin_memory,
        shuffle=shuffle,
        num_workers=num_workers,
        prefetch_factor=prefetch_factor,
        persistent_workers=persistent_workers,
    )

    val_loader = torch.utils.data.DataLoader(
        val_dataset,
        batch_size=batch_size,
        collate_fn=collate_fn,
        pin_memory=pin_memory,
        shuffle=shuffle,
        num_workers=num_workers,
        prefetch_factor=prefetch_factor,
        persistent_workers=persistent_workers,
    )

    return train_dataset, val_dataset, train_loader, val_loader
