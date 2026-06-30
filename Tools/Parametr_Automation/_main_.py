import sys
from pathlib import Path
import time
from tools.paramspider import run_paramspider
from tools.qsreplace import run_qsreplace
from tools.httpx import run_httpx
from tools.AWK import run_AWK


if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print(f'start with => python3 _main_.py domain')
    else:    
        input_target = sys.argv[1]
        print(f'start tool {input_target}')

    run_paramspider(input_target)
    time.sleep(1.5)
    run_qsreplace(input_target)
    time.sleep(1.5)
    run_httpx()
    time.sleep(1.5)
    run_AWK()


    
