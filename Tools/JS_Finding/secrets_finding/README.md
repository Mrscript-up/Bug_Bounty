
  Tool Badge  Python Badge  JS Badge  Bug Bounty Badge
  

 ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗██╔════╝ ██╔════╝██╔═══██╗██╔══██╗████╗  ██║██║  ███╗█████╗  ██║   ██║██████╔╝██╔██╗ ██║██║   ██║██╔══╝  ██║   ██║██╔══██╗██║╚██╗██║╚██████╔╝███████╗╚██████╔╝██║  ██║██║ ╚████║ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝  

  
Secrets Finding in JavaScript Files

  Hunt down hardcoded secrets, API keys, tokens & sensitive data leaked in JavaScript files.

  Features •  Installation •  Usage •  Patterns •  Examples •  Contributing
## 🎯 Overview

### secrets_finding.py is a fast, lightweight Python tool designed for Bug Bounty Hunters and Security Researchers to extract hardcoded secrets from JavaScript source files. It scans .js files or entire directories using powerful regex patterns to uncover accidentally exposed credentials.

    💡 Why it matters? Developers often hardcode API keys, tokens, and secrets inside JS bundles. These leaks can lead to full account takeovers, cloud infrastructure compromise, and critical P1 bounties.

## ✨ Features
#### Feature	Description
- 🔍 Multi-Pattern Detection	Detects API keys, tokens, passwords, AWS keys, JWTs, and more
- 📁 Recursive Scanning	Scan a single file or an entire directory tree
- 🎨 Colorized Output	Easy-to-read terminal output with highlighted matches
- 📊 Summary Report	Get a quick overview of all findings
- ⚡ Fast & Lightweight	No heavy dependencies — pure Python + regex
- 🛡️ Bug Bounty Focused	Patterns curated from real-world bounty findings
- 📝 Export Support	Save results to a file for further analysis
- 📦 Installation
## Clone the Repository
```
git clone https://github.com/Mrscript-up/Bug_Bounty.gitcd Bug_Bounty/Tools/JS_Finding/secrets_finding/
```
## Requirements
```bash
# No extra dependencies needed — uses Python standard library
python3 --version  # Requires Python 3.6+
 ```
## 🚀 Usage
### Basic Syntax
```bash
python3 secrets_finding.py [OPTIONS]
```
### Scan a Single File
```bash
python3 secrets_finding.py -f target.js
```
### Scan a Directory Recursively
```bash
python3 secrets_finding.py -d /path/to/js/files/
 ```
### Save Output to File
```bash
python3 secrets_finding.py -d /path/to/js/files/ -o results.txt
 ```
### All Options
```text
Usage: secrets_finding.py [OPTIONS]
Options:
  -f, --file      Path to a single JavaScript file
  -d, --dir       Path to a directory containing JS files
  -o, --output    Save results to output file
  -h, --help      Show this help message
 ```
 
## 🔑 Detected Patterns

The tool scans for the following categories of secrets:
Category
	
## Examples
- 🔑 API Keys	api_key, apikey, api-key, key
- 🔐 Auth Tokens	auth_token, access_token, bearer, token
- ☁️ AWS Keys	AKIA[0-9A-Z]{16}, AWS Secret Keys
** draft JWT Tokens**	eyJ[A-Za-z0-9-_]+\.eyJ[A-Za-z0-9-_]+\.[A-Za-z0-9-_]+
- 🔐 Passwords	password, passwd, pwd, secret
- 🔗 Connection Strings	mongodb://, mysql://, postgres://, redis://
- 📦 Private Keys	-----BEGIN PRIVATE KEY-----, -----BEGIN RSA
- 🌐 Webhooks	webhook, slack_webhook, discord_webhook
- 💳 Stripe/Payments	sk_live_, pk_live_, rk_live_
- ☁️ Cloud Configs	firebase, supabase, algolia keys
- 📧 SendGrid / Mail	SG., sendgrid API keys
- 🗺️ Google Maps	AIza prefixed keys
  
    📌 And many more patterns added regularly based on real bounty findings.

## all:
| Switch | Full Form    | Description                                                                                          |
| :----: | :----------- | :--------------------------------------------------------------------------------------------------- |
|  `-f`  | `--file`     | Path to a single JavaScript file to scan. Example: `-f app.js`                                       |
|  `-d`  | `--dir`      | Path to a directory for recursive scanning of all `.js` files inside it. Example: `-d ./js_files/`   |
|  `-o`  | `--output`   | Save scan results to a text file. Example: `-o results.txt`                                          |
|  `-h`  | `--help`     | Display help information and exit                                                                    |
|  `-v`  | `--verbose`  | Show detailed output including file name, line number, found value, and pattern type                 |
|  `-q`  | `--quiet`    | Quiet mode — only found results are displayed (no informational messages)                            |
|  `-p`  | `--pattern`  | Apply a custom Regex pattern in addition to default patterns. Example: `-p "MY_SECRET=[\"'].*[\"']"` |
|  `-t`  | `--type`     | Filter scanning based on a specific secret type. Example: `-t aws` searches only for AWS keys        |
|  `-e`  | `--ext`      | Change the target file extension. Default: `.js` — Example: `-e .mjs` for scanning ESM files         |
|  `-l`  | `--list`     | Display a list of all detectable patterns without scanning                                           |
|  `-nc` | `--no-color` | Disable colored output (useful for saving to files or piping)                                        |
|  `-s`  | `--silent`   | Fully silent mode — no output is printed (only exit code: `0` for no findings, `1` for findings)     |


## 📸 Examples
### Example 1: Scanning a single JS bundle
```bash
 $ python3 secrets_finding.py -f app.bundle.js

[*] Loading patterns...
[*] Scanning: app.bundle.js
[+] File size: 2.4 MB

[!] SECRET FOUND [API Key]
    Line 1247: api_key = "sk_live_4eC39HqLyjWDarjtT1zdp7dc"
    Pattern: Stripe Secret Key

[!] SECRET FOUND [AWS Key]
    Line 3591: accessKeyId: "AKIAIOSFODNN7EXAMPLE"
    Pattern: AWS Access Key ID

[!] SECRET FOUND [Password]
    Line 5820: var dbPassword = "SuperSecret123!";
    Pattern: Hardcoded Password

========================================
       SCAN COMPLETE - SUMMARY
========================================
  Files Scanned    : 1
  Secrets Found    : 3
  Scan Time        : 0.42s
========================================
 
``` 
### Example 2: Recursive directory scan with output
```bash
 $ python3 secrets_finding.py -d ./js_files/ -o bounty_findings.txt

[*] Loading patterns...
[*] Scanning directory: ./js_files/
[*] Found 47 JS files
[+] Scanning [1/47] analytics.js
[+] Scanning [2/47] auth.js
[!] SECRET FOUND [Auth Token] in auth.js:42
...
[+] Scanning [47/47] utils.js

========================================
       SCAN COMPLETE - SUMMARY
========================================
  Files Scanned    : 47
  Secrets Found    : 12
  Scan Time        : 3.21s
========================================
[*] Results saved to: bounty_findings.txt
 
 ```
## 🧠 Pro Tips for Bug Hunters
```text
┌──────────────────────────────────────────────────────────────┐
│                    🎯 BOUNTY HUNTER TIPS                     │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  1. Combine with waybackurls or gau to find old JS files     │
│     $ gau target.com | grep '.js$' | sort -u > urls.txt      │
│     $ cat urls.txt | xargs -I{} curl -s {} -o dl/$(basename {}) │
│     $ python3 secrets_finding.py -d dl/                      │
│                                                              │
│  2. Check webpack chunks — they often contain env vars       │
│     $ python3 secrets_finding.py -d ./webpack_chunks/        │
│                                                              │
│  3. Look for source maps (.js.map) to find original source   │
│                                                              │
│  4. Always verify if the secret is still active/valid        │
│                                                              │
│  5. Check for internal API endpoints leaked in JS files      │
│                                                              │
└──────────────────────────────────────────────────────────────┘
 ```
## 🛠️ Tech Stack
```
     Language: Python 3
     Core: re, os, sys (Standard Library)
     Philosophy: Zero dependencies, maximum portability
```
## 🤝 Contributing

Contributions are welcome! Here's how you can help:

    Add new regex patterns — Found a new type of secret? Submit a PR!
    Report false positives — Help improve accuracy
    Suggest features — Open an issue with your ideas
    Spread the word — Star the repo, share with the community

```bash
# Fork → Branch → Commit → Push → Pull Request
```
## ⚠️ Disclaimer
    This tool is intended for authorized security testing and educational purposes only.
    Unauthorized scanning of systems you do not own or have explicit permission to test is illegal.
    The author assumes no liability for misuse of this tool.
    Use responsibly.
## 📜 License

### This project is licensed under the MIT License — see the LICENSE file for details.
<p align="center">
  <img src="https://img.shields.io/badge/Made%20with-%E2%9D%A4%EF%B8%8F-red?style=flat-square" alt="Made with love">
  <img src="https://img.shields.io/badge/Bug%20Bounty-%F0%9F%90%9B-green?style=flat-square" alt="Bug Bounty">
  <img src="https://img.shields.io/badge/Happy%20Hacking-%F0%9F%94%A5-blue?style=flat-square" alt="Happy Hacking">
</p>

<p align="center">
  <strong>Built by <a href="https://github.com/Mrscript-up">Mrscript-up</a></strong>
</p>
<p align="center"> <img src="https://capsule-render.vercel.app/api?type=waving&color=00FF00&height=120&section=footer"/> </p>
