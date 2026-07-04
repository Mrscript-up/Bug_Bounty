# 🔍 Spidering Automation Tool

A fully automated **Security Reconnaissance Pipeline** written in Python that integrates multiple powerful OSINT and web enumeration tools such as `gospider`, `paramspider`, `httpx`, `katana`, and `qsreplace`.

This tool is designed for **bug bounty hunters** and **penetration testers** to automate endpoint discovery, parameter extraction, and basic reflection analysis.

---

## ⚙️ Features

- 🌐 Automated crawling using **GoSpider**
- 🔎 Parameter discovery with **ParamSpider**
- ⚡ Live URL validation using **httpx**
- 🧠 Reflection and response comparison analysis
- 🧪 Parameter fuzzing using **qsreplace**
- 🕷️ Deep crawling via **Katana**
- 📁 Smart categorization of:
  - API / Admin / Auth endpoints
  - JS / XHR / Web assets
  - Config / backup / sensitive files
- 📊 Auto-generated recon summary report
- 🧹 Automatic cleanup of temporary files
- 🧵 Fully pipelined execution (no manual chaining needed)

---

## 📦 Requirements

Make sure the following tools are installed and available in your `$PATH`:

- gospider
- paramspider
- httpx
- qsreplace
- katana
- grep / cut / sort (Unix tools)
- Python 3.8+

Optional:
- colorama (for colored output)

Install Python dependency:

```bash
pip install colorama
```
## 🚀 Installation

#### Clone the repository:
```
git clone https://github.com/your-username/recon-automation.git
cd recon-automation
```
#### Make sure all required tools are installed:
```
go install github.com/jaeles-project/gospider@latest
go install github.com/projectdiscovery/httpx/cmd/httpx@latest
go install github.com/projectdiscovery/katana/cmd/katana@latest
```
- (Install ParamSpider manually from GitHub)

## ▶️ Usage

Run the tool:
```
python Spidering_Attack_Tool.py
```
Then enter target domain:

Enter target domain (e.g. target.com): example.com
📁 Output Structure

After execution, results will be saved in:
```
recon_<domain>_<timestamp>/
│
├── results/
│   ├── gospider_resolve.txt
│   ├── paramspider_for_now_resolve.txt
│   ├── all_things_in_katana.out
│   ├── RECON_SUMMARY.txt
│
├── extracted/
│   ├── paths/
│   │   ├── clean_paths.txt
│   │   ├── important_paths.txt
│   │
│   ├── params/
│   │   ├── extracted_parameters.txt
│   │
│   ├── files/
│       ├── configs.txt
│       ├── scripts.txt
│       ├── web_pages.txt
│       ├── backups.txt
│
└── temp/
    (temporary processing files - auto deleted)
```
## 🧠 Workflow Overview

The tool runs in 6 automated phases:

- Phase 1: GoSpider Crawling
    - Collects initial URLs
    - Filters target domain
    - Validates with httpx
- Phase 2: ParamSpider
    - Extracts parameterized URLs
    - Filters valid endpoints
- Phase 3: Reflection Analysis
    - Replaces query values using qsreplace
    - Compares response behavior via httpx
    - Detects potential reflection differences
- Phase 4: Katana Deep Crawl
    - Crawls JS, XHR, and full paths
    - Expands discovery surface
- Phase 5: Extraction & Classification
#### Extracts:
    - Clean paths
    - Important endpoints (admin, api, login, etc.)
    - URL parameters
    - Categorizes file types automatically
- Phase 6: Reporting
    - Generates final summary report
    - Displays discovered assets count
## 📌 Example Summary Output
<img width="725" height="550" alt="image" src="https://github.com/user-attachments/assets/73e2d649-9d0c-40f8-8e8f-39c25781e92c" />

## ⚠️ Disclaimer

This tool is intended for:

- Bug bounty programs
- Authorized penetration testing
- Educational purposes

### ❌ Do NOT use on systems without permission.

The author is not responsible for any misuse.

## 🛠️ Future Improvements
- Parallel execution support
- Database output (SQLite / JSON)
- Web dashboard for results
- Docker support
- Advanced vulnerability detection

## 👤 Author

Built by a Mrscript 🚀
Focused on automation, bug bounty, and offensive security tooling.

## ⭐ If you like this project

Give it a star and contribute improvements!
