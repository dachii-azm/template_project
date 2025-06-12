import argparse

from torch.utils.data import DataLoader

from prj.libs.preprocess import get_example_array
from prj.configs.defaults import get_cfg
from prj.utils.registry import registry
from prj.utils.logging import logger
import prj.utils.path as pt

def main(cfg_path=None):
    if cfg_path is None:
        cfg = get_cfg(pt.get_config("demo.yaml"))
    else:
        cfg = get_cfg(args.cfg)

    array = get_example_array()

    dataset = registry.get_value(key="dataloader", name="example")(cfg, array)
    dataloader = DataLoader(dataset, batch_size=cfg.run.batch_size, shuffle=True)

    model = registry.get_value(key="model", name="example")()
    model.eval()

    for batch in dataloader:
        result = model(batch)
        print(result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--cfg", type=str, default=None)
    args = parser.parse_args()
    main(args.cfg)