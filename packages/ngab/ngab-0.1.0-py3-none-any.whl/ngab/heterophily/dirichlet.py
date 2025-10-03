import torch


def dirichlet(x, edge_index, batch):
   # x: [N, d]
   # batch: [N], graph id per node
   del edge_index  # unused in this computation

   if x.numel() == 0:
      return torch.empty(0, dtype=x.dtype, device=x.device)

   eps = 1e-12
   # Normalize features (cosine similarity)
   norms = x.norm(dim=1, keepdim=True).clamp_min(eps)
   x_norm = x / norms

   # Group nodes by batch id
   num_graphs = int(batch.max().item()) + 1 if batch.numel() > 0 else 0
   if num_graphs == 0:
      return torch.empty(0, dtype=x.dtype, device=x.device)

   counts = torch.bincount(batch, minlength=num_graphs)

   # Sort by batch to make contiguous blocks
   order = torch.argsort(batch)
   x_sorted = x_norm[order]

   # Pad into [G, max_len, d]
   splits = torch.split(x_sorted, counts.tolist())
   padded = torch.nn.utils.rnn.pad_sequence(splits, batch_first=True, padding_value=0.0)
   # Similarity matrices per graph: [G, max_len, max_len]
   sims = torch.bmm(padded, padded.transpose(1, 2)).abs()

   # Build masks for valid nodes and exclude diagonals from numerator
   device = x.device
   max_len = padded.size(1)
   valid = (torch.arange(max_len, device=device)[None, :] < counts[:, None])
   pair_mask = valid[:, :, None] & valid[:, None, :]
   eye = torch.eye(max_len, device=device, dtype=torch.bool)[None, :, :]
   off_diag_mask = pair_mask & ~eye

   # Numerator: sum over |cos| for i != j within each graph
   numerator = (sims * off_diag_mask.to(sims.dtype)).sum(dim=(1, 2))

   # Denominator: m^2 to match previous mean over full matrix including 0-diagonal
   m = counts.to(sims.dtype)
   denom = (m * m).clamp_min(1)

   # For graphs with m <= 1, define value as 0
   per_graph = torch.where((counts > 1), numerator / denom, numerator.new_zeros(counts.size(), dtype=sims.dtype))

   return per_graph.mean()