import subprocess
import sys
import threading
import time
from pathlib import Path

def run_httpx(domain):
   
    input_file = Path(f"{domain}_httpx_results.txt")
    output_file = Path(f"{domain}_httpx_final_results.txt")

   
    if not input_file.exists():
        print(f"Input file {input_file} does not exist. Please run sort_httpx first.")
        return

    
    with open(output_file, "w") as f:
        subprocess.run(["httpx", "-l", str(input_file), "-title", "-sc", "-cl", "-location"], stdout=f)

    
