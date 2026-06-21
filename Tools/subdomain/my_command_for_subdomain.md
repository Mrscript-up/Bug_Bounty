### I use this command and tools to collect subdomains of a target:
- subfinder
- alterx
- dnsx
- naabu
- httpx

command
```bash
subfinder -d example.com -all | alterx | dnsx >> resolve.txt
cat resolve.txt | naabu -top-ports 1000 -ep 22 > resolve2.txt
cat resolve2.txt | httpx -title -sc -cl -location > resolve3.txt

# use "sort -u"
```

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

Link tool => [PDTM](https://github.com/projectdiscovery/pdtm)

