from MODULES.run_cmd import run_cmd
import os

def katana_js(domain):
    run_cmd(f"katana -u {domain} -jc -jsl -d 5 >> js.files_by_katana")
    run_cmd("cat js.files_by_katana | sort -u | httpx >> js.files_by_httpx_katana1")
    os.remove("js.files_by_katana")
