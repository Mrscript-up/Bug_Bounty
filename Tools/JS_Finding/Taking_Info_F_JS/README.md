# 🔍 JS Info Extractor
## Extract Hidden Gems from JavaScript Files

Python 3.8+Bug BountyLicenseStatus
    "The most interesting findings are often buried in plain sight — inside JavaScript files."

## 📖 Overview

### taking_info_js.py is a lightweight yet powerful Python script designed to passively extract sensitive information from JavaScript files during Bug Bounty reconnaissance. It hunts for:

    🔑 API Keys & Tokens (AWS, Google, Stripe, etc.)
    🔗 Hidden Endpoints & Routes
    📂 Internal Paths & Directories
    🍪 Hardcoded Credentials
    🌐 Firebase Configs & Database URLs
    📮 Webhooks & External URLs
    🔧 Debug Parameters & Hidden Params

## ✨ Features
### Feature	Description
- 🚀 Fast	Parses JS files in seconds, no heavy dependencies
- 🎯 Precise	Regex patterns tuned for real-world bug bounty targets
- 📋 Clean Output	Structured, colorized terminal output — easy to read
- 🔄 Recursive	Can process multiple JS files from a directory or URL list
- 🧩 Extensible	Easy to add your own regex patterns
- 📁 Export	Save results to a file for later analysis
- 🛠️ Installation

# Clone the repositorygit clone https://github.com/Mrscript-up/Bug_Bounty.git# Navigate to the toolcd Bug_Bounty/Tools/JS_Finding/Taking_Info_F_JS/# (Optional) Create a virtual environmentpython3 -m venv venvsource venv/bin/activate    # Linux/macOSvenv\Scripts\activate       # Windows# No extra dependencies needed — pure Python 🐍

## 🚀 Usage
### Basic — Single File
```bash
python3 taking_info_js.py -f target.js
### Scan a Directory
```bash
python3 taking_info_js.py -d /path/to/js/files/
```
### From URL List
```bash
python3 taking_info_js.py -l urls.txt
### Save Output to File
```bash
python3 taking_info_js.py -f app.js -o results.txt
 ```
### All Options
```bash
python3 taking_info_js.py -h
 
 ```
## 📸 Example Output
```text
╔══════════════════════════════════════════════════════════╗
║            🔍 JS Info Extractor — Results               ║
║            Target: app.bundle.js                         ║
╚══════════════════════════════════════════════════════════╝

[🔑 API KEYS]
  ├─ AIzaSyBxxxxxxxxxxxxxxxxxxxxxxxxx (Google API Key)
  └─ sk_live_51Hxxxxxxxxxxxxxxxxxxxxx (Stripe Secret Key)

[🔗 ENDPOINTS]
  ├─ /api/v2/admin/users/export
  ├─ /api/v1/internal/debug/trace
  └─ /graphql?query={users{id,email,role}}

[🌐 URLS & WEBHOOKS]
  ├─ https://hooks.slack.com/services/T00/B00/xxx
  └─ https://internal-dashboard.company.com

[🔥 FIREBASE CONFIG]
  └─ {"apiKey":"AIza...","projectId":"app-prod-1234","databaseURL":"https://app-prod-1234.firebaseio.com"}

[📁 HIDDEN PATHS]
  ├─ /static/backup/sql_dump_2024.sql
  └─ /.env.production

═══════════════════════════════════════════════════════════
  Total Findings: 9  |  High Severity: 3  |  Medium: 4  |  Low: 2
═══════════════════════════════════════════════════════════
 ```
 
## 🧠 Pro Tips for Bug Bounty
    💡 Maximize your findings with these workflows:

```bash
# 1. First, collect all JS file URLs from a target
cat urls.txt | grep -oP 'https?://[^\s"<>]+\.js' > js_urls.txt

# 2. Download them all
cat js_urls.txt | xargs -I {} wget -q {} -P ./js_files/

# 3. Run the extractor on everything
python3 taking_info_js.py -d ./js_files/ -o findings.txt

# 4. Quick grep for the juicy stuff
cat findings.txt | grep -iE "secret|admin|internal|debug|sql|backup|\.env"
 ```
 
## 🔧 Where to Find JS Files on Targets
## 🗺️ Regex Patterns Detected

### The tool scans for these pattern categories:
Category
	
## Examples
- Cloud Keys	AWS, GCP, Azure access keys & secrets
- Payment	Stripe, PayPal, Razorpay tokens
- Social	Facebook, Twitter, GitHub tokens
- API Keys	Google Maps, SendGrid, Mailgun, Twilio
- Firebase	Full config objects with project details
- Endpoints	/api/, /graphql, /admin/, /internal/
- Secrets	Hardcoded passwords, bearer tokens, JWTs
- Webhooks	Slack, Discord, Zapier webhook URLs
- Sensitive Files	.env, .git, backup, sql_dump paths
  
## 📁 Project Structure
```text
Taking_Info_F_JS/
├── taking_info_js.py    # Main script
├── README.md            # This file
└── example_output.txt   # Sample output (optional)
 ```
## ⚖️ Disclaimer
<div align="center">
    ⚠️ This tool is intended for educational purposes and authorized security testing only.

    Only use it on targets you have explicit permission to test.
    Unauthorized scanning or extraction of data may violate laws and regulations.
    The author assumes no liability for misuse.

</div>

## 🤝 Contributing

### Pull requests are welcome! To add new regex patterns:
```
    Open taking_info_js.py
    Add your pattern to the appropriate category list
    Test with a sample JS file
    Submit a PR ✅
```
<div align="center">

<br/>
Made with 🔥 by Mrscript-up
<br/>

<img src="https://img.shields.io/badge/Bug%20Bounty-Happy%20Hunting!-red?style=for-the-badge" alt="Happy Hunting"/>

<br/><br/>
⭐ Star this repo · Report Bug · Follow on GitHub
</div>
