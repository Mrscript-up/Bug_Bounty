# Day one of working on a VDP program . just for fun and learn more.
### hello there .

# Day 1

### Understanding the Target

- Understanding the target by exploring the entire website:
  - What sections does it have?
  - What options and features are available?
  - What actions can be performed on the website?
  - What does the website generally do?
- Finding subdomains using `subfinder`.
- Gathering additional information about them using:
  - `naabu`
  - `httpx`
  - `dnsx`
- Taking notes on all sections and links of the website to better understand the application and storing them in `Obsidian`.
- Extracting all links and URLs from the main domain using `katana`.
- Filtering out important paths based on the notes taken while reviewing the website's sections and links. For example, paths related to `/dc` are not useful because they are related to documentation.
- Creating two users for additional testing.

---

## Part 2: Checking Subdomains

Opening the domains manually, 10 at a time, and taking notes on all the features and options available on each domain.

This includes:

- **Request & Response**
- **URLs** → using `katana` (for now)
- **Differences between User 1 & User 2 requests**
- **What kind of options does it have?**

A simple note like this:

> <img width="564" height="670" alt="Screenshot 2026-10-03 225038" src="https://github.com/user-attachments/assets/ba3cb5d2-1fbd-4998-a11d-9f6d3f2b5977" />


Using the [Active Recon](https://github.com/Mrscript-up/Full_Recon_Tool/blob/main/Active_Recon_Tool/active-recon.py) extension.
