
<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?color=00FF00&center=true&vCenter=true&lines=Welcom+To+This+Section" />
</p>

# 🕷️ Automation Spidering Attack

> 🔥 A powerful automation toolkit for spidering & reconnaissance in bug bounty hunting.

---

## 📌 Description

**Automation Spidering Attack** is a modular and lightweight tool designed to automate the spidering phase of reconnaissance in bug bounty workflows.

This tool leverages powerful utilities like `katana`, `httpx`, and other recon techniques to:

* Collect URLs and endpoints
* Extract JavaScript files
* Filter valid and live targets
* Focus only on the target domain (no noise 🔥)

Built for speed, efficiency, and clean output.

---

## ⚡ Features

* ✅ Automated spidering using `katana`
* ✅ JavaScript file extraction (`-js`, `-jc`, `-jsl`)
* ✅ Live URL filtering using `httpx`
* ✅ Domain-based filtering (only target domain & subdomains)
* ✅ Clean & unique output (sorted + deduplicated)
* ✅ Modular structure (easy to extend 🔧)
* ✅ Designed for bug bounty recon workflows

---

## 🛠️ Installation

```bash
git clone https://github.com/Mrscript-up/Bug_Bounty.git
cd Bug_Bounty/Tools/Automation_Spidering_Attack
```

---

## ▶️ Usage

```bash
python3 _main_.py -d example.com
```

Or if you designed it differently:

```bash
python3 _main_.py example.com
```

---

## ⚙️ Workflow

```text
Target Domain
     ↓
Katana Spidering
     ↓
Extract JS / URLs
     ↓
Sort & Deduplicate
     ↓
Filter Live URLs (httpx)
     ↓
Domain Filtering (No Out-of-Scope)
     ↓
Clean Output 🎯
```
---

## 🧠 Why This Tool?

During bug bounty recon, tools like spiderers often return:

* ❌ Noise (other domains)
* ❌ Duplicates
* ❌ Dead endpoints

This tool solves that by:

* Filtering only target domain
* Keeping outputs clean and usable
* Automating repetitive steps

---

## 🔥 Use Cases

* Bug bounty reconnaissance
* JavaScript analysis
* Endpoint discovery
* Attack surface mapping

---

## 📦 Requirements

Make sure you have installed:

* `katana`
* `httpx`
* `Python 3.x`

---

## 💡 Future Improvements

* [ ] Parallel execution
* [ ] Add more spidering tools (gospider, hakrawler)
* [ ] JSON output support
* [ ] Integration with nuclei
* [ ] Auto recon pipeline

---

## 🤝 Contributing

Pull requests are welcome. Feel free to improve or extend the tool.

---

## ⚠️ Disclaimer

This tool is for educational and authorized security testing purposes only.
Do not use it on systems without permission.

---

## 👨‍💻 Author

**Mrscript**
Bug Bounty Hunter 🚀

---
## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
<p align="center"> <img src="https://capsule-render.vercel.app/api?type=waving&color=00FF00&height=120&section=footer"/> </p>
