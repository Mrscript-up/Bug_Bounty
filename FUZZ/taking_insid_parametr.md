I created this tool to extract endpoints and parameters inside post requests,
to make my work easier for the fuzzing stages.
***
### What does this tool do?

#### This tool actually takes an .xml file output from burp, which contains the values ​​and parameters in the post requests, decodes them to base64, and then sorts them based on their URL and path and displays them to the attacker. So that attacker can use these values ​​to:
- fuzzing
- mass assignment vulnerability
- testing other vulnerability else:
  - SQLI
  - XSS
  - ...

#### Features
- suport => `application/json` & `application/x-www-form-urlencoded` TE CL.
- base64 decode
- just extracing POST req
- Grouping by URL
- Sorting parameters by name
- CSV output
***
### how can you use it?
First, save the post requests that have values ​​in burp in an .xml file like this:

Burp > Target > Sitemap > Click right (on your target host) > save sellected items
and save items as a `.xml` file.

#### then run tool:
```python
python TP.py -f file_name.xml
```
#### output:
```
[*] Reading Burp XML: ..\malwarebytes.com\req.xml
[*] Found 1 request(s)
================================================================================
BURP SUITE POST PARAMETER EXTRACTOR
================================================================================

────────────────────────────────────────────────────────────────────────────────
URL: https://sso.malwarebytes.com/realms/idms/login-actions/authenticate?session_code=_cg6jfuQh9GfC4q2315ihD4q-JrKJTNPriZYkap8EpU&execution=766fcec1-d4f3-4dc7-b733-ff036c3f3fda&client_id=www-website&tab_id=HUh-HDeK0Cs&client_data=eyJydSI6Imh0dHBzOi8vd3d3Lm1hbHdhcmVieXRlcy5jb20vIiwicnQiOiJjb2RlIiwic3QiOiJjMmY3NzY1YjY1MDU5MjQ1Y2UxMzA1ZGYyOWZkMTVlOCJ9
Parameters: 4
────────────────────────────────────────────────────────────────────────────────
Parameter Name                           Value                                   
─────────────────────────────────────── ───────────────────────────────────────
credentialId                                                                     
password                                 fas;dlkfjewnfpiu341                     
rememberMe                               on                                      
username                                 ali@gmail.com                           

================================================================================
SUMMARY: 1 URLs with POST parameters, 4 total parameters
================================================================================
```
***
### All switches:
`-f` = your .xml file.
`-o` = output file.
`--csv` = for excel output file.
`--debug` = debug output.
***
### download:
```

```
