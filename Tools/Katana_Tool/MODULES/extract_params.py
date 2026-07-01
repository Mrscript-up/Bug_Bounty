from MODULES.run_cmd import run_cmd

def extract_params():
    run_cmd(
        r"""grep '=' all_things_in_katana.txt > files_and_importent/parametrs_by_katana.txt"""
    )
