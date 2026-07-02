from MODULES.run_cmd import run_cmd
import sys
from pathlib import Path
import time
from goapiser.gospider import start_gospider

def greps(domain):
    try:
        run_cmd(f"grep '\.js' /gospider/{domain}_resolve_gospider.txt >> /gospider/files/js.files") # just js files
        run_cmd(f"grep '=' /gospider/{domain}_resolve_gospider.txt >> /gospider/parametr/parametr.txt") # just parametrs
        run_cmd(f"grep -Eo 'https?://[^? ]+' /gospider/{domain}_resolve_gospider.txt >> /gospider/paths/paths.txt") # just paths
        run_cmd(f"grep -E '\.(bak|old|zip|tar|gz|sql|env|config|yml|yaml|xml|php|asp|aspx|jsp|git|cgi|cfm|do|action|json|js.map|map|xml|html|css|svg|txt|conf|log|md)$' /gospider/{domain}_resolve_gospider.txt >> /gospider/files/files.txt") # importent files
    except:
        print("[~] Error...")
        sys.exit()
