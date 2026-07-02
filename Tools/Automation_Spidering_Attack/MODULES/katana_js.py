from MODULES.run_cmd import run_cmd
import os
import re 

def katana_js(domain):
    dom = f"{domain}"
    escaped_dom = re.escape(dom)
    run_cmd(f"katana -u {domain} -jc -jsl -d 5 > js.files_by_katana")
    run_cmd(f'sort -u js.files_by_katana | grep -E "^https?://([^/]+\\.)?{escaped_dom}" | httpx > js.files_by_httpx_katana1')
    os.remove("js.files_by_katana")
