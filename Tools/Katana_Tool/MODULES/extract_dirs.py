from MODULES.run_cmd import run_cmd

def extract_dirs():
    run_cmd(
        "sed 's/?.*//' all_things_in_katana.txt > files_and_importent/dirs_by_katana.txt"
    )
