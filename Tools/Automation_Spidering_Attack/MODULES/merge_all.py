from MODULES.run_cmd import run_cmd
import os

def merge_all(domain):
    run_cmd(
        f"""cat js.files_by_httpx_katana1 \
        xhr_files_by_httpx_katana2 \
        katana_httpx_standard3 \
        paths_by_httpx_katana4 | sort -u | grep -E '(^|\\.){domain}' >> all_things_in_katana.txt"""
    )

    os.remove("js.files_by_httpx_katana1")
    os.remove("xhr_files_by_httpx_katana2")
    os.remove("katana_httpx_standard3")
    os.remove("paths_by_httpx_katana4")
