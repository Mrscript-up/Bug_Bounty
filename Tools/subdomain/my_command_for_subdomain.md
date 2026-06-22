<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?color=00FF00&center=true&vCenter=true&lines=Welcome+To+This+Section;" />
</p>

### I use this command and tools to collect subdomains of a target:
- subfinder
- alterx
- dnsx
- naabu
- httpx

<img src="https://user-images.githubusercontent.com/74038190/212284087-bbe7e430-757e-4901-90bf-4cd2ce3e1852.gif" width="30" height="30"></img> command:
```bash
subfinder -d example.com -all | alterx | dnsx -a -resp | sed 's/\[[^]]*\]//g' | httpx -mc 200,201,202,203,204,301,302,303,307,308,401,403,405,500 >> resolve.txt
cat resolve.txt | naabu -top-ports 1000 -ep 22 > resolve2.txt # + httpx -mc 200,201,202,203,204,301,302,303,307,308,401,403,405,500
cat resolve2.txt | httpx -title -sc -cl -location > resolve3.txt

# use "sort -u"
```
***
### Before the first explanation, let's look at how we can download these tools?
Just download pdtm tool.

whats pdtm??
```
The pdtm tool actually has a list of tools within it that are useful,
and it makes it easier for you to download them so that you no longer need to download these tools one by one.
```
OK.

Frist you need yo download GO language => `apt install golang-go`
then download pdtm => `go install -v github.com/projectdiscovery/pdtm/cmd/pdtm@latest`

#### After going through the previous steps, we must first clean all the tools with this command => `pdtm -ra` then:
#### We download the tools with this command => `pdtm -ia -igp`
#### After the download is complete, run pdtm to see the tools you downloaded.

#### This tool has the ability to update a tool via pdtm if an update is available.

### NOW: some inforamtion about alterx tool:
berore use alterx , write your target hist here in this section:
for example write => google , api , etc
<img width="600" height="600" alt="image" src="https://github.com/user-attachments/assets/2d7c2db7-d79c-4eba-a9b9-f7785c50f3ff" />
#### and after find subdomains => open all subdomain by this extention in browzer: `open-multiple-urls`
download from (for firefox) => [open-multiple-urls](https://addons.mozilla.org/en-US/firefox/addon/open-multiple-urls/)

<img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/4b1714d2-c7ad-450b-8117-a9418a0344c3" />

***
👤 tool link => [PDTM](https://github.com/projectdiscovery/pdtm)

🧰 tools links:
- [subfinder](https://github.com/projectdiscovery/subfinder)
- [alterx](https://github.com/projectdiscovery/alterx)
- [dnsx](https://github.com/projectdiscovery/dnsx)
- [naabu](https://github.com/projectdiscovery/naabu)
- [httpx](https://github.com/projectdiscovery/httpx)
- [open-multiple-urls](https://addons.mozilla.org/en-US/firefox/addon/open-multiple-urls/)

<p align="center"> <img src="https://capsule-render.vercel.app/api?type=waving&color=00FF00&height=120&section=footer"/> </p>

