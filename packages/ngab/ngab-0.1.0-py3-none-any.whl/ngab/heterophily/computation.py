import torch
import torch.utils.data

from .._train_utils import GADatasetBatch


def run(
    model: torch.nn.Module,
    loader: torch.utils.data.DataLoader[GADatasetBatch],
) -> tuple[dict[int, float], dict[int, float]]:
    """
    Execute ``model`` on every graph pair in ``dataset`` and return collected
    per-layer means for energies and noise robustness.

    The model is expected to expose ``energies`` and ``noise_robustness``
    dictionaries mapping layer indices to a list of scalar tensors. Both are
    cleared before running and returned as Python floats grouped by layer.
    """
    # Clear previously accumulated energies, if any
    model.energies = {layer: [] for layer in model.energies.keys()}
    # Clear previously accumulated robustness, if any
    if hasattr(model, "noise_robustness"):
        model.noise_robustness = {
            layer: [] for layer in model.noise_robustness.keys()
        }
    else:
        # Initialize robustness dict aligned with energies layers if missing
        model.noise_robustness = {layer: [] for layer in model.energies.keys()}

    try:
        model_device = next(model.parameters()).device
    except StopIteration:
        model_device = torch.device("cpu")

    model.eval()
    with torch.no_grad():
        batch: GADatasetBatch
        for batch in loader:
            batch = batch.to(model_device)
            model(batch.base_graphs, batch.corrupted_graphs)

    # Compute mean energies per layer as plain floats
    energy_means: dict[int, float] = {}
    for layer, energy_list in model.energies.items():
        values = [float(e.detach().cpu().item()) for e in energy_list]
        energy_means[int(layer)] = (
            (sum(values) / len(values)) if len(values) > 0 else 0.0
        )

    # Compute mean noise robustness per layer as plain floats
    robustness_means: dict[int, float] = {}
    for layer, robustness_list in model.noise_robustness.items():
        values = [float(r.detach().cpu().item()) for r in robustness_list]
        robustness_means[int(layer)] = (
            (sum(values) / len(values)) if len(values) > 0 else 0.0
        )

    return energy_means, robustness_means
