import subprocess
import sys
import threading
import time
from pathlib import Path

def run_delete_old_files(domain):
    
    dnsx_file = Path(f"{domain}_dnsx_results.txt")
    subdomains_file = Path(f"{domain}_subdomains.txt")

    
    for file in [dnsx_file,subdomains_file]:
        if file.exists():
            file.unlink()
            print(f"Deleted {file}")
        else:
            print(f"{file} does not exist and cannot be deleted.")
