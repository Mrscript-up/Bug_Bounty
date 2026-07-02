import sys
import subprocess
from pathlib import Path
from MODULES.run_cmd import run_cmd

def run_httpx():
    # Define the command to run
    command = f"httpx -l /paramspider/qs.output -content-length -silent -sc -hash mmh3 >> /paramspider/httpx_output.txt"
    
    # Run the command using subprocess
    try:
        run_cmd(command)
    except subprocess.CalledProcessError as e:
        print(f"[1] An error occurred while running httpx: {e}") 
    
    command2 = f"httpx -l /paramspider/qs2_bb1b.output -content-length -silent -sc -hash mmh3 >> /paramspider/httpx_bb1b_output.txt"

    try:
        run_cmd(command2)
    except subprocess.CalledProcessError as e:
        print(f"[2] An error occurred while running httpx: {e}")
