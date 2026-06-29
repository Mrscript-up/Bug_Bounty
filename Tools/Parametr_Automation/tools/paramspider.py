import sys
import subprocess
from pathlib import Path


def run_paramspider(target):
    # Check paramspider is installed or isnt:
    try:
        subprocess.run(["paramspider", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError:
        print("paramspider is not installed. Please install it first.")
        sys.exit(1)

    # Run paramspider:
    try:
        command = f"paramspider -d {target} -s | sort -u | httpx >> {target}_paramspider_output.txt"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if process.returncode != 0:
            print(f"Error running paramspider: {stderr.decode()}")
            sys.exit(1)

        return stdout.decode()
    
    except Exception as e:
        print(f"error: {e}")
        sys.exit(1)
