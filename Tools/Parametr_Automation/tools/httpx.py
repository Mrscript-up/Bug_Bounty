import sys
import subprocess
from pathlib import Path

def run_httpx(target):
    # Define the command to run
    command = f"httpx -l qs.output -content-length -silent -sc -hash mmh3 >> httpx_output.txt"
    
    # Run the command using subprocess
    try:
        subprocess.run(command, shell=True, check=True)
        
    except subprocess.CalledProcessError as e:
        print(f"[1] An error occurred while running httpx: {e}") 
    
    command2 = f"httpx -l qs2_bb1b.output -content-length -silent -sc -hash mmh3 >> httpx_bb1b_output.txt"

    try:
        subprocess.run(command2, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"[2] An error occurred while running httpx: {e}")
