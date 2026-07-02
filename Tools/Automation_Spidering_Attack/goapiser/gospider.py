from MODULES.run_cmd import run_cmd
import sys
from pathlib import Path
import os
import re
def start_gospider(domain):
    try:
        dom = f"{domain}"
        escaped = re.escape(dom)
        run_cmd(f"gospider -s {domain} -d 2 -q | sort -u >> resoulve_gospider1.txt")
        run_cmd(f'grep -E grep -E "^https?://([a-zA-Z0-9_-]+\.)*{escaped}(/|$)" resoulve_gospider1.txt | httpx >> /gospider/{domain}_resolve_gospider.txt')
        os.remove("resoulve_gospider1.txt")
    except:
        print('[~] Error...')
        sys.exit()
