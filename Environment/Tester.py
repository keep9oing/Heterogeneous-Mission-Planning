from utils import Batch_cal_cost
import torch

cost = Batch_cal_cost(torch.Tensor([[0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000],[0.2233, 0.6920, 0.0579, 0.2233, 0.6920, 0.0000, 0.0000, 1.0000]]),
                      torch.Tensor([[0.9517, 0.2221, 0.0000, 0.9517, 0.2221, 0.0000, 1.0000, 0.0000],[0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000]]),
                      2)[:,None]
print(cost)
