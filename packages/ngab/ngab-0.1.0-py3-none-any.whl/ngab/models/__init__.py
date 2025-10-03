"""
Graph neural network models built on PyTorch Geometric.

Available models
----------------
- GCN: Graph Convolutional Network (stack of `GCNConv`).
- GAT: Graph Attention Network (stack of `GATConv`).
- GATv2: Graph Attention Network v2 (stack of `GATv2Conv`).
- GatedGCN: Gated Graph Convolution (stack of `GatedGraphConv`).
- GIN: Graph Isomorphism Network (stack of `GINConv` with MLP).
"""

__all__ = ["GAT", "GatedGCN", "GATv2", "GCN", "GIN", "TAGCN", "SGC", "GraphGPS", "PNA", "PAN"]

from ._gat import GAT
from ._gated_gcn import GatedGCN
from ._gatv2 import GATv2
from ._gcn import GCN
from ._gin import GIN
from ._graphgps import GraphGPS
from ._pan import PAN
from ._pna import PNA
from ._sgc import SGC
from ._taggcn import TAGCN
