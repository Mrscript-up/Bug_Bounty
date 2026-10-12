### what i did toady ???
so i done some subdomain recon . included some => finding paths , js files , req,res , what vulnerability should be test and etc
and i updated the subdomain recon methodology , with gowitness tool. (its a tool for take photo from pages)
like :
```
### endpoint [POST] => POST /c/portal/render_portlet 
#### testing:
- xss => on => "currentURL=" (in body)
- xss => on => "portletAjaxable=" (in body)

***
### endpoint:
- POST /home?p_p_id=com_liferay_login_web_portlet_LoginPortlet&p_p_lifecycle=1&p_p_state=maximized&p_p_mode=view&_com_liferay_login_web_portlet_LoginPortlet_javax.portlet.action=%2Flogin%2Fforgot_password&_com_liferay_login_web_portlet_LoginPortlet_mvcRenderCommandName=%2Flogin%2Fforgot_password

- information descloger . (user email) => (in reset password)
- no **ratelimition** to burtforce. => (in reset & login)
- openredirect and SSRF => on => "portlet_LoginPortlet_redirect=" (body)
- XSS => on => "web_portlet_LoginPortlet_login=" (body)
- bypass the capcha.

***
### endpoint :
- POST /home?p_p_id=com_liferay_login_web_portlet_LoginPortlet&p_p_lifecycle=1&p_p_state=exclusive&p_p_mode=view&_com_liferay_login_web_portlet_LoginPortlet_javax.portlet.action=%2Flogin%2Flogin&_com_liferay_login_web_portlet_LoginPortlet_mvcRenderCommandName=%2Flogin%2Flogin/fdfdfd

- openredirect => on => "_mvcRenderCommandName="
- massassegment => on => "_javax.portlet.action="
- openredirecct => on => "_LoginPortlet_redirect" (body)
- no **ratelimition** to burtforce.

***
### endpint => POST /c/portal/render_portlet
- XSS => on => "p_p_col_id=" (body)
```
and gowitness command:
```bash
gowitness scan single --url "https://releases-cdn.liferay.com" --write-db
```
it will give you a img file , that you can open it with `display` command.
tomorrow i,ll done another subdomains and these recon .
i hope that this recon process will be done some ): until this weak. (i hope :) )

and this command: (for crawling)
```bash
katana -u 'https://releases-cdn.liferay.com/' -d 3 | hakrawler -d 3 | anew katana.txt; uro -i katana.txt >> katana_.txt; cat katana_.txt | grep -i "liferay" | unfurl domain | while read f; do echo "https://$f"; done >> domains.txt; grep -i "releases-cdn.liferay.com" katana_.txt >> main_domain.txt; mkdir -p ./parameter ./paths; cat main_domain.txt | unfurl keypairs | sort -u >> ./parameter/parameter.txt; cat main_domain.txt | unfurl paths | sort -u >> ./paths/paths.txt; mkdir -p ./paths_for_httpx; grep -i "https://releases-cdn.liferay.com/" katana_.txt | unfurl format '%s://%d%p' | sort -u >> ./paths_for_httpx/paths.txt; cat ./paths_for_httpx/paths.txt | httpx -title -sc -cl -location -fc 404 >> ./paths_for_httpx/httpx_katana_resolve.txt; mkdir ./grep_files; cat katana_.txt | grep -Ei "\.(zip|tar|gz|bak|old|sql|db|env|conf|config|yml|yaml)$" > ./grep_files/backup_files.txt; cat katana_.txt | grep -Ei "\.js(\?|$)" > ./grep_files/js_urls.txt; cat katana_.txt | grep -oE "[a-zA-Z0-9_\-\.\/]+\.(js\.map|map)\b" > ./grep_files/only_maps.txt; rm -rf katana.txt
```
