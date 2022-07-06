import torch
import torch.nn as nn
import torch.nn.functional as F
from kernel_activation.kaf import KAF

class ELMK:
    def __init__(self, input_size, output_size) -> None:
        self.input_size = input_size
        self.output_size = output_size 
        self.mat1 = nn.Parameter(torch.Tensor(input_size, input_size), requires_grad=False)
        self.KAF = KAF(input_size)
        self.mat2 = nn.Parameter(torch.Tensor(input_size, output_size))
    def forward(self, x):
        x = torch.matmul(x, self.mat1)
        x = self.KAF(x)
        x = torch.matmul(x, self.mat2) 
        return input
