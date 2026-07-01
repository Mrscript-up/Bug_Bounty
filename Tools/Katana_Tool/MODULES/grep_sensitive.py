from MODULES.run_cmd import run_cmd

def grep_sensitive():
    run_cmd(
        r"""grep -E '\.(bak|old|zip|tar|gz|sql|env|config|yml|yaml|xml|php|asp|aspx|jsp|git|cgi|cfm|do|action|json|js|js.map|map|xml|html|css|svg|txt|conf|log|md)$' all_things_in_katana.txt > files_and_importent/sensitive_importent_files.txt"""
    )
