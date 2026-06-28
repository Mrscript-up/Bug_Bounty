import subprocess
import sys
import threading
import time
from pathlib import Path


def run_dnsx(domain):
    
    input_file = Path(f"{domain}_subdomains.txt")
    output_file = Path(f"{domain}_dnsx_results.txt")

    
    if not input_file.exists():
        print(f"Input file {input_file} does not exist. Please run subfinder first.")
        return

    
    with open(output_file, "w") as f:
        subprocess.run(["dnsx", "-l", str(input_file)], stdout=f)

    
