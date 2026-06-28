import subprocess
import sys
import threading
import time
from pathlib import Path

def run_subfinder(domain):
    
    output_file = Path(f"{domain}_subdomains.txt")

    
    with open(output_file, "w") as f:
        subprocess.run(["subfinder", "-d", domain, "-all"], stdout=f)

    
