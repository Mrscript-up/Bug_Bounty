# Today , DAY3

- Checked the subdomains:
  - `idp-internal.liferay.com`
  - `certmanager.liferay.com`
- Continued and completed the recon for:
  - `brand.liferay.com`
  - `na1.hub.liferay.com`
- This included:
  - DIFF
  - Request/Response analysis
  - Options checker
  - etc.

There were some interesting options to test on the first domain.

I checked around **1,900 requests** in Burp for this domain, and found several interesting things worth testing further.

I also did some initial research on **SAMLRequest** in the context of the SSO domains:

- [SAMLRequest](https://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0-cd-02.html)
- [SAML Security Testing](https://cheatsheetseries.owasp.org/cheatsheets/SAML_Security_Cheat_Sheet.html)
- [SAML research by PortSwigger](https://portswigger.net/research/the-fragile-lock)

Unfortunately, since I had **school today**, I didn't have enough time to do more recon on the first two domains.

*It is what it is* :)
