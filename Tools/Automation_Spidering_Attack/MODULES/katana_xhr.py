from MODULES.run_cmd import run_cmd
import os
import re
def katana_xhr(domain):
    dom = domain
    dom2 = re.escape(dom)
    run_cmd(f"katana -u {domain} -xhr -d 5 -aff > xhr_files_by_katana")
    run_cmd(f'sort -u xhr_files_by_katana | grep -E "^https?://([^/]+\\.)?{dom2}" | httpx > xhr_files_by_httpx_katana2')
    os.remove("xhr_files_by_katana")
