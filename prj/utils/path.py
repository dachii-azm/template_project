import importlib.resources

# import your file here
import prj.configs.settings

def get_path(pkg, path=None, ext=".yaml", default="demo"):
    if path is None:
        path = path + ext if ext not in path else path
    else:
        path = default + ext
    ctx = importlib.resources.path(pkg, path)
    with ctx as c:
        file = c
    return file

def get_config(path=None):
    return get_path(prj.configs.settings, path=path, ext=".yaml", default="demo")
