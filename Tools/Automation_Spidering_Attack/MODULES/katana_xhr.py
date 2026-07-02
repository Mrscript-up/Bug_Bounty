from MODULES.run_cmd import run_cmd
import os

def katana_xhr(domain):
    run_cmd(f"katana -u {domain} -xhr -d 5 -aff >> xhr_files_by_katana")
    run_cmd("cat xhr_files_by_katana | sort -u | httpx >> xhr_files_by_httpx_katana2")
    os.remove("xhr_files_by_katana")
