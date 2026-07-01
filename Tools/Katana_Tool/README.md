<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?color=00FF00&center=true&vCenter=true&lines=Welcome;To+This+Section" />
</p>

# 🔥 Katana Automation Toolkit — by Mrscript

A modular and automated recon tool designed to supercharge your workflow using **Katana** and **httpx**.

This tool helps bug bounty hunters and penetration testers quickly gather, filter, and organize valuable endpoints, parameters, and sensitive files from a target domain.

---

## 🚀 Features

* 🔍 Automated crawling using **Katana** (JS, XHR, paths, standard)
* 🌐 Live endpoint validation with **httpx**
* 🧠 Smart data aggregation and deduplication
* 📂 Organized output structure
* 🕵️ Sensitive file discovery
* 📁 Directory extraction
* 🔗 Parameter collection for further fuzzing
* 🧩 File-type based splitting (JS, JSON, PHP, etc.)

---

## ⚙️ How It Works

This tool runs multiple Katana modules on your target:

1. **JavaScript Discovery**

   * Extracts JS files using Katana
   * Filters live ones using httpx

2. **XHR Endpoint Extraction**

   * Finds API/XHR endpoints
   * Validates them

3. **Standard Crawling**

   * Basic crawling for general endpoints

4. **Path Enumeration**

   * Extracts paths and directories

Then:

* 🧬 Merges all results into a single file
* 🧹 Removes duplicates
* 🎯 Filters:

  * Sensitive files
  * Parameters (`?id=`, etc.)
  * Directories (`/admin/`, etc.)
* 📦 Splits files by extension for easier analysis

---

## 📁 Output Structure

```
files_and_importent/
├── sensitive_importent_files.txt
├── dirs_by_katana.txt
├── parametrs_by_katana.txt
└── files/
    ├── js.files
    ├── json.files
    ├── php.files
    ├── html.files
    └── ...
```

---

## 🛠️ Requirements

Make sure you have the following tools installed:

* [Katana](https://github.com/projectdiscovery/katana)
* [httpx](https://github.com/projectdiscovery/httpx)
* Python 3.x

---

## ▶️ Usage

```bash
python3 _main_.py.py
```

Then enter your target domain:

```
Enter domain: example.com
```

---

## ⚡ Example Use Cases

* 🎯 Bug bounty recon automation
* 🔍 Finding hidden endpoints
* 🔓 Discovering exposed sensitive files
* 🧪 Preparing targets for fuzzing
* 📊 Organizing recon data efficiently

---

## 🧠 Why This Tool?

Manual recon is slow and messy. This tool:

* Saves time ⏱️
* Reduces noise 🔇
* Organizes everything 📂
* Makes your workflow scalable 🚀

---

## ⚠️ Disclaimer

This tool is intended for **educational purposes** and **authorized testing only**.
Do not use it on targets without proper permission.

---

## 👨‍💻 Author

**Mrscript**
Aspiring Bug Bounty Hunter 🔥

---

## ⭐ Support

If you like this project:

* Give it a ⭐ on GitHub
* Share it with others
* Improve it and contribute!
<p align="center"> <img src="https://capsule-render.vercel.app/api?type=waving&color=00FF00&height=120&section=footer"/> </p>
