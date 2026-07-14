## CppRecon ⚡

### A lightweight, dependency-free, and fast TCP Port Scanner written in C++, designed for the Reconnaissance phase in Bug Bounty.
About the Project

### In the bug bounty and penetration testing lifecycle, the Reconnaissance phase is crucial. While tools like Nmap are incredibly powerful, they can sometimes be overkill for a quick check of common ports. 

### CppRecon is a custom-built utility that leverages raw POSIX sockets to perform basic TCP Connect scans. It requires no external libraries, compiles in seconds, and serves as an excellent demonstration of low-level network programming in C++ for your portfolio.
## Features
    Zero Dependencies: No need to install third-party libraries (like libpcap or Boost).
    Lightweight & Fast: Direct use of Linux system calls for minimal overhead.
    Clean Code: Written with modern C++ standards and best practices.
    Curated Default Ports: Pre-loaded with a list of the most common web and network ports.

## Prerequisites
```
    Linux or macOS operating system
    g++ compiler
```


## Compile the source code (using the -O2 flag for speed optimization is recommended): 
 ```bash
g++ -O2 scanner.cpp -o cpprecon
 ```
 

## Run the scanner (Note: sudo is required to scan privileged ports below 1024):
```bash
./cpprecon 192.168.1.1
# or scan a specific host
sudo ./cpprecon example.com
 ```
 
## Example Output
 ```text
[*] Starting scan on host: 192.168.1.1
--------------------------------------------------
[+] Port 22 is OPEN!
[+] Port 80 is OPEN!
[+] Port 443 is OPEN!
--------------------------------------------------
[*] Scan finished. Found 3 open ports.
 ```
 
## Roadmap
### This project currently serves as a solid foundation for a custom recon tool. Future updates will include:

     Multi-threading: Concurrent port scanning for significant speed improvements.
     Custom Port Ranges: Allow users to input custom ranges (e.g., 1-1000).
     JSON Export: Output results in JSON format for easier parsing by other scripts.
     Banner Grabbing: Basic service version detection.
