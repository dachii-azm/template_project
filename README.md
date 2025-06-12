# template_project
research project template

## Installation
### Local Installation
```
conda create -n prj python=3.xx
```

```
pip install -r requirements.txt
```

```
python -m pip install -e .
```


## Usage

### Basic Usage
1. Load configuration:
```python
# Get default config
cfg = get_cfg()

# Or load specific config
cfg = get_cfg(pt.get_config("demo.yaml"))
```

2. Get modules from registry:
```python
# List all available modules
registry.get_value_list()

# Get specific module (e.g., dataloader)
dataloader = registry.get_value(key="dataloader", name="example")
model = registry.get_value(key="model", name="example")
```

For more detailed examples, please refer to the `notebook/example.ipynb`.

