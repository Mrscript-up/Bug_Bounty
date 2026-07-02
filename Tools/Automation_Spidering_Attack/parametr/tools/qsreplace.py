import sys
import subprocess
from pathlib import Path
from MODULES.run_cmd import run_cmd
import time
def run_qsreplace(domain):
    # Check if qsreplace is installed
    try:
        subprocess.run(["qsreplace", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError:
        print("qsreplace is not installed. Please install it first.")
        sys.exit(1)

    # Run qsreplace command
    try:
        input_file = Path(f"/paramspider/{domain}_paramspider_output.txt")
        if not input_file.exists():
            print(f"Input file {input_file} does not exist. Please run paramspider first.")
            sys.exit(1)

        command = f"cat {input_file} | qsreplace aaaa > /paramspider/qs.output"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        time.sleep(3)
        if process.returncode != 0:
            print(f"Error running qsreplace: {stderr.decode()}")
            sys.exit(1)

        command2 = f"cat {input_file} | qsreplace bb1b > /paramspider/qs2_bb1b.output"
        process2 = subprocess.Popen(command2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process2.communicate()
        time.sleep(3)
        if process2.returncode != 0:
            print(f"Error running qsreplace: {stderr.decode()}")
            sys.exit(1)

        return stdout.decode()
    
    except Exception as e:
        print(f"error: {e}")
        sys.exit(1)
