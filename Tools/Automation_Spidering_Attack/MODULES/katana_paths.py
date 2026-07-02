from MODULES.run_cmd import run_cmd
import os
import re
def katana_paths(domain):
    dom = domain
    dom2 = re.escape(dom)
    run_cmd(f"katana {domain} -d 5 -fs fqdn >> paths_by_katana")
    run_cmd(f'sort -u paths_by_katana | grep -E "^https?://([^/]+\\.)?{dom2}" | httpx > paths_by_httpx_katana4')
    os.remove("paths_by_katana")
