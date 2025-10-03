from jaxtyping import Float
import torch
import torch.nn.functional as F
import torch_geometric.data as pyg_data
from torch_geometric.nn import GatedGraphConv
from torch_geometric.nn import GCNConv
from torch_geometric.nn import GraphNorm


class GatedGCN(torch.nn.Module):
    def __init__(
        self,
        in_features: int,
        features: int,
        out_features: int,
        layers: int,
    ) -> None:
        super().__init__()
        assert layers >= 1, "Number of layers must be greater than or equal to 1"

        self.in_features = in_features

        self.layer0 = GCNConv(
            in_channels=in_features, out_channels=features, aggr="add"
        )
        self.norm0 = GraphNorm(features)
        self.layers = torch.nn.ModuleList(
            [
                GatedGraphConv(out_channels=features, num_layers=2)
                for _ in range(layers - 1)
            ]
        )
        self.gns = torch.nn.ModuleList(
            [GraphNorm(features) for _ in range(layers - 1)]
        )
        self.linear = torch.nn.Linear(features, out_features)

    def forward(
        self,
        data: pyg_data.Data,
    ) -> Float[torch.Tensor, "num_nodes out_features"]:
        assert getattr(data, "edge_index", None) is not None, (
            "GatedGCN.forward expects 'data.edge_index' to be present"
        )
        assert getattr(data, "batch", None) is not None, (
            "GatedGCN.forward expects 'data.batch' to be present"
        )
        if data.x is None:
            x = torch.ones(
                (data.num_nodes, self.in_features),
                dtype=torch.float,
                device=data.edge_index.device,
            )
        else:
            x = data.x
        edge_index = data.edge_index
        x = self.layer0(x, edge_index)
        x = self.norm0(x, data.batch)
        for i in range(len(self.layers)):
            x = x + self.gns[i](F.gelu(self.layers[i](x, edge_index)), data.batch)
        x = self.linear(x)

        return x
