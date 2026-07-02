from MODULES.run_cmd import run_cmd
import os
import re
def katana_standard(domain):
    dom = domain
    dom2 = re.escape(dom)
    run_cmd(f"katana -u {domain} -silent > katana_standard")
    run_cmd(f'sort -u katana_standard | grep -E "^https?://([^/]+\\.)?{dom2}" | httpx > katana_httpx_standard3')
    os.remove("katana_standard")
