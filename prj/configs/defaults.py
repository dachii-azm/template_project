import os
from yacs.config import CfgNode as CN

_C = CN()

_C.input=CN()


_C.output=CN()


_C.run=CN()
_C.run.mode="test" # test, train, eval
_C.run.seed=42
_C.run.device="cuda"
_C.run.num_gpus=1
_C.run.batch_size=128

_C.run.train=CN()
_C.run.train.num_workers=4
_C.run.train.num_gpus=1
_C.run.train.num_epochs=100
_C.run.train.learning_rate=0.001
_C.run.train.weight_decay=0.0001
_C.run.train.resume_from_checkpoint=None

_C.run.test=CN()


_C.model=CN()
_C.model.name=""

_C.model.loss=CN()
_C.model.loss.name=""

def get_cfg(filename=None):
    cfg = _C.clone()
    if filename is not None:
        if os.path.isfile(filename):
            cfg.merge_from_file(filename)
        else:
            cfg.merge_from_file(filename+".yaml")
    return cfg