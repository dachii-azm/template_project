import torch.nn as nn

from prj.utils.registry import registry

#implement example model
@registry.register_values(key="model", name="example")
class ExampleModel(nn.Module):
    def __init__(self):
        super(ExampleModel, self).__init__()
        self.conv1 = nn.Conv2d(1, 64, 3, padding=1)
    
    def forward(self, x):
        x = self.conv1(x)
        return x