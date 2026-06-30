import sys
import subprocess
from pathlib import Path

def run_AWK(target):
    # Define the command to run
    command = r"""cat httpx_output.txt httpx_bb1b_output.txt | sort -u | uniq | awk '{url=$1;status=$2;len=$3;base=url;sub(/\?.*/,"",base);val=status"_"len;seen[base][val]=1;urls[base]=urls[base]"\n"url} END{for(b in seen){count=0;for(v in seen[b])count++;if(count>1){print "🔥 "b urls[b]"\n"}}}' httpx_output_AWK.txt """
    
    # Run the command using subprocess
    try:
        subprocess.run(command, shell=True, check=True)
        
    except subprocess.CalledProcessError as e:
        print(f"[1] An error occurred while running httpx: {e}")
