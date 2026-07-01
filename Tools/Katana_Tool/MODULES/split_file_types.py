from MODULES.run_cmd import run_cmd

def split_file_types():
    extensions = [
        "js", "json", "php", "aspx", "jsp", "html", "xml",
        "txt", "log", "conf", "md", "css", "svg"
    ]

    for ext in extensions:
        run_cmd(
            f"grep '\\.{ext}$' all_things_in_katana.txt > files_and_importent/files/{ext}.files"
        )
