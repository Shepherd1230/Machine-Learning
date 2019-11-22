from __future__ import print_function
import torch

x=torch.ones(5,3)
print(x)

if torch.cuda.is_available():
    device = torch.device("cuda:1")          # a CUDA device object
    y = torch.ones_like(x, device=device)  # directly create a tensor on GPU
    x = x.to(device)                       # or just use strings ``.to("cuda")``
    z = x + y
    print(z)
    # print(z.to("cpu", torch.double))       # ``.to`` can also change dtype together!
    print(z.to("cpu"))
