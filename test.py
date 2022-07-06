import torch 
import torch.nn as nn
import numpy as np
a = torch.from_numpy(np.random.random((64,128, 5)).astype(np.float32)).repeat(64, 128, 5)
#a = torch.tensor([1, 2, 3, 4, 5]).repeat(1,1)
b = torch.multiply(a, a.T)
print(b)