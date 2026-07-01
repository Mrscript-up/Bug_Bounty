from MODULES.run_cmd import run_cmd
import os

def katana_paths(domain):
    run_cmd(f"katana {domain} -d 5 -fs fqdn >> paths_by_katana")
    run_cmd("cat paths_by_katana | sort -u | httpx >> paths_by_httpx_katana4")
    os.remove("paths_by_katana")
