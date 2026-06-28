import subprocess
import sys
import threading
import time
from pathlib import Path

def run_naabu(domain):
    
    input_file = Path(f"{domain}_dnsx_results.txt")
    output_file = Path(f"{domain}_naabu_results.txt")

   
    if not input_file.exists():
        print(f"Input file {input_file} does not exist. Please run dnsx first.")
        return

    
    with open(output_file, "w") as f:
        subprocess.run(["naabu", "-l", str(input_file), "-top-ports", "1000", "-ep", "22"], stdout=f)
