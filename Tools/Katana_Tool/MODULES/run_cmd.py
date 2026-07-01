import subprocess
import time

DELAY = 3  # seconds for per command

def run_cmd(cmd):
    print(f"[+] Running: {cmd}")
    subprocess.run(cmd, shell=True)
    time.sleep(DELAY)
