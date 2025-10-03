from jaxtyping import Float
from jaxtyping import Int
from rdkit import Chem
from rdkit.Chem import AllChem
import torch
import torch_geometric.data as pyg_data
import torch_geometric.utils as pyg_utils


def smiles_to_minimal_graph(
    smiles: str,
    *,
    sanitize: bool = False,
    add_hs: bool = False,
    compute_coords: bool = True,
) -> pyg_data.Data:
    """
    Convert a SMILES string into a minimal PyG graph.

    Parameters
    - smiles: SMILES string to parse.
    - sanitize: Whether to sanitize the molecule during parsing.
    - add_hs: Whether to explicitly add hydrogens before building the graph.
    - compute_coords: If True, compute 2D coordinates and store in `data.pos`.

    Returns
    - data: `pyg_data.Data` with fields:
        - edge_index: Int[Tensor, "2 num_edges"]
        - num_nodes: int
        - pos (optional): Float[Tensor, "num_nodes 2"] when `compute_coords=True`
    """
    mol = Chem.MolFromSmiles(smiles, sanitize=sanitize)
    if mol is None:
        raise ValueError(f"Invalid SMILES provided: {smiles!r}")

    if add_hs:
        mol = Chem.AddHs(mol, addCoords=False)

    # Build unweighted adjacency (boolean)
    adjacency_matrix = Chem.GetAdjacencyMatrix(mol, useBO=False)
    adjacency_tensor = torch.tensor(adjacency_matrix, dtype=torch.bool)

    edge_index: Int[torch.Tensor, "2 num_edges"]
    edge_index, _ = pyg_utils.dense_to_sparse(adjacency_tensor)

    # Prepare data kwargs and optional coordinates (2D depiction)
    data_kwargs: dict = {
        "edge_index": edge_index.long(),
        "num_nodes": int(adjacency_tensor.shape[0]),
    }

    if compute_coords:
        try:
            AllChem.Compute2DCoords(mol)
            conformer = mol.GetConformer()
            xy = []
            for i, _atom in enumerate(mol.GetAtoms()):
                p = conformer.GetAtomPosition(i)
                xy.append([p.x, p.y])
            pos: Float[torch.Tensor, "num_nodes 2"] = torch.tensor(
                xy, dtype=torch.float32
            )
            data_kwargs["pos"] = pos
        except Exception as e:  # noqa: BLE001
            # Re-raise the exception instead of silently falling back
            raise RuntimeError(
                f"Failed to compute 2D coordinates for molecule: {smiles!r}"
            ) from e
    data = pyg_data.Data(**data_kwargs)
    return data
