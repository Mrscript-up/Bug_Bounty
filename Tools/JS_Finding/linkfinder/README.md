
**Discover hidden endpoints in JavaScript files**

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen.svg)]()
[![Version](https://img.shields.io/badge/Version-1.0.0-orange.svg)]()

</div>

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔍 **Smart Extraction** | 11 specialized regex patterns for maximum coverage |
| 🕷️ **Auto-Spidering** | Crawls websites to discover JS files automatically |
| ⚡ **Concurrent Processing** | Multi-threaded analysis for speed |
| 🎯 **HTTP Method Detection** | Identifies GET, POST, PUT, DELETE, PATCH from context |
| 🚫 **False Positive Filtering** | Intelligent filtering to reduce noise |
| 📊 **Multiple Output Formats** | CLI, JSON, and interactive HTML reports |
| 🔗 **URL Normalization** | Handles relative, absolute, and protocol-relative URLs |
| 🍪 **Custom Headers/Cookies** | Full control over requests |

### Detected Endpoint Types

- `absolute_url` — Full http/https URLs
- `relative_path` — Paths like `/api/users`
- `ajax_call` — fetch/axios/jquery calls
- `assigned_path` — `url: "/endpoint"` patterns
- `base_url` — API base URL configurations
- `template_literal` — ES6 template strings
- `graphql` — GraphQL queries/mutations
- `websocket` — ws:// and wss:// connections
- `import_path` — import/require statements
- `location_assign` — window.location assignments

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/Mrscript-up/Bug_Bounty.git
cd Tools/JS_Finding/linkfinder/

# Install dependencies
pip install -r requirements.txt
```
### Requirements:
```
requests>=2.28.0
beautifulsoup4>=4.12.0
```
 
### 🚀 Usage
```bash
python linkfinder.py <input-option> [options]
```
 
#### Input Methods (choose one)
```Flag
Description
-u, --url	Target URL to spider and analyze
-f, --file	Local JavaScript file to analyze
-j, --js-url	Direct URL to a JavaScript file
```
### 📖 Examples
#### Spider a website and show results
```bash
python linkfinder.py -u https://example.com
```
 
#### Analyze a local JS file
```bash
python linkfinder.py -f bundle.js
```
#### Analyze a specific JS file URL
```bash
python linkfinder.py -j https://example.com/static/app.min.js
```
#### Export to HTML report
```bash
python linkfinder.py -u https://example.com -o report.html
```
#### Export to JSON
```bash
python linkfinder.py -u https://example.com -o results.json
```
 
#### Deep crawl with custom headers
```bash
python linkfinder.py -u https://example.com \
  -d 3 \
  -H "Authorization: Bearer TOKEN" \
  -H "X-Custom-Header: value" \
  -o deep_scan.html
```
 
#### Filter results by pattern
```bash
python linkfinder.py -u https://example.com --filter "/api/v[0-9]"
```
 
#### Use with cookies (for authenticated areas)
```bash
python linkfinder.py -u https://example.com \
  -b "session=abc123; token=xyz789" \
  -o auth_endpoints.json
```
 
#### Skip SSL verification (for testing)
```bash
python linkfinder.py -u https://self-signed.example.com --no-verify-ssl
```
 
### 📄 Output Formats
#### CLI (default)
```text
============================================================
LinkFinder Results - 47 unique endpoints found
============================================================

   1. [POST] https://api.example.com/v2/users
      Source: https://example.com/static/app.js
      Line: 142

   2. [GET] https://api.example.com/v2/config
      Source: https://example.com/static/config.js
      Line: 23
```
 
```JSON
json
{
  "metadata": {
    "timestamp": "2024-01-15T10:30:00",
    "total_endpoints": 47,
    "tool": "LinkFinder-Python",
    "version": "1.0.0"
  },
  "endpoints": [
    {
      "url": "https://api.example.com/v2/users",
      "source_file": "https://example.com/static/app.js",
      "line_number": 142,
      "context": "...fetch('/api/v2/users', {method: 'POST'...",
      "method": "POST",
      "endpoint_type": "ajax_call"
    }
  ]
}
```
#### HTML
<img width="1000" height="700" alt="image" src="https://github.com/user-attachments/assets/93cfb349-5c91-480a-a2c8-a01d5472aab2" />

#### The HTML output includes:

- 🎨 Dark theme UI
- 🔍 Real-time search/filter
- 📋 One-click copy to clipboard
- 🏷️ Color-coded HTTP method badges
- 📊 Type-based filtering

#### ⚙️ Options
```text
Input:
  -u, --url URL          Target URL to spider and analyze
  -f, --file FILE        Local JavaScript file to analyze
  -j, --js-url URL       Direct URL to a JavaScript file

Output:
  -o, --output FILE      Output file (.json, .html, or .txt)
  --no-dedupe            Disable deduplication
  --show-context         Show code context for each endpoint

Crawling:
  -d, --depth INT        Crawling depth (default: 1)
  -c, --concurrency INT  Concurrent requests (default: 10)
  -t, --timeout INT      Request timeout in seconds (default: 30)

Request:
  -H, --header HEADER    Custom header ("Name: Value")
  -b, --cookie STRING    Cookie string ("name=value; name2=value2")
  --no-verify-ssl        Disable SSL verification

Filter:
  --filter REGEX         Filter results by regex pattern
```
### 🎯 Use Cases
#### Scenario
	
```Command
Bug bounty recon	python linkfinder.py -u https://target.com -d 2 -o recon.html
API discovery	python linkfinder.py -u https://app.com --filter "/api/"
Analyze webpack bundle	python linkfinder.py -f main.[hash].js -o endpoints.json
Find hidden routes	python linkfinder.py -u https://spa.example.com --show-context
WebSocket hunting	python linkfinder.py -u https://realtime.app --filter "ws[s]?://"
GraphQL endpoint search	python linkfinder.py -u https://api.app --filter "graphql"
```
## 🛡️ Disclaimer

#### This tool is intended for authorized security testing and educational purposes only. Unauthorized scanning of systems you do not own or have explicit permission to test is illegal. Always obtain proper authorization before using this tool.

<div align="center">
Made by Mrscript
</div>
<p align="center"> <img src="https://capsule-render.vercel.app/api?type=waving&color=00FF00&height=120&section=footer"/> </p>
