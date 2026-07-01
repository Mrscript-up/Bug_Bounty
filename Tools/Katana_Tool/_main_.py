# imports:
import subprocess
import time
from pathlib import Path
from MODULES.run_cmd import run_cmd
from MODULES.katana_js import katana_js
from MODULES.katana_xhr import katana_xhr
from MODULES.katana_standard import katana_standard
from MODULES.katana_paths import katana_paths
from MODULES.merge_all import merge_all
from MODULES.grep_sensitive import grep_sensitive
from MODULES.extract_dirs import extract_dirs
from MODULES.extract_params import extract_params
from MODULES.split_file_types import split_file_types

# CONFIG:
DELAY = 3  # seconds for per command
OUTPUT_DIR = Path("files_and_importent")
FILES_DIR = OUTPUT_DIR / "files"

#/\/\/\/\/\/\/\/\/\
def ensure_dirs():
    OUTPUT_DIR.mkdir(exist_ok=True)
    FILES_DIR.mkdir(exist_ok=True)
#\/\/\/\/\/\/\/\/\/

# MAIN:
def main(domain):
    ensure_dirs()

    katana_js(domain)
    katana_xhr(domain)
    katana_standard(domain)
    katana_paths(domain)

    merge_all()

    grep_sensitive()
    extract_dirs()
    extract_params()
    split_file_types()

    print("\n[~] Done. Results saved in files_and_importent/")


if __name__ == "__main__":
    domain = input("[~] Enter domain: ")
    main(domain)
