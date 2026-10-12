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
