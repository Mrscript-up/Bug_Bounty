import subprocess
import sys
import threading
import time
from pathlib import Path

def run_sort_httpx(domain):
    
    input_file = Path(f"{domain}_naabu_results.txt")
    output_file = Path(f"{domain}_httpx_results.txt")

    
    if not input_file.exists():
        print(f"Input file {input_file} does not exist. Please run naabu first.")
        return

    
    with open(output_file, "w") as f:
        sort_proc = subprocess.Popen(
            ["sort", "-u", str(input_file)],
            stdout=subprocess.PIPE
        )

        subprocess.run(
            ["httpx"],
            stdin=sort_proc.stdout,
            stdout=f
        )
