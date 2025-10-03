from jaxtyping import Float
import torch
import torch.nn.functional as F
import torch_geometric.data as pyg_data
from torch_geometric.nn import GATConv
from torch_geometric.nn import GCNConv
from torch_geometric.nn import GraphNorm

from .dirichlet import dirichlet


class GAT(torch.nn.Module):
    def __init__(
        self,
        in_features: int,
        features: int,
        out_features: int,
        layers: int,
        heads: int,
    ) -> None:
        super().__init__()
        assert layers >= 3, "Number of layers must be greater than or equal to 3"
        assert features % heads == 0, "Features must be divisible by heads"

        self.in_features = in_features

        self.layer0 = GCNConv(
            in_channels=in_features, out_channels=features, aggr="add"
        )
        self.norm0 = GraphNorm(features)
        self.layers = torch.nn.ModuleList(
            [
                GATConv(features, features // heads, heads=heads)
                for _ in range(layers - 2)
            ]
        )
        self.gns = torch.nn.ModuleList([GraphNorm(features) for _ in range(layers - 2)])
        self.linear = torch.nn.Linear(features, out_features)

        self.energies = {i: [] for i in range(layers+1)}
        self.noise_robustness = {i: [] for i in range(layers+1)}

    def forward(
        self,
        data1: pyg_data.Data,
        data2: pyg_data.Data,
    ) -> Float[torch.Tensor, "num_nodes out_features"]:
        assert getattr(data1, "edge_index", None) is not None, (
            "GAT.forward expects 'data1.edge_index' to be present"
        )
        assert getattr(data1, "batch", None) is not None, (
            "GAT.forward expects 'data1.batch' to be present"
        )
        assert getattr(data2, "edge_index", None) is not None, (
            "GAT.forward expects 'data2.edge_index' to be present"
        )
        assert getattr(data2, "batch", None) is not None, (
            "GAT.forward expects 'data2.batch' to be present"
        )

        if data1.x is None:
            x1 = torch.ones(
                (data1.num_nodes, self.in_features),
                dtype=torch.float,
                device=data1.edge_index.device,
            )
        else:
            x1 = data1.x

        if data2.x is None:
            x2 = torch.ones(
                (data2.num_nodes, self.in_features),
                dtype=torch.float,
                device=data2.edge_index.device,
            )
        else:
            x2 = data2.x

        edge_index1 = data1.edge_index
        edge_index2 = data2.edge_index
        batch1 = data1.batch
        batch2 = data2.batch

        # Track energy on first input to match existing semantics
        self.energies[0].append(dirichlet(x1, edge_index1, batch1))
        # Robustness
        sim = torch.abs(F.cosine_similarity(x1, x2, dim=-1)).mean()
        self.noise_robustness[0].append(sim)

        # Layer 0
        x1 = self.layer0(x1, edge_index1)
        x1 = self.norm0(x1, batch1)
        x2 = self.layer0(x2, edge_index2)
        x2 = self.norm0(x2, batch2)



        # GAT layers
        for i in range(len(self.layers)):
            # Energy before applying layer i (matching previous behavior)
            self.energies[i + 1].append(dirichlet(x1, edge_index1, batch1))
            # Robustness
            sim_i = torch.abs(F.cosine_similarity(x1, x2, dim=-1)).mean()
            self.noise_robustness[i + 1].append(sim_i)
            x1 = x1 + self.gns[i](F.gelu(self.layers[i](x1, edge_index1)), batch1)
            x2 = x2 + self.gns[i](F.gelu(self.layers[i](x2, edge_index2)), batch2)
        
        self.energies[len(self.layers) + 1].append(dirichlet(x1, edge_index1, batch1))
        sim_i = torch.abs(F.cosine_similarity(x1, x2, dim=-1)).mean()
        self.noise_robustness[len(self.layers) + 1].append(sim_i)

        # Final linear projection for first input (return shape unchanged)
        x1 = self.linear(x1)
        x2 = self.linear(x2)

        self.energies[len(self.layers)+2].append(dirichlet(x1, edge_index1, batch1))
        sim_i = torch.abs(F.cosine_similarity(x1, x2, dim=-1)).mean()
        self.noise_robustness[len(self.layers)+2].append(sim_i)