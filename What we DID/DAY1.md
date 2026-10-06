# Day 1
## Part 1: Understanding the Target

- Understanding the target by exploring the entire website:
  - What sections does it have?
  - What options and features are available?
  - What actions can be performed on the website?
  - What does the website generally do?
- This includes:
  - Asking AI for an overview and better understanding of the target.
  - Opening all subdomains that are either shown by the website itself or included in the program's scope.
  - Checking all of those subdomains and reviewing all available options to understand what can be done within the application.
- Finding subdomains using `subfinder`.
- Gathering additional information about them using:
  - `naabu`
  - `httpx`
  - `dnsx`
- Taking notes on all sections and links of the website to better understand the application and storing them in `Obsidian`.
- Extracting all links and URLs from the main domain using `katana` and `uro`.
- Then, using `grep`, extracting the paths related to the domain that was provided to `katana`:
  - `grep -i ''`
- Separating important paths based on the notes taken while reviewing the website's sections and links.
  - For example, paths related to `/dc` are not useful because they are related to documentation.
- If a path has a specific option or functionality worth testing, making a note of it for further testing.
- Creating two users for additional testing, plus another user who is not logged in.

---

## Part 2: Checking Subdomains

Opening the domains manually, 10 at a time, and taking notes on all the features and options available on each domain.

This includes:

- **Request & Response**
- **URLs** → using `katana` (for now)
  - Then checking the **paths**.
- **Differences between User 1 & User 2 requests**
- **What kind of options does it have?**
  - A simple note like this:

  > <img width="564" height="670" alt="Screenshot 2026-10-03 225038" src="https://github.com/user-attachments/assets/ba3cb5d2-1fbd-4998-a11d-9f6d3f2b5977" />

Using the [Active Recon](https://github.com/Mrscript-up/Full_Recon_Tool/blob/main/Active_Recon_Tool/active-recon.py) extension.

All *commands* used:
```bash
#extracking domains:
subfinder -d target.com -all | dnsx >> domains.txt
cat domains.txt | naabu -top-ports 1000 -ep 22 > naabu_domain.txt
cat naabu_domain.txt | httpx -title -sc -cl -sc -location > httpx_domains.txt
```
```bash
#extracking urls paths:
katana -u https://target.com -jc -d 3 | httpx >> katana_httpx_1.out 
uro -i katana_httpx_1.out >> katana_httpx.out
```
