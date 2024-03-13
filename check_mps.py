# GPU acceleration
import torch
if torch.backends.mps.is_available():
    mps_device = torch.device("mps")
    x = torch.ones(1, device=mps_device)
    print(x)  # This should show tensor([1.], device='mps:0')
else:
    print("MPS device not found.")
