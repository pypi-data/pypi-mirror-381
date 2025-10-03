import os
import pathlib
import statistics
import time
from typing import NamedTuple

from jaxtyping import Bool
from jaxtyping import Float
from jaxtyping import Int
import numpy as np
from safetensors.torch import save_model
from scipy.optimize import linear_sum_assignment
import torch
import torch.utils.data
from torch_geometric.utils import degree
import wandb

import ngab

from ._train_utils import GADatasetBatch
from ._train_utils import setup_data


def siamese_similarity(
    model: torch.nn.Module, batch: GADatasetBatch
) -> Float[torch.Tensor, "batch max_base_nodes max_corrupted_nodes"]:
    """
    Compute per-graph similarity matrices between base and corrupted graphs.

    Returns a tensor of shape [batch, max_base_nodes, max_corrupted_nodes].
    """
    # Forward pass on each side; models expect a PyG Batch and return [total_nodes, D]
    base_embeddings: Float[torch.Tensor, "total_base_nodes features"] = model(
        batch.base_graphs
    )
    corrupted_embeddings: Float[torch.Tensor, "total_corrupted_nodes features"] = model(
        batch.corrupted_graphs
    )

    assert base_embeddings.dim() == 2, "Model must return [num_nodes, features]"
    assert corrupted_embeddings.dim() == 2, "Model must return [num_nodes, features]"
    assert base_embeddings.shape[1] == corrupted_embeddings.shape[1], (
        "Base and corrupted embeddings must have the same feature dimension"
    )

    batch_size: int = batch.base_node_masks.shape[0]
    max_base_nodes: int = batch.base_node_masks.shape[1]
    max_corrupted_nodes: int = batch.corrupted_node_masks.shape[1]
    features_dim: int = base_embeddings.shape[1]

    # Pad to fixed [B, max_nodes, D] using the masks
    padded_base: Float[torch.Tensor, "batch max_base_nodes features"] = (
        base_embeddings.new_zeros((batch_size * max_base_nodes, features_dim))
    )
    padded_base[batch.base_node_masks.reshape(-1)] = base_embeddings
    padded_base = padded_base.view(batch_size, max_base_nodes, features_dim)

    padded_corrupted: Float[torch.Tensor, "batch max_corrupted_nodes features"] = (
        corrupted_embeddings.new_zeros((batch_size * max_corrupted_nodes, features_dim))
    )
    padded_corrupted[batch.corrupted_node_masks.reshape(-1)] = corrupted_embeddings
    padded_corrupted = padded_corrupted.view(
        batch_size, max_corrupted_nodes, features_dim
    )

    # Similarity matrices: [B, max_base_nodes, max_corrupted_nodes]
    alignment_similarities: Float[
        torch.Tensor, "batch max_base_nodes max_corrupted_nodes"
    ] = torch.bmm(padded_base, padded_corrupted.transpose(1, 2))

    return alignment_similarities


@torch.vmap
def __compute_losses(
    similarity_matrix: Float[torch.Tensor, "n n"], mask: Bool[torch.Tensor, " n"]
) -> Float[torch.Tensor, ""]:
    similarity_matrix.masked_fill_(torch.logical_not(mask), -float("inf"))
    diag_logits = torch.diag(torch.softmax(similarity_matrix, dim=1))
    diag_logits.masked_fill_(torch.logical_not(mask), 1)
    loss = -torch.log(diag_logits + 1e-7).mean()
    return loss


def compute_losses(
    similarity_matrices: Float[torch.Tensor, "batch n n"],
    masks: Bool[torch.Tensor, "batch n"],
) -> Float[torch.Tensor, " batch"]:
    """
    Batched alignment loss.

    Shapes
    - similarity_matrices: [batch, n, n]
    - masks: [batch, n] where True indicates a valid node (unpadded)

    Returns
    - per-example loss tensor of shape [batch]
    """
    assert similarity_matrices.dim() == 3, "similarity_matrices must be 3D [B, n, n]"
    assert masks.dim() == 2, "masks must be 2D [B, n]"
    assert similarity_matrices.shape[0] == masks.shape[0], "batch size mismatch"
    assert similarity_matrices.shape[1] == similarity_matrices.shape[2], "matrices must be square"
    assert similarity_matrices.shape[1] == masks.shape[1], "node dimension mismatch"

    return __compute_losses(similarity_matrices, masks)


class AccuraciesResults(NamedTuple):
    top1: Float[torch.Tensor, " batch"]
    top3: Float[torch.Tensor, " batch"]
    top5: Float[torch.Tensor, " batch"]


def compute_accuracies(
    alignement_similarities: Float[torch.Tensor, "batch n n"],
    masks: Bool[torch.Tensor, "batch n"],
) -> AccuraciesResults:
    top1 = torch.empty(
        (len(alignement_similarities),),
        dtype=torch.float,
        device=alignement_similarities.device,
    )
    top3 = torch.empty(
        (len(alignement_similarities),),
        dtype=torch.float,
        device=alignement_similarities.device,
    )
    top5 = torch.empty(
        (len(alignement_similarities),),
        dtype=torch.float,
        device=alignement_similarities.device,
    )
    for i, similarity_matrix in enumerate(alignement_similarities):
        similarity_matrix = similarity_matrix[masks[i]]
        _, indices = torch.sort(similarity_matrix, descending=True)

        top1_indices = indices[:, :1].detach().cpu()
        top1[i] = float(
            torch.isin(torch.arange(len(similarity_matrix)), top1_indices)
            .float()
            .mean()
        )

        top3_indices = indices[:, :3].detach().cpu()
        top3[i] = float(
            torch.isin(torch.arange(len(similarity_matrix)), top3_indices)
            .float()
            .mean()
        )

        top5_indices = indices[:, :5].detach().cpu()
        top5[i] = float(
            torch.isin(torch.arange(len(similarity_matrix)), top5_indices)
            .float()
            .mean()
        )

    return AccuraciesResults(top1=top1, top3=top3, top5=top5)


class LAPResults(NamedTuple):
    permutations: list[Int[torch.Tensor, " n"]]
    lap: list[float]


def compute_lap(
    alignement_similarities: Float[torch.Tensor, "batch n n"],
    masks: Bool[torch.Tensor, "batch n"],
) -> LAPResults:
    permuations = []
    lap = []
    for similarity_matrix, mask in zip(alignement_similarities, masks):
        similarity_matrix = (
            torch.softmax(similarity_matrix[mask], dim=-1).detach().cpu().numpy()
        )
        idx, permutation_pred = linear_sum_assignment(similarity_matrix, maximize=True)
        permuations.append(
            torch.tensor(
                permutation_pred,
                dtype=torch.long,
                device=alignement_similarities.device,
            )
        )
        lap.append(float((idx == permutation_pred).astype(float).mean()))

    return LAPResults(permutations=permuations, lap=lap)


@torch.no_grad
def compute_metrics(
    model: torch.nn.Module,
    loader: torch.utils.data.DataLoader,
    device: torch.device,
) -> dict[str, float]:
    metrics_l: dict[str, list[float]] = {
        "loss": [],
        "lap": [],
        "top_1": [],
        "top_3": [],
        "top_5": [],
    }

    batch: GADatasetBatch
    for i, batch in enumerate(loader):
        batch = batch.to(device)

        similarity_matrices = siamese_similarity(model, batch)
        masks = (
            batch.base_node_masks
        )  # The algorithm doesn't work with different size graph pairs

        losses = compute_losses(similarity_matrices, masks)
        metrics_l["loss"].append(float(losses.mean()))

        (top_1, top_3, top_5) = compute_accuracies(similarity_matrices, masks)
        metrics_l["top_1"].append(float(top_1.mean()))
        metrics_l["top_3"].append(float(top_3.mean()))
        metrics_l["top_5"].append(float(top_5.mean()))

        (_permutations, lap) = compute_lap(similarity_matrices, masks)

        metrics_l["lap"].append(statistics.mean(lap))

    return {k: statistics.mean(v) for (k, v) in metrics_l.items()}

def get_degree_histogram(dataset: ngab.GADataset) -> torch.Tensor:
        r"""Returns the degree histogram to be used as input for the :obj:`deg`
        argument in :class:`PNAConv`.
        """
        deg_histogram = torch.zeros(1, dtype=torch.long)
        for data in dataset:
            deg = degree(data.base_graph.edge_index[1], num_nodes=data.base_graph.num_nodes,
                         dtype=torch.long)
            deg_bincount = torch.bincount(deg, minlength=deg_histogram.numel())
            deg_histogram = deg_histogram.to(deg_bincount.device)
            if deg_bincount.numel() > deg_histogram.numel():
                deg_bincount[:deg_histogram.size(0)] += deg_histogram
                deg_histogram = deg_bincount
            else:
                assert deg_bincount.numel() == deg_histogram.numel()
                deg_histogram += deg_bincount

        return deg_histogram

class TrainConfig:
    model: torch.nn.Module
    dataset: pathlib.Path
    experiment: str
    run_name: str
    epochs: int
    batch_size: int
    device: torch.device
    log_frequency: int
    profile: bool
    optimizer: torch.optim.Optimizer
    scheduler: torch.optim.lr_scheduler._LRScheduler
    grad_clip: float
    confid_dict: dict[str, any]


def train(config: TrainConfig) -> None:
    # Load the training and validation datasets and build suitable loaders to batch the graphs together.
    (train_dataset, val_dataset, train_loader, val_loader) = setup_data(
        dataset_path=config.dataset,
        batch_size=config.batch_size,
    )
    model = config.model.to(config.device)
    optimizer = config.optimizer
    scheduler = config.scheduler

    # For PNA models, reinstantiate with degree information and rebuild optimizer
    if isinstance(config.model, ngab.models.PNA):
        deg = get_degree_histogram(train_dataset)

        model_args = {
            'in_features': config.model.in_features,
            'features': config.model.layer0.out_channels,
            'out_features': config.model.linear.out_features,
            'layers': len(config.model.layers) + 1,
            'deg': deg,
        }
        model = ngab.models.PNA(**model_args).to(config.device)
        # Safely rebind optimizer's parameters to the new model instance
        optimizer = config.optimizer
        new_params = list(model.parameters())
        if len(optimizer.param_groups) > 0:
            # Assign new params to the first group and drop extra groups
            optimizer.param_groups[0]["params"] = new_params
            for i in range(len(optimizer.param_groups) - 1, 0, -1):
                del optimizer.param_groups[i]
        else:
            optimizer.add_param_group({"params": new_params})
        # Clear any optimizer state tied to old parameter tensors
        optimizer.state.clear()



    run = wandb.init(
        project=config.experiment,
        name=config.run_name,
        config=config,
    )
    run.config.update(
        {"nb_params": sum([np.prod(p.size()) for p in model.parameters()])}
    )

    def forward_pass(model: torch.nn.Module, batch: GADatasetBatch) -> float:
        similarity_matrices = siamese_similarity(model, batch)
        masks = batch.base_node_masks

        losses = compute_losses(similarity_matrices, masks)
        loss = losses.mean()
        loss.backward()
        torch.nn.utils.clip_grad_value_(model.parameters(), config.grad_clip)
        optimizer.step()
        return float(loss.data)

    for epoch in range(config.epochs):
        run.log({"learning_rate": scheduler.get_last_lr()[0]}, epoch)

        # Logging
        logging_start_time = time.time()
        if epoch % config.log_frequency == 0:
            model.eval()
            train_metrics = {
                f"{k}/train": v
                for (k, v) in compute_metrics(model, train_loader, config.device).items()
            }
            val_metrics = {
                f"{k}/val": v
                for (k, v) in compute_metrics(model, val_loader, config.device).items()
            }
            run.log(train_metrics, epoch)
            run.log(val_metrics, epoch)

        run.log({"log_time": time.time() - logging_start_time}, epoch)

        # Training loop
        training_start_time = time.time()
        model.train()
        batch: GADatasetBatch
        for i, batch in enumerate(train_loader):
            batch = batch.to(config.device)

            model.zero_grad()
            forward_pass(model, batch)

        scheduler.step()
        run.log({"train_time": time.time() - training_start_time}, epoch)

    checkpoint_path = os.path.join(
        wandb.run.dir, "checkpoints/final_checkpoint.safetensors"
    )
    os.makedirs(os.path.dirname(checkpoint_path), exist_ok=True)
    save_model(model, checkpoint_path)
    run.save(checkpoint_path, base_path=wandb.run.dir)
    run.finish()
