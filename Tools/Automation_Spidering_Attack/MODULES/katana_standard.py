from MODULES.run_cmd import run_cmd
import os

def katana_standard(domain):
    run_cmd(f"katana -u {domain} -silent >> katana_standard")
    run_cmd("cat katana_standard | sort -u | httpx >> katana_httpx_standard3")
    os.remove("katana_standard")
