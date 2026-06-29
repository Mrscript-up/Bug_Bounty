import sys
import subprocess
from pathlib import Path

def run_httpx(target):
    # Define the command to run
    command = f"httpx -l {target}_paramspider_output.txt -content-length -silent -sc -hash mmh3 >> httpx_output.txt"
    
    # Run the command using subprocess
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running httpx: {e}") 
    
