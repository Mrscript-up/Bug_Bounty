import subprocess
from pathlib import Path
from MODULES.run_cmd import run_cmd
import os

def run_AWK(domain) -> str:
    # Define the command to run
    command = r"""cat /paramspider/httpx_output.txt /paramspider/httpx_bb1b_output.txt | sort -u | uniq | awk '{url=$1;status=$2;len=$3;base=url;sub(/\?.*/,"",base);val=status"_"len;seen[base][val]=1;urls[base]=urls[base]"\n"url} END{for(b in seen){count=0;for(v in seen[b])count++;if(count>1){print "🔥 "b urls[b]"\n"}}}' /paramspider/httpx_output_AWK.txt """
    
    # Run the command using subprocess
    try:
        run_cmd(command)
        os.remove(f"/paramspider/{domain}_paramspider_output.txt")
        os.remove("/paramspider/qs.output")
        os.remove("/paramspider/qs2_bb1b.output")
        os.remove("/paramspider/httpx_output.txt")
        os.remove("/paramspider/httpx_bb1b_output.txt")
        print("resolve in => (/paramspider/httpx_output_AWK.txt)")
    except subprocess.CalledProcessError as e:
        print(f"[1] An error occurred while running httpx: {e}")
