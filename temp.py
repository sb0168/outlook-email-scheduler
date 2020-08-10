import torch
from torch.nn import functional as F
from torch import nn
import numpy as np

f = np.array([1, 2, 1], dtype=np.float32)
f = f[:, np.newaxis] * f[np.newaxis, :]
f /= np.sum(f)
kernel = torch.Tensor(f).view(1, 1, 3, 3).repeat(64, 1, 1, 1)
print(len(kernel))