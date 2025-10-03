"""
Module providing random operations linked to graphs.
"""

import random
from typing import Literal

import torch
import torch_geometric.data as pyg_data
import torch_geometric.utils as pyg_utils


def erdos_renyi(
    nb_graphs: int,
    order: int,
    p: float,
    *,
    directed: bool = False,
    self_loops: bool | None = False,
) -> pyg_data.Batch:
    """
    Generate a batch of random Erdős–Rényi graphs.

    ### Arguments:
    - nb_graphs: Number of graphs to generate.
    - order: number of nodes in each graph.
    - p: edge probability.
    - directed: if false the graph will be undirected.
    - self_loops: if None, there might be self loops, if False all self loops will be removed, if true they will be added.
    """

    assert 0.0 <= p <= 1, "'p' must be between 0 and 1"

    batch = torch.empty(size=(nb_graphs, order, order), dtype=torch.bool).bernoulli_(p)

    if not directed:
        tri_up = batch.triu(0)
        batch = tri_up | tri_up.transpose(1, 2)

    if self_loops is not None:
        idx = torch.arange(order, device=batch.device)
        if self_loops:
            batch[:, idx, idx] = True
        else:
            batch[:, idx, idx] = False

    edge_indices, _ = pyg_utils.dense_to_sparse(batch)
    batch_vector = torch.arange(
        nb_graphs, device=edge_indices.device
    ).repeat_interleave(order)
    data = pyg_data.Batch(
        edge_index=edge_indices, num_nodes=order * nb_graphs, batch=batch_vector
    )
    return data


@torch.vmap
def __graph_normalization(
    adj_matrix: torch.Tensor, mask: torch.BoolTensor
) -> torch.Tensor:
    """
    density/(1 - density) with the same shape as adj_matrix.
    """
    order = mask.sum()
    avg_degree = adj_matrix.masked_fill(mask.logical_not(), 0).float().sum() / (
        order - 1
    )
    degrees_matrix = torch.empty_like(adj_matrix, dtype=torch.float)
    degrees_matrix.fill_(avg_degree)
    return (degrees_matrix / (order - 1 - degrees_matrix)).nan_to_num(0, 1)


def bernoulli_corruption(
    graphs: pyg_data.Batch,
    noise: float,
    *,
    directed: bool = False,
    self_loops: bool = False,
    type: Literal["add", "add_remove"],
) -> pyg_data.Batch:
    """
    Apply a Bernoulli corruption to each graph in the batch.

    ### Arguments:
    - batch: graph batch to corrupt
    - noise: amount of noise to apply
    - directed: if false, the perturbation will be symmetric
    - self_loops: if false, will not add or remove self loops
    - type: whether to add and remove edges or just to add them.
    """
    assert 0.0 <= noise <= 1, "'noise' must be between 0 and 1"

    device = graphs.edge_index.device
    adj_matrices = pyg_utils.to_dense_adj(graphs.edge_index, batch=graphs.batch).bool()
    _, masks = pyg_utils.to_dense_batch(graphs.batch, graphs.batch)
    normalization_tensor = __graph_normalization(adj_matrices, masks)

    if type == "add_remove":
        edge_noise = torch.empty_like(
            adj_matrices, dtype=torch.bool, device=device
        ).bernoulli_(noise)
    elif type == "add":
        edge_noise = torch.zeros_like(adj_matrices, dtype=torch.bool, device=device)

    nonedge_noise = torch.empty_like(
        adj_matrices, dtype=torch.bool, device=device
    ).bernoulli_(torch.clip(noise * normalization_tensor, 0, 1))

    if not directed:
        tri_up = edge_noise.triu()
        edge_noise = tri_up | tri_up.transpose(1, 2)

        tri_up = nonedge_noise.triu()
        nonedge_noise = tri_up | tri_up.transpose(1, 2)

    if not self_loops:
        idx = torch.arange(adj_matrices.shape[1], device=device)
        edge_noise[:, idx, idx] = False
        nonedge_noise[:, idx, idx] = False

    corrupted_batch = adj_matrices.clone()
    corrupted_batch[adj_matrices & edge_noise] = False
    corrupted_batch[torch.logical_not(adj_matrices) & nonedge_noise] = True

    sparse_graphs: list[pyg_data.Data] = []
    for i in range(corrupted_batch.shape[0]):
        order = masks[i].sum().item()
        edge_index = corrupted_batch[i, :order, :order].nonzero(as_tuple=False).t()
        sparse_graphs.append(
            pyg_data.Data(
                edge_index=edge_index,
                num_nodes=order,
            )
        )
    return pyg_data.Batch.from_data_list(sparse_graphs)


def node_sub_sample(
    graph: pyg_data.Data, nodes_sample: torch.LongTensor
) -> pyg_data.Data:
    """
    Returns the graph only containing the nodes in `nodes_sample`.
    """
    mask = torch.logical_and(
        torch.isin(graph.edge_index[0], nodes_sample),
        torch.isin(graph.edge_index[1], nodes_sample),
    )

    new_senders = graph.edge_index[0][mask]
    new_receivers = graph.edge_index[1][mask]

    for i, v in enumerate(torch.unique(torch.cat([new_senders, new_receivers]))):
        new_senders[new_senders == v] = i
        new_receivers[new_receivers == v] = i

    return pyg_data.Data(
        edge_index=torch.stack([new_senders, new_receivers]),
        num_nodes=max(int(torch.max(new_senders)), int(torch.max(new_receivers))) + 1,
    )


def uniform_sub_sampling(
    graph: pyg_data.Data, n: int, num_nodes: int
) -> pyg_data.Batch:
    """
    Randomly sample num_nodes nodes from the graph and extract the graph spanning on those nodes.
    Repeat the process n times to build a batch.
    """
    order = graph.num_nodes
    device = graph.edge_index.device

    graphs_l: list[pyg_data.Data] = []
    for _ in range(n):
        sampled_indices = torch.randperm(order, device=device)[:num_nodes]
        graphs_l.append(node_sub_sample(graph, sampled_indices))

    return pyg_data.Batch.from_data_list(graphs_l)


def bfs_sub_sampling(
    graph: pyg_data.Data, n: int, num_nodes: int, *, p: float = 1
) -> pyg_data.Batch:
    """
    Sample with the Breadth First Search Method num_nodes nodes from the graph and extract the graph spanning on those nodes.
    Repeat the process n times to build a batch.
    """
    assert 0.0 < p <= 1.0, "'p' must be in (0, 1]"

    device = graph.edge_index.device
    (senders, receivers) = graph.edge_index[0], graph.edge_index[1]
    graphs_l: list[pyg_data.Data] = []

    for _ in range(n):
        base_node = random.randint(0, graph.num_nodes - 1)
        kept_nodes: set[int] = {base_node}
        while len(kept_nodes) < num_nodes:
            new_nodes = set(
                receivers[
                    torch.isin(
                        senders,
                        torch.tensor(list(kept_nodes), dtype=torch.long, device=device),
                    )
                ].tolist()
            ).difference(kept_nodes)
            if len(new_nodes) == 0:
                kept_nodes.add(random.randint(0, graph.num_nodes - 1))
            else:
                new_nodes = random.sample(
                    sorted(new_nodes), max(int(p * len(new_nodes)), 1)
                )
                if len(new_nodes) + len(kept_nodes) < num_nodes:
                    kept_nodes = kept_nodes.union(new_nodes)
                else:
                    kept_nodes = kept_nodes.union(
                        random.sample(sorted(new_nodes), num_nodes - len(kept_nodes))
                    )
        graphs_l.append(
            node_sub_sample(
                graph,
                torch.tensor(sorted(kept_nodes), dtype=torch.long, device=device),
            )
        )

    return pyg_data.Batch.from_data_list(graphs_l)
