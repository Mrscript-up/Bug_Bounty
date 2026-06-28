import subprocess
import sys
import threading
import time
from pathlib import Path
from tools.subfinder import run_subfinder
from tools.dnsx import run_dnsx
from tools.naabu import run_naabu
from tools.sort_HTTPX import run_sort_httpx
from tools.HttPX import run_httpx
from tools.DeLeTe_OldFiLe import run_delete_old_files
#-----------------------inside-musole----------------------
'''
if you dont have this tools already , download them:
1- httpx
2- subfinder
3- naabu
4- dnsx
'''
# taking target input from user:

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python _main_.py <domain>")
        sys.exit(1)

    domain = sys.argv[1]
    run_subfinder(domain)
    time.sleep(1.5)
    run_dnsx(domain)
    time.sleep(1.5)
    run_naabu(domain)
    time.sleep(1.5)
    run_sort_httpx(domain)
    time.sleep(1.5)
    run_httpx(domain)
    time.sleep(1.5)
    run_delete_old_files(domain)
