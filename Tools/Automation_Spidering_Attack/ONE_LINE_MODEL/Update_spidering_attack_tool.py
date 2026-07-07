import os
import sys
import re
import shutil
import subprocess
import time
from datetime import datetime
import argparse
import json
import logging
from pathlib import Path

# Setup Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[logging.NullHandler()])

# Try importing colorama
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    GREEN = Fore.GREEN
    RED = Fore.RED
    YELLOW = Fore.YELLOW
    BLUE = Fore.BLUE
    CYAN = Fore.CYAN
    RESET = Style.RESET_ALL
except ImportError:
    GREEN = RED = YELLOW = BLUE = CYAN = RESET = ""

def print_banner():
    print(f"""{BLUE}================================================={RESET}
{BLUE}     Security Reconnaissance Automation v3.2     {RESET}
{BLUE}================================================={RESET}""")

def print_status(message): print(f"{GREEN}[+]{RESET} {message}")
def print_error(message): print(f"{RED}[!]{RESET} {message}", file=sys.stderr)
def print_info(message): print(f"{YELLOW}[*]{RESET} {message}")

def check_tools(required_tools):
    missing_tools = [tool for tool in required_tools if shutil.which(tool) is None]
    if missing_tools:
        print_error(f"Missing required tools: {', '.join(missing_tools)}")
        sys.exit(1)
    print_status("All required external tools are installed.")

def run_command_with_pipe(pipeline, output_file=None, timeout=600):
    processes = []
    try:
        for i, cmd in enumerate(pipeline):
            stdin = processes[-1].stdout if i > 0 else None
            p = subprocess.Popen(cmd, stdin=stdin, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
            processes.append(p)

        for p in processes[:-1]: p.stdout.close()
        stdout, _ = processes[-1].communicate(timeout=timeout)

        if output_file and stdout.strip():
            Path(output_file).parent.mkdir(parents=True, exist_ok=True)
            with open(output_file, 'wb') as f: f.write(stdout)
            return True
        return False
    except subprocess.TimeoutExpired:
        print_error(f"Timeout reached after {timeout}s executing: {' '.join(pipeline[-1])}")
        return False
    except Exception as e:
        print_error(f"Pipeline failed: {e}")
        return False

def get_technology(input_file, output_file):
    if os.path.exists(input_file) and os.path.getsize(input_file) > 0:
        cmd = ["httpx", "-l", input_file, "-tech-detect", "-title", "-silent", "-o", output_file]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    return False

def parse_httpx_output(filepath):
    results = {}
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0: return results

    # Regex to extract URL, Status Code, and Content-Length (Handles lengths with commas like 1,234)
    httpx_regex = re.compile(r'^(https?://\S+)\s+\[(\d+)\]\s+\[([\d,]+)\]', re.IGNORECASE)

    with open(filepath, 'r', errors='ignore') as f:
        for line in f:
            match = httpx_regex.match(line.strip())
            if match:
                url, status, length = match.groups()
                length = length.replace(",", "") # Clean comma from large numbers
                base_url = url.split('?')[0]
                val = f"{status}_{length}"

                if base_url not in results: results[base_url] = {"seen_values": set(), "urls": set()}
                results[base_url]["seen_values"].add(val)
                results[base_url]["urls"].add(url)
    return results

def parse_tech_output(filepath):
    techs = set()
    if not os.path.exists(filepath): return techs
    tech_regex = re.compile(r'^https?://\S+\s+\[\d+\]\s+\[([^\]]+)\]', re.IGNORECASE)
    with open(filepath, 'r', errors='ignore') as f:
        for line in f:
            match = tech_regex.match(line.strip())
            if match:
                raw_techs = match.group(1)
                for t in raw_techs.split(','):
                    techs.add(t.strip())
    return techs

def main():
    parser = argparse.ArgumentParser(description="Advanced Security Reconnaissance Automation", formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-d', '--domain', required=True, help="Target domain (e.g., target.com)")
    parser.add_argument('-o', '--output', default=None, help="Custom output directory name")
    parser.add_argument('-m', '--mode', choices=['full', 'tech'], default='full',
                        help="Execution mode:\n  full  -> Complete recon (default)\n  tech  -> Only extract technologies")

    args = parser.parse_args()
    domain = args.domain

    if not re.match(r"^[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$", domain):
        print_error("Invalid domain format.")
        sys.exit(1)

    print_banner()

    base_tools = ["httpx", "uro"]
    if args.mode == 'full':
        base_tools.extend(["gospider", "paramspider", "qsreplace", "katana"])
    check_tools(base_tools)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = args.output if args.output else f"recon_{domain}_{timestamp}"
    temp_dir = os.path.join(output_dir, "temp")
    results_dir = os.path.join(output_dir, "results")
    tecno_dir = os.path.join(output_dir, "tecno")

    for d in [temp_dir, results_dir, tecno_dir]:
        os.makedirs(d, exist_ok=True)

    log_file = os.path.join(output_dir, "recon.log")
    logging.getLogger().addHandler(logging.FileHandler(log_file))
    logging.info(f"Started recon for {domain} in {args.mode} mode")

    print_status(f"Target: {domain} | Mode: {args.mode} | Output: {output_dir}\n")
    escaped_domain_regex = rf"([a-zA-Z0-9_]+\.)*{re.escape(domain)}\b"
    url_extraction_regex = "https?://[^ ]+"

    all_technologies = set()

    # ==================== PHASE 1: GoSpider ====================
    print_info("Phase 1: Launching GoSpider...")
    gospider_resolve_file = os.path.join(results_dir, "gospider_resolve.txt")
    gospider_tech_file = os.path.join(tecno_dir, "gospider_tech.txt")

    pipeline_gospider = [
        ["gospider", "-s", f"https://{domain}", "-d", "2", "-q"],
        ["grep", "-oE", url_extraction_regex],
        ["uro"],
        ["grep", "-Ei", escaped_domain_regex],
        ["httpx", "-silent"]
    ]

    if run_command_with_pipe(pipeline_gospider, gospider_resolve_file):
        print_status("GoSpider found live URLs. Extracting technologies...")
        if get_technology(gospider_resolve_file, gospider_tech_file):
            all_technologies.update(parse_tech_output(gospider_tech_file))

    # ==================== PHASE 2: ParamSpider ====================
    print_info("Phase 2: Launching ParamSpider...")
    paramspider_resolve_file = os.path.join(results_dir, "paramspider_resolve.txt")
    paramspider_tech_file = os.path.join(tecno_dir, "paramspider_tech.txt")

    pipeline_paramspider = [
        ["paramspider", "-d", domain, "-s"],
        ["uro"],
        ["grep", "-Ei", escaped_domain_regex],
        ["httpx", "-silent"]
    ]

    if run_command_with_pipe(pipeline_paramspider, paramspider_resolve_file):
        print_status("ParamSpider found live URLs. Extracting technologies...")
        if get_technology(paramspider_resolve_file, paramspider_tech_file):
            all_technologies.update(parse_tech_output(paramspider_tech_file))

    if args.mode == 'tech':
        print(f"\n{BLUE}====================================================={RESET}")
        print(f"{BLUE}           TECHNOLOGY DETECTION RESULTS           {RESET}")
        print(f"{BLUE}====================================================={RESET}")
        if all_technologies:
            print(f"{GREEN}[+]{RESET} Discovered Technologies: {', '.join(sorted(all_technologies))}")
        else:
            print(f"{YELLOW}[*]{RESET} No specific technologies detected.")
        print(f"{CYAN}[*]{RESET} Full details saved in: {os.path.abspath(tecno_dir)}")
        sys.exit(0)

    # ==================== PHASE 3: Parameter Reflection Analysis ====================
    print_info("\nPhase 3: Analyzing parameters for potential reflection...")
    res_aa2a_httpx = os.path.join(temp_dir, "res_aa2a_httpx.txt")
    res_bb1b_httpx = os.path.join(temp_dir, "res_bb1b_httpx.txt")

    if os.path.exists(paramspider_resolve_file) and os.path.getsize(paramspider_resolve_file) > 0:
        print_info("Running httpx analysis on aa2a & bb1b payloads...")
        # FIX: Removed -hash mmh3 to prevent parsing bugs and increase speed
        pipeline_aa = [
            ["cat", paramspider_resolve_file],
            ["qsreplace", "aa2a"],
            ["httpx", "-silent", "-sc", "-cl"]
        ]
        pipeline_bb = [
            ["cat", paramspider_resolve_file],
            ["qsreplace", "bb1b"],
            ["httpx", "-silent", "-sc", "-cl"]
        ]
        run_command_with_pipe(pipeline_aa, res_aa2a_httpx, timeout=1200)
        run_command_with_pipe(pipeline_bb, res_bb1b_httpx, timeout=1200)
    else:
        print_error("ParamSpider did not find any URLs with parameters to test.")

    print_info("Processing response data for differences...")
    reflection_results = parse_httpx_output(res_aa2a_httpx)
    reflection_results.update(parse_httpx_output(res_bb1b_httpx))

    main_parameter_file = os.path.join(results_dir, "main_parameters.txt")
    reflected_count = 0
    with open(main_parameter_file, 'w') as out:
        for base, data in reflection_results.items():
            if len(data["seen_values"]) > 1:
                out.write(f"[POTENTIAL REFLECTION] {base}\n")
                for u in sorted(data["urls"]): out.write(f"  -> {u}\n")
                out.write("\n")
                reflected_count += 1

    if reflected_count > 0:
        print_status(f"Found {reflected_count} potential reflected parameters!")
    else:
        # FIX: Better explanation for the user why it's empty
        print_info("No reflected parameters detected (Status/Length remained identical).")
        print_info("Note: The target likely ignores unknown parameters silently.")

    # ==================== PHASE 4: Katana Deep Crawl ====================
    print_info("Phase 4: Running Katana crawler modes...")
    katana_js = os.path.join(temp_dir, "katana_js.txt")
    katana_xhr = os.path.join(temp_dir, "katana_xhr.txt")
    katana_paths = os.path.join(temp_dir, "katana_paths.txt")
    all_katana_out = os.path.join(results_dir, "all_katana_resolve.txt")

    # FIX: Added -timeout 300 (5 mins max per run) and -c 20 (faster crawling) to prevent infinite hangs on huge sites
    run_command_with_pipe([
        ["katana", "-u", f"https://{domain}", "-jc", "-jsl", "-d", "3", "-c", "20", "-timeout", "300", "-silent"],
        ["grep", "-oE", url_extraction_regex], ["grep", "-Ei", escaped_domain_regex], ["sort", "-u"]
    ], katana_js, timeout=600)

    run_command_with_pipe([
        ["katana", "-u", f"https://{domain}", "-xhr", "-kf", "all", "-c", "20", "-timeout", "300", "-silent"],
        ["grep", "-oE", url_extraction_regex], ["grep", "-Ei", escaped_domain_regex], ["sort", "-u"]
    ], katana_xhr, timeout=600)

    run_command_with_pipe([
        ["katana", "-u", f"https://{domain}", "-d", "3", "-fs", "fqdn", "-c", "20", "-timeout", "300", "-silent"],
        ["grep", "-oE", url_extraction_regex], ["grep", "-Ei", escaped_domain_regex], ["sort", "-u"]
    ], katana_paths, timeout=600)

    katana_files = [katana_js, katana_xhr, katana_paths]
    if any(os.path.exists(f) and os.path.getsize(f) > 0 for f in katana_files):
        print_info("Merging and probing Katana outputs with httpx...")
        merge_cmd = [["cat"] + [f for f in katana_files if os.path.exists(f)]]
        run_command_with_pipe(merge_cmd + [["sort", "-u"], ["httpx", "-silent"]], all_katana_out, timeout=600)

    # ==================== PHASE 5: Extraction & RegEx Filtering ====================
    print_info("Phase 5: Cleaning, extracting, and sorting results...")
    combined_urls = set()
    for source in [all_katana_out, gospider_resolve_file]:
        if os.path.exists(source):
            with open(source, 'r', errors='ignore') as f:
                combined_urls.update(line.strip() for line in f if line.strip())

    paths_without_params, important_paths, parameters = set(), set(), set()
    extensions_map = {
        "configs": re.compile(r"\.(json|xml|yml|yaml|env|config|conf|ini|properties|log|txt|md)(\?|$|#)", re.IGNORECASE),
        "scripts": re.compile(r"\.(js|js\.map|map|svg)(\?|$|#)", re.IGNORECASE),
        "web_pages": re.compile(r"\.(html|css|asp|php|aspx|jsp|cgi|cfm)(\?|$|#)", re.IGNORECASE),
        "backups": re.compile(r"\.(git|bak|old|zip|tar|gz|sql|rar|7z)(\?|$|#)", re.IGNORECASE)
    }
    important_path_rx = re.compile(r"/(api|admin|login|dashboard|v[0-9]|graphql|swagger|wp-json|auth|config|internal|db|test|dev|staging|backup)(\/|$)", re.IGNORECASE)

    extracted_dir = os.path.join(output_dir, "extracted")
    for d in [os.path.join(extracted_dir, "paths"), os.path.join(extracted_dir, "params"), os.path.join(extracted_dir, "files")]:
        os.makedirs(d, exist_ok=True)

    cat_files = {cat: open(os.path.join(extracted_dir, "files", f"{cat}.txt"), 'w') for cat in extensions_map}

    for url in combined_urls:
        base_path = url.split('?')[0].split('#')[0]
        paths_without_params.add(base_path)
        if important_path_rx.search(base_path): important_paths.add(base_path)
        if '?' in url: parameters.update(re.findall(r"(?:[?&])([a-zA-Z0-9_\-]+)(?:=|$)", url))
        for cat, regex in extensions_map.items():
            if regex.search(url): cat_files[cat].write(f"{url}\n")
    for f in cat_files.values(): f.close()

    def safe_write(file_path, data_set):
        if data_set:
            with open(file_path, 'w') as f: f.write('\n'.join(sorted(data_set)) + '\n')

    safe_write(os.path.join(extracted_dir, "paths", "clean_paths.txt"), paths_without_params)
    safe_write(os.path.join(extracted_dir, "paths", "important_paths.txt"), important_paths)
    safe_write(os.path.join(extracted_dir, "params", "extracted_parameters.txt"), parameters)

    shutil.rmtree(temp_dir, ignore_errors=True)

    # ==================== PHASE 6: Summary Generator ====================
    print_status("Phase 6: Generating execution summary...")

    summary_data = {
        "domain": domain,
        "timestamp": datetime.now().isoformat(),
        "technologies": list(sorted(all_technologies)),
        "stats": {
            "total_live_urls": len(combined_urls),
            "clean_paths": len(paths_without_params),
            "important_paths": len(important_paths),
            "unique_parameters": len(parameters),
            "reflected_endpoints": reflected_count
        },
        "output_dir": os.path.abspath(output_dir)
    }

    with open(os.path.join(results_dir, "summary.json"), 'w') as jf:
        json.dump(summary_data, jf, indent=4)

    print(f"\n{BLUE}====================================================={RESET}")
    print(f"{BLUE}           RECON FINAL REPORT: {domain.upper()}{RESET}")
    print(f"{BLUE}====================================================={RESET}")
    print(f"{GREEN}[+]{RESET} Total Live URLs Discovered      : {YELLOW}{summary_data['stats']['total_live_urls']}{RESET}")
    print(f"{GREEN}[+]{RESET} Clean Directory Paths           : {YELLOW}{summary_data['stats']['clean_paths']}{RESET}")
    print(f"{GREEN}[+]{RESET} Critical/Important Paths        : {YELLOW}{summary_data['stats']['important_paths']}{RESET}")
    print(f"{GREEN}[+]{RESET} Unique Parameter Keys Extracted : {YELLOW}{summary_data['stats']['unique_parameters']}{RESET}")
    print(f"{GREEN}[+]{RESET} Potential Reflected Params      : {YELLOW}{summary_data['stats']['reflected_endpoints']}{RESET}")

    if all_technologies:
        print(f"{BLUE}-----------------------------------------------------{RESET}")
        print(f"{CYAN}[*]{RESET} Identified Technologies:")
        print(f"    {', '.join(sorted(all_technologies))}")

    print(f"{BLUE}-----------------------------------------------------{RESET}")
    print(f"{CYAN}[*]{RESET} Results saved to: {os.path.abspath(output_dir)}")
    print(f"{BLUE}====================================================={RESET}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print_error("\n[INTERRUPTED] Process killed by user (Ctrl+C).")
        sys.exit(1)
