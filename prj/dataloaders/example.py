import torch
from torch.utils.data import Dataset

from prj.utils.registry import registry
from prj.utils.logging import logger

@registry.register_values(key="dataloader", name="example")
class ExampleDataloader(Dataset):
    def __init__(self, config, array):
        self.config = config
        self.array = array

    def __len__(self):
        return len(self.array)

    def __getitem__(self, idx):
        return self.array[idx]

