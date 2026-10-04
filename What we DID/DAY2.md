We extracted all the paths of one of the subdomains:

```url
https://status.liferay.cloud
https://status.liferay.cloud/api/v2/status.json
https://status.liferay.cloud/enterprise.js
https://status.liferay.cloud/incidents/qm0jh27c5zr1
https://status.liferay.cloud/history
https://status.liferay.cloud/history.rss
https://status.liferay.cloud/incidents/1nsx2rzr49rm
https://status.liferay.cloud/history.atom
https://status.liferay.cloud/incidents/dtqmg6kzxnf9
https://status.liferay.cloud/incidents/zl7rvcmbznv5
...
...
...
```

We moved on to the other domains and their options and took notes from them:

<img width="574" height="988" alt="Screenshot 2026-10-04 210325" src="https://github.com/user-attachments/assets/27fbc527-7681-4dcf-920a-bf91a2a1cc97" />


We checked and reviewed the overall status of the subdomains:

```python
http://customer-uat.liferay.com:1077 [200] [] [1378] [money]
http://customer-uat.liferay.com:1056 [200] [] [1378] [money]
http://customer-uat.liferay.com:1121 [200] [] [1378] [money]
```

We performed full reconnaissance on 6 of them using the following tool:

[active-recon](https://github.com/Mrscript-up/Full_Recon_Tool/tree/main/Active_Recon_Tool)

Some of the reconnaissance notes:

### [status.liferay.cloud] Page:
### Request: 7
**URL** : https://status.liferay.cloud:443/subscriptions/new-email #URL
**METHOD**: `POST` #POST-req
**NOTE-REQ**: #note-req
> subscribe to updates button.

**STATUS**: `200` #status_200
**REQ**:
```python
POST /subscriptions/new-email HTTP/2
Host: status.liferay.cloud
Cookie: _ga_XVBB7MBJYJ=GS2.1.s1790606498$o2$g0$t1790606498$j60$l0$h0; _ga=GA1.2.831444701.1790520452; _spsess=TFZXUGNhZ05zaW0zZzZwTnYwc2c4Sk5uaTZkL0lZRThWb25zek05MndMdGpsUEFGSGRPZHZoUXpweVRUZnVONldIdlFFNWdIZ09jeDFkYXdvekpTbWhtRjBkRHAyUDYybzhpNlJIb2xzTS9zelFiWms2NWJTNTFPd2Y1b2Qrb1EzQXpIZ0NGREdLbzBTTlVjRWtEZFQ0L3Zab09ZZzlFNzBsR1hFVnRzQjdnS0Q2Zm5MYXdOQkNCL2NTMWxvTWVlVWxFeUpPTzNNcm4rK2g4VGNwcm91b2pjQnJaQVViSFRaV3I0WDYyc2Zzaz0tLW81aW5aVDhWbTY5QUt6OHJSSDE0bXc9PQ%3D%3D--931b614f31f3436bf4e9a8c0928edb89d32bfcda
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:157.0) Gecko/20100101 Firefox/157.0
Accept: */*;q=0.5, text/javascript, application/javascript, application/ecmascript, application/x-ecmascript
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate, br
Referer: https://status.liferay.cloud/history?page=2
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 2692
Origin: https://status.liferay.cloud
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

authenticity_token=bz5o0IgFW4Q_fK8NLAH_505knStpaBCs6aLNgHGoaN9V0Pclps6qD7B-V3BbyRVAWMF-R71_Rl_XZHOlac_kXg&email_otp_verify_flow=false&email=ali%40gmail.com&email_otp_auth_token=&otp=&captcha_error=false&g-recaptcha-response=0cAFcWeA4vkj9K74wUGMYNnrBEzzXw36O92r8DjOI8DtBwtEdoJ4DIDHcWirr4BuJz0zjTFQ298Fp3ouJ2D-QSbUziAb2lzMAvVT6VTyJOgmndYFiZ-55GetjEhHzKrJ4LEwr0tKI7kL1jz1HzmJ2-BchBGGsBt6JICWchGqj64q8ZswRbtN59buW3D7O0eKI9TI_1PIN6p7qeQ9-trGPUCyw7ReYtup4FqbC_XtoUKl7UQuXfDKwZjX5MP7hafPrQdPkXlP2AqYTOrD-2ThhODgZssGDI00Ve1IEl0rPgaLI4xz0shiTuA4LV_f1xWATjln0EGngDD2qcHEPJeCnUYz7XIQq5I7GbRJAp5A90Rl7j8r5En1Qx0CbQEzuskW0HZFnYOJZf_d4jSi7-VMFsF2IgKSt-x2rOoIV-kDcrz14OtxieoFfCFLy-PtXkBBOcYgMdD9qJyMgz_UfwIdZ_6UJf9hCjUFy7Qi1PI_5lFv_svV8ZHOWbnPHTTK1wLr9K3qbcNzZ5U1b3RygWlkjUCn5mT6QRfVXRDHNM__SKG9CjZDwOVh32Tq0mhNLJYpM3FHuWfrqrOW_-8pod-j-8GdgOs0OdMPcDPR6EtFRs2sZ85S-6Uuq_SkNIIVwIWyKcoTcfLj_moOruzyZLmitcuLUJNQJu2hCPsx8v1Ou-p8FVvlpaIrReTHC4etisxcmH22ukc1xnRkbb8jiyXQzJlBzZPDxDtzJp9MrzifosMfFeOX-y25eVjtPd-PvG_1qAeftZNSLpN4J9__FLB0x4qToJEO8P8wqjSeFm6iuiUcFTYXyASYBxC9qa2gitZM-HwHrU_VV4T0x5r-Cl6S-hk1YQhEnEWhvxFc_k6d6jUzz71ZITB4Kd472Wdja6cxku6npH9ezirjJtzUDK8zFAHSbDBwLO86vS83h-zSVVMURrW3JU4m8Xx_emU6KNbKYB_ISzMSmmEhoFRFe2MWA3Iobo5wRR8_yYkd-GsmSCBzPvKQIwxNGIwAGwlJuNoNSooP1DK_QtFJkFA_6idLOcsKDFo0eVpo42fJpO12PJLfzy9hZ_ghMjrrIFyROuiP9baxyRWg04Elw4UxnIoLpU5cBPZssWJf9VL1CtZqaAQenc-Qad5TvYKMRYo9dDKT6IsHRb2o2wSe2f6gQEkqldtVBSW1EV3rhTv-BDevNVpfJF2FeAkwNiUZhB9q8nDGrtNRYsSB43GBcYK2q2pZOw47AGHc9XQHICvfKbjWICCnZV9JMlKh8H5ycbnRmteotgXxEMShnX9cQVpvOMMtWpR0ySo6PUV8PhHw36NL8r3Ed7Ey-w0f5IXogIwAl_Jx5DSYUsqjbpOlqM5KlrLfrcXZLygJ6Q6WUQrxAQ-TkXfMajUxBrkTBrKzJtXp7D6k1gZtZz3F_BLcrgoSvrgQ_4uHLKKgeetfnaeFUTsMlF3kKI0EjHxmUg7-NIXH7aP2Q87WmnWfdcUvFXwI_hp2Brp-Yzg_rM-0cq-sbRWa5PwWsHjjgrKQG5E_WYUJweOHRZb5zej-npVhHVPEDs_bKjelElobvz5qMtkQd1NGbsMraQ0OTtatH_g-uRmM-ZnfKDn03VbrVPG4E99GmDgL9nxenJANYK3PEQr4qAf6gvirqkaOzENpdVLDwzuWl7qR8dVn3xL2_s_HlTjJEZxW0LOqU154Uji0elfQffXUiPNIUuIpYlY5iJNN37WroGYPmdztOof5hP4x4G8ga6EZwxNoAslrfvX6KnXw5K5lIUNOokoc9Foe_M2wg9YWVDOlnM6FwaaA17Rj-oFos-wrrpPGwDvwdIfiYonyzWHsOpBl7HUopUfLIJQBykCHED38E8xURdX7gOp6oafHFoLXrNzUasv2vF3YxO-SDOtgRQlnloCO-0ZDVAo_a0FZA1r6VvjMbm4SzziRuZ16NjIOcXBV84s3Qt6oSVB6Z7gBEZX7dnwTMxW9LPJuP07McquXbQWyUfe9H51BGYltdiQgrRHBMt9Z8V5YcE3Z4ddYpUd5T5ID4N4KXf8wZHC2fEGYsJ2sJuhI-N5u1m98iBdGtYoBhuNOB6sbgTft6Wt04I_y72NPu2vpDR5DP5fM_K9U61KTWhG_QfyaqcFafMHjHbaHD7b3JMh9nfeiuK8NE8GuRWvFo1uVUdJyIvco5P73cFfK5CS8h8H5c14baaIeIm0WY4uIHSYlFjgCNojLM1vmHeiKE1ta5xmSwi2zOX5xR4kXtvR-BRygAvFCRpKIhEmf4Or6RynRxJNCTlShfvwCe2ZoJ1x5L-HAlDdBdifuffewB-AV498XAVKPTeiXEtcwKd2tcJBq-eu_CgQOjDYLTFvArWEKJhlvJX4jvqHJ4wuXM8sEJeTRKjbMnsVe89a-ISp35phgtg_pFMxF5o8Ryp44olHjldRJN_g6Mt_FzwgFxPrLRwJpILYywuW7a4E_721bOz3bCVg
```

**REQ-DATA**:
`decode`

```python
authenticity_token=bz5o0IgFW4Q_fK8NLAH_505knStpaBCs6aLNgHGoaN9V0Pclps6qD7B-V3BbyRVAWMF-R71_Rl_XZHOlac_kXg&email_otp_verify_flow=false&email=ali@gmail.com&email_otp_auth_token=&otp=&captcha_error=false&g-recaptcha-response=0cAFcWeA4vkj9K74wUGMYNnrBEzzXw36O92r8DjOI8DtBwtEdoJ4DIDHcWirr4BuJz0zjTFQ298Fp3ouJ2D-QSbUziAb2lzMAvVT6VTyJOgmndYFiZ-55GetjEhHzKrJ4LEwr0tKI7kL1jz1HzmJ2-BchBGGsBt6JICWchGqj64q8ZswRbtN59buW3D7O0eKI9TI_1PIN6p7qeQ9-trGPUCyw7ReYtup4FqbC_XtoUKl7UQuXfDKwZjX5MP7hafPrQdPkXlP2AqYTOrD-2ThhODgZssGDI00Ve1IEl0rPgaLI4xz0shiTuA4LV_f1xWATjln0EGngDD2qcHEPJeCnUYz7XIQq5I7GbRJAp5A90Rl7j8r5En1Qx0CbQEzuskW0HZFnYOJZf_d4jSi7-VMFsF2IgKSt-x2rOoIV-kDcrz14OtxieoFfCFLy-PtXkBBOcYgMdD9qJyMgz_UfwIdZ_6UJf9hCjUFy7Qi1PI_5lFv_svV8ZHOWbnPHTTK1wLr9K3qbcNzZ5U1b3RygWlkjUCn5mT6QRfVXRDHNM__SKG9CjZDwOVh32Tq0mhNLJYpM3FHuWfrqrOW_-8pod-j-8GdgOs0OdMPcDPR6EtFRs2sZ85S-6Uuq_SkNIIVwIWyKcoTcfLj_moOruzyZLmitcuLUJNQJu2hCPsx8v1Ou-p8FVvlpaIrReTHC4etisxcmH22ukc1xnRkbb8jiyXQzJlBzZPDxDtzJp9MrzifosMfFeOX-y25eVjtPd-PvG_1qAeftZNSLpN4J9__FLB0x4qToJEO8P8wqjSeFm6iuiUcFTYXyASYBxC9qa2gitZM-HwHrU_VV4T0x5r-Cl6S-hk1YQhEnEWhvxFc_k6d6jUzz71ZITB4Kd472Wdja6cxku6npH9ezirjJtzUDK8zFAHSbDBwLO86vS83h-zSVVMURrW3JU4m8Xx_emU6KNbKYB_ISzMSmmEhoFRFe2MWA3Iobo5wRR8_yYkd-GsmSCBzPvKQIwxNGIwAGwlJuNoNSooP1DK_QtFJkFA_6idLOcsKDFo0eVpo42fJpO12PJLfzy9hZ_ghMjrrIFyROuiP9baxyRWg04Elw4UxnIoLpU5cBPZssWJf9VL1CtZqaAQenc-Qad5TvYKMRYo9dDKT6IsHRb2o2wSe2f6gQEkqldtVBSW1EV3rhTv-BDevNVpfJF2FeAkwNiUZhB9q8nDGrtNRYsSB43GBcYK2q2pZOw47AGHc9XQHICvfKbjWICCnZV9JMlKh8H5ycbnRmteotgXxEMShnX9cQVpvOMMtWpR0ySo6PUV8PhHw36NL8r3Ed7Ey-w0f5IXogIwAl_Jx5DSYUsqjbpOlqM5KlrLfrcXZLygJ6Q6WUQrxAQ-TkXfMajUxBrkTBrKzJtXp7D6k1gZtZz3F_BLcrgoSvrgQ_4uHLKKgeetfnaeFUTsMlF3kKI0EjHxmUg7-NIXH7aP2Q87WmnWfdcUvFXwI_hp2Brp-Yzg_rM-0cq-sbRWa5PwWsHjjgrKQG5E_WYUJweOHRZb5zej-npVhHVPEDs_bKjelElobvz5qMtkQd1NGbsMraQ0OTtatH_g-uRmM-ZnfKDn03VbrVPG4E99GmDgL9nxenJANYK3PEQr4qAf6gvirqkaOzENpdVLDwzuWl7qR8dVn3xL2_s_HlTjJEZxW0LOqU154Uji0elfQffXUiPNIUuIpYlY5iJNN37WroGYPmdztOof5hP4x4G8ga6EZwxNoAslrfvX6KnXw5K5lIUNOokoc9Foe_M2wg9YWVDOlnM6FwaaA17Rj-oFos-wrrpPGwDvwdIfiYonyzWHsOpBl7HUopUfLIJQBykCHED38E8xURdX7gOp6oafHFoLXrNzUasv2vF3YxO-SDOtgRQlnloCO-0ZDVAo_a0FZA1r6VvjMbm4SzziRuZ16NjIOcXBV84s3Qt6oSVB6Z7gBEZX7dnwTMxW9LPJuP07McquXbQWyUfe9H51BGYltdiQgrRHBMt9Z8V5YcE3Z4ddYpUd5T5ID4N4KXf8wZHC2fEGYsJ2sJuhI-N5u1m98iBdGtYoBhuNOB6sbgTft6Wt04I_y72NPu2vpDR5DP5fM_K9U61KTWhG_QfyaqcFafMHjHbaHD7b3JMh9nfeiuK8NE8GuRWvFo1uVUdJyIvco5P73cFfK5CS8h8H5c14baaIeIm0WY4uIHSYlFjgCNojLM1vmHeiKE1ta5xmSwi2zOX5xR4kXtvR-BRygAvFCRpKIhEmf4Or6RynRxJNCTlShfvwCe2ZoJ1x5L-HAlDdBdifuffewB-AV498XAVKPTeiXEtcwKd2tcJBq-eu_CgQOjDYLTFvArWEKJhlvJX4jvqHJ4wuXM8sEJeTRKjbMnsVe89a-ISp35phgtg_pFMxF5o8Ryp44olHjldRJN_g6Mt_FzwgFxPrLRwJpILYywuW7a4E_721bOz3bCVg
```

**RES**:
```python
HTTP/2 200 OK
Content-Type: application/json; charset=utf-8
Date: Thu, 01 Oct 2026 13:28:03 GMT
X-Download-Options: noopen
X-Permitted-Cross-Domain-Policies: none
Referrer-Policy: strict-origin-when-cross-origin
X-Statuspage-Version: 7f2d0789bbd5cf3da6b7515f3d369b7dfdd2265f
Vary: Accept,Accept-Encoding,X-Forwarded-Host,X-Forwarded-Scheme,X-Forwarded-Proto,Fastly-SSL
Strict-Transport-Security: max-age=259200
X-Statuspage-Skip-Logging: true
Access-Control-Allow-Origin: *
X-Pollinator-Metadata-Service: status-page-web-pages
Etag: W/"98049a8585e71d979be711a97278eccf"
Cache-Control: max-age=0, private, must-revalidate
Set-Cookie: _spsess=SGVrYjBpZEIxUWFScHFtaDhsUmZTcHlBSGJuYlowdnRoUWZER2NoQS9qMG8zUXdZRzBJeU5kUXUwRHNIRVlJTzhoNmlIbHFUUHZTbFZPSlgxdEVsaE5EVFQwMHF5dVptQ2QyRWF4UDBSU3BqY3JMNVRCUFBMdk0rZHRtcVRPUy82ZW1XQnlSYXFlMDZJUjAwTUZ1YzVNZkpzNlp5d0hBQVUvQmlpQk1wTUwwYUdlZllMSE9KdmpMT09LZTI4YlFHNUpBVksyRHcySGFhcXFqcG5SdDJwZlVWOFJhM2hmODlMZVc3Zm9ncFo1az0tLTlnU0VyZDc5cjFIbDJCRlFOR1QrNUE9PQ%3D%3D--27222a4c55b940da509c12c8fca281f6fdef02af; path=/; expires=Sun, 04 Oct 2026 13:28:03 GMT; secure; HttpOnly; SameSite=Lax
X-Runtime: 0.395699
Server: AtlassianEdge
Accept-Ranges: bytes
X-Content-Type-Options: nosniff
X-Xss-Protection: 1; mode=block
Atl-Traceid: 84f7129976b04ccea28721c80d6ce140
Atl-Request-Id: 84f71299-76b0-4cce-a287-21c80d6ce140
Report-To: {"endpoints": [{"url": "https://dz8aopenkvv6s.cloudfront.net"}], "group": "endpoint-1", "include_subdomains": true, "max_age": 600}
Nel: {"failure_fraction": 0.01, "include_subdomains": true, "max_age": 600, "report_to": "endpoint-1"}
Server-Timing: atl-edge;dur=670,atl-edge-internal;dur=5,atl-edge-upstream;dur=665,atl-edge-pop;desc="aws-us-east-1"
X-Cache: Miss from cloudfront
Via: 1.1 ca9f3841ca2bd61788b6781e41891042.cloudfront.net (CloudFront)
X-Amz-Cf-Pop: DUS51-P6
Alt-Svc: h3=":443"; ma=86400
X-Amz-Cf-Id: cXnRDj6kf6FRHZuPwalNBaeqdIk1AVlaVgILFTrcpE4ecqSgQqW7uQ==
```

**RES-DATA**:
`decode`

```python
{"text":"Check your email inbox and confirm your subscription.","redirect_to":"/subscriptions/component-selection?id=3kxdxr3z71nc","type":"success"}
```

**PARAMETERS**: #parameters
```python
_ga_XVBB7MBJYJ, _ga, _spsess, authenticity_token, email_otp_verify_flow, email, email_otp_auth_token, otp, captcha_error, g-recaptcha-response, type, redirect_to, text
```

**PARAMETER VALUES**: #parameter_values
```python
_ga_XVBB7MBJYJ = GS2.1.s1790606498$o2$g0$t1790606498$j60$l0$h0
#-------------------------------------
_ga = GA1.2.831444701.1790520452
#-------------------------------------
_spsess = TFZXUGNhZ05zaW0zZzZwTnYwc2c4Sk5uaTZkL0lZRThWb25zek05MndMdGpsUEFGSGRPZHZoUXpweVRUZnVONldIdlFFNWdIZ09jeDFkYXdvekpTbWhtRjBkRHAyUDYybzhpNlJIb2xzTS9zelFiWms2NWJTNTFPd2Y1b2Qrb1EzQXpIZ0NGREdLbzBTTlVjRWtEZFQ0L3Zab09ZZzlFNzBsR1hFVnRzQjdnS0Q2Zm5MYXdOQkNCL2NTMWxvTWVlVWxFeUpPTzNNcm4rK2g4VGNwcm91b2pjQnJaQVViSFRaV3I0WDYyc2Zzaz0tLW81aW5aVDhWbTY5QUt6OHJSSDE0bXc9PQ==--931b614f31f3436bf4e9a8c0928edb89d32bfcda
#-------------------------------------
authenticity_token = bz5o0IgFW4Q_fK8NLAH_505knStpaBCs6aLNgHGoaN9V0Pclps6qD7B-V3BbyRVAWMF-R71_Rl_XZHOlac_kXg
#-------------------------------------
email_otp_verify_flow = false
#-------------------------------------
email = ali@gmail.com
#-------------------------------------
email_otp_auth_token =
#-------------------------------------
otp =
#-------------------------------------
captcha_error = false
#-------------------------------------
g-recaptcha-response = 0cAFcWeA4vkj9K74wUGMYNnrBEzzXw36O92r8DjOI8DtBwtEdoJ4DIDHcWirr4BuJz0zjTFQ298Fp3ouJ2D-QSbUziAb2lzMAvVT6VTyJOgmndYFiZ-55GetjEhHzKrJ4LEwr0tKI7kL1jz1HzmJ2-BchBGGsBt6JICWchGqj64q8ZswRbtN59buW3D7O0eKI9TI_1PIN6p7qeQ9-trGPUCyw7ReYtup4FqbC_XtoUKl7UQuXfDKwZjX5MP7hafPrQdPkXlP2AqYTOrD-2ThhODgZssGDI00Ve1IEl0rPgaLI4xz0shiTuA4LV_f1xWATjln0EGngDD2qcHEPJeCnUYz7XIQq5I7GbRJAp5A90Rl7j8r5En1Qx0CbQEzuskW0HZFnYOJZf_d4jSi7-VMFsF2IgKSt-x2rOoIV-kDcrz14OtxieoFfCFLy-PtXkBBOcYgMdD9qJyMgz_UfwIdZ_6UJf9hCjUFy7Qi1PI_5lFv_svV8ZHOWbnPHTTK1wLr9K3qbcNzZ5U1b3RygWlkjUCn5mT6QRfVXRDHNM__SKG9CjZDwOVh32Tq0mhNLJYpM3FHuWfrqrOW_-8pod-j-8GdgOs0OdMPcDPR6EtFRs2sZ85S-6Uuq_SkNIIVwIWyKcoTcfLj_moOruzyZLmitcuLUJNQJu2hCPsx8v1Ou-p8FVvlpaIrReTHC4etisxcmH22ukc1xnRkbb8jiyXQzJlBzZPDxDtzJp9MrzifosMfFeOX-y25eVjtPd-PvG_1qAeftZNSLpN4J9__FLB0x4qToJEO8P8wqjSeFm6iuiUcFTYXyASYBxC9qa2gitZM-HwHrU_VV4T0x5r-Cl6S-hk1YQhEnEWhvxFc_k6d6jUzz71ZITB4Kd472Wdja6cxku6npH9ezirjJtzUDK8zFAHSbDBwLO86vS83h-zSVVMURrW3JU4m8Xx_emU6KNbKYB_ISzMSmmEhoFRFe2MWA3Iobo5wRR8_yYkd-GsmSCBzPvKQIwxNGIwAGwlJuNoNSooP1DK_QtFJkFA_6idLOcsKDFo0eVpo42fJpO12PJLfzy9hZ_ghMjrrIFyROuiP9baxyRWg04Elw4UxnIoLpU5cBPZssWJf9VL1CtZqaAQenc-Qad5TvYKMRYo9dDKT6IsHRb2o2wSe2f6gQEkqldtVBSW1EV3rhTv-BDevNVpfJF2FeAkwNiUZhB9q8nDGrtNRYsSB43GBcYK2q2pZOw47AGHc9XQHICvfKbjWICCnZV9JMlKh8H5ycbnRmteotgXxEMShnX9cQVpvOMMtWpR0ySo6PUV8PhHw36NL8r3Ed7Ey-w0f5IXogIwAl_Jx5DSYUsqjbpOlqM5KlrLfrcXZLygJ6Q6WUQrxAQ-TkXfMajUxBrkTBrKzJtXp7D6k1gZtZz3F_BLcrgoSvrgQ_4uHLKKgeetfnaeFUTsMlF3kKI0EjHxmUg7-NIXH7aP2Q87WmnWfdcUvFXwI_hp2Brp-Yzg_rM-0cq-sbRWa5PwWsHjjgrKQG5E_WYUJweOHRZb5zej-npVhHVPEDs_bKjelElobvz5qMtkQd1NGbsMraQ0OTtatH_g-uRmM-ZnfKDn03VbrVPG4E99GmDgL9nxenJANYK3PEQr4qAf6gvirqkaOzENpdVLDwzuWl7qR8dVn3xL2_s_HlTjJEZxW0LOqU154Uji0elfQffXUiPNIUuIpYlY5iJNN37WroGYPmdztOof5hP4x4G8ga6EZwxNoAslrfvX6KnXw5K5lIUNOokoc9Foe_M2wg9YWVDOlnM6FwaaA17Rj-oFos-wrrpPGwDvwdIfiYonyzWHsOpBl7HUopUfLIJQBykCHED38E8xURdX7gOp6oafHFoLXrNzUasv2vF3YxO-SDOtgRQlnloCO-0ZDVAo_a0FZA1r6VvjMbm4SzziRuZ16NjIOcXBV84s3Qt6oSVB6Z7gBEZX7dnwTMxW9LPJuP07McquXbQWyUfe9H51BGYltdiQgrRHBMt9Z8V5YcE3Z4ddYpUd5T5ID4N4KXf8wZHC2fEGYsJ2sJuhI-N5u1m98iBdGtYoBhuNOB6sbgTft6Wt04I_y72NPu2vpDR5DP5fM_K9U61KTWhG_QfyaqcFafMHjHbaHD7b3JMh9nfeiuK8NE8GuRWvFo1uVUdJyIvco5P73cFfK5CS8h8H5c14baaIeIm0WY4uIHSYlFjgCNojLM1vmHeiKE1ta5xmSwi2zOX5xR4kXtvR-BRygAvFCRpKIhEmf4Or6RynRxJNCTlShfvwCe2ZoJ1x5L-HAlDdBdifuffewB-AV498XAVKPTeiXEtcwKd2tcJBq-eu_CgQOjDYLTFvArWEKJhlvJX4jvqHJ4wuXM8sEJeTRKjbMnsVe89a-ISp35phgtg_pFMxF5o8Ryp44olHjldRJN_g6Mt_FzwgFxPrLRwJpILYywuW7a4E_721bOz3bCVg
#-------------------------------------
type = success
#-------------------------------------
redirect_to = /subscriptions/component-selection?id=3kxdxr3z71nc
#-------------------------------------
text = Check your email inbox and confirm your subscription.
```

#### ReqDiff | 2026-10-01 18:50
**REQ-ENDPOINT**: `POST` /subscriptions/new-email
**DATAS-ENDPOINT**:
```json
// User A:
	"authenticity_token": "KhU7znxE1I5f12-m8mrCHoohUyf0pA92dP-8_jJ_y7BlE8K4iHVGV2sG4KSG7I5o2kCaECeomQdRraZL8sZt5A"
	"email": "email@gmail.com"
	"g-recaptcha-response": "0cAFcWeA7f7QYb2LiI3F8ufy9LLyD1LDUP4S93rGufhvkFm6BrMDHjWGc88NWhD3S0Xk5I1AqYi4PC8HuEB243Xpbw8HyZatO5vkHkqa4Y8Rd1cLi4MMrrg9E9qy8cOSUwyWtFjjqH9KoW31IQTl_6ue3ezxkPCu0QQ5ccAaqIbJDCXIHD9GbGisBT2ib4YXkKEbVCiWGD5TeZrNaT6iYCqOohdwo3ok699LeaeF5o6m6t1reOEPjAsQSFYBHsPPCE04PAHiOxG7cdLIJ-jDS8LSHGQoSNkH6AEnVLrbRiFdD-raeBO4ESRODU_MkJS0NLUhz376-DuaqsiEL_P9NQ07KRBlWQBQRvGaeiEVjLDF4cIi2vGnpqZub94e76HQRwVCY1Dr_A-wbT86xUWzUq5tjotONRimIl0n_eUk1pVfYL0cN1OJFctR5zVarEf--QqKoJC5V9PONi_8Jcb63eNAhCK5KP4lcg8l1ZNxdWdTX-oPYzXfh6f81WxhTKWichLPs7rdiGHE-iwTqc7Am5ffYaITRdnE-68lk09E4akCVEPRRU9anGlbpKRowoXqgN7tOsWCEJQ6oWF4DORmQ9JbUKRNCgrSOlpYjQLI4Gz4FDuSEOAfwtEro3rXcx7V6tfqqowmGRFwfPR8qMHDauYK1RDDqwQh4wznlLUWqQ8UA_Ovg1GjEbIDR8KO3501a6aW24nEGTptFEdE71UK5LKFcRMcGLzfqzbVDIbZU1hvR-wwz-cK2AqZWfSGcXyi2-1mz8O-SLwGE2oX8xNTy0XZucaxBmMWU23dU3VhSoKyF9kSk54_NC_Zhqr3yDwalUms5s_w8AF_pk0DgEfJC7faKQeUKC4AsaKKg9rdqDdUKfQbcFAOQdyfDScBVNfGzPUZlxofnNM9o24D4KX2zzpNZn26mu_NSVv-jQoWdeC1kPmiLpIdxW2HGdXhfCMNa-t7VcyhqBpJBaRjWfLs6yaNH0HmHkzBJeQzxmPLtpS6SBljkyJr_D57LVON-B-eKeObhLacTE33VtJcQcOwPy9jDHouEeb36IPW88ecpDdfOqG9HPLXKbE14GBYFE7P5KCpG_pqhGmbqQawVTP6CKRm6OAuUgvVwUToM9FyWhSJH91zVembjefoMgEefz0SunGXlr_5EYJy3fvwGCTzRTLm5_pLeM7ujJLpmWDbsb-JfXkq8sHMbVwhxUBq4e0fb3nssWo9VSkfSqHSMh9mkuOtdF7MKT6AX-6Asoo44EcHbkeWUrphwKDu-N1wRUo4eG-YGg7bBdt_e1bTkQnhmnr6E2SqZ4UIVqMKDk7-DV445PQVwGI8g48Ze84z6BSBEBpefbHxXCCw_7_4p0in4KH9KS24lAo0EPVB17Pe1VSdEfZGfevW4z3uyT7EVZMdnJZhYYxDRO81Wr8kxp8z-IdpMZSBbjlfZjk0PEyK7nRzjJWmnK9XdkVMn0OwRw_srGbuvFB4GJsNBKRltqfYSxa7-Cwxj4pKn1YtmIfEMoiqIlW2DyP84jL5zVc1-vBED5qmDeaCWTRtZb_u9F15CPlauTDgmFov3LdjohH--f654zWcMzM8lq2MiH8lHz1b0e_u555eQnDlyXzVUbx5t3kN64uFNSHrKvM8u7_e05Hq0-ANm4QZUSmXMXZX0TzFHb1naRjvN8orhGAlHXFivihKDmLP8pHZk0zNBHe1Ys4XkloVoe2H097MgtfH8ug1D9mbo-UMiPC_JrZ-njhNHJK5ByIipRnzDsn6nHpnXXD8ZmYGB71CtaBf_d--CZbbdYq18wCRMziDORKHwT1IE2VC2pBAk30I8pbu3WCwnz7SA9_Pyn0103mUziXJmXpU5fpSvo66BgzphLtRQXx1slD5rQ-hp1OTtlCguSF1IicFcGMzKI2P45NYINUQxpKMK_y0euAWKXKUvMIY3POSw9Cy-v2pDjJRDb6jw3p6kGq2yLOs1-FcezKB88ndgiBjz1ed3QK1DanHuO5mgnwZc9lUpD0Wejah4vViYgLj2dN4mW5lZaokdiza_XJHsAtVdXHJZ_RmdEiL8EgtPr6k3XhdLPB_NMKSgF768HMFMUugHLyVNVwn4viCfvyqhhPGYzfxYTkX-1nB80RCiZCCLTOBmy0qqR6RnpvqpgvmuOtAy99vIxxApDpPJPRuGt9DEtsUP1RyBAwO8uUGUTYgf0vUSlUPNmA5diH31hQS2Cs0p7Ui1NIKezdOa4R5lALUpl7daEiTDPGoWtiZslzTRXJswdeFVMvlJE_whxcRmOgHxcbzeR2ZDVF0KT6A88hxsdnCmlFxERklHAvO4Ba-Siv4GOKHn66PlTV5y0IsMAPdhv2F16B0rfYMTYlJEz5bZTugXVB1ki-9s4y5Msz3uCEu7msm-7Ap-3a9j1oq9vo7oa5EJUaGsL0k"
// User B:
	"authenticity_token": "bz5o0IgFW4Q_fK8NLAH_505knStpaBCs6aLNgHGoaN9V0Pclps6qD7B-V3BbyRVAWMF-R71_Rl_XZHOlac_kXg"
	"email": "ali@gmail.com"
	"g-recaptcha-response": "0cAFcWeA4vkj9K74wUGMYNnrBEzzXw36O92r8DjOI8DtBwtEdoJ4DIDHcWirr4BuJz0zjTFQ298Fp3ouJ2D-QSbUziAb2lzMAvVT6VTyJOgmndYFiZ-55GetjEhHzKrJ4LEwr0tKI7kL1jz1HzmJ2-BchBGGsBt6JICWchGqj64q8ZswRbtN59buW3D7O0eKI9TI_1PIN6p7qeQ9-trGPUCyw7ReYtup4FqbC_XtoUKl7UQuXfDKwZjX5MP7hafPrQdPkXlP2AqYTOrD-2ThhODgZssGDI00Ve1IEl0rPgaLI4xz0shiTuA4LV_f1xWATjln0EGngDD2qcHEPJeCnUYz7XIQq5I7GbRJAp5A90Rl7j8r5En1Qx0CbQEzuskW0HZFnYOJZf_d4jSi7-VMFsF2IgKSt-x2rOoIV-kDcrz14OtxieoFfCFLy-PtXkBBOcYgMdD9qJyMgz_UfwIdZ_6UJf9hCjUFy7Qi1PI_5lFv_svV8ZHOWbnPHTTK1wLr9K3qbcNzZ5U1b3RygWlkjUCn5mT6QRfVXRDHNM__SKG9CjZDwOVh32Tq0mhNLJYpM3FHuWfrqrOW_-8pod-j-8GdgOs0OdMPcDPR6EtFRs2sZ85S-6Uuq_SkNIIVwIWyKcoTcfLj_moOruzyZLmitcuLUJNQJu2hCPsx8v1Ou-p8FVvlpaIrReTHC4etisxcmH22ukc1xnRkbb8jiyXQzJlBzZPDxDtzJp9MrzifosMfFeOX-y25eVjtPd-PvG_1qAeftZNSLpN4J9__FLB0x4qToJEO8P8wqjSeFm6iuiUcFTYXyASYBxC9qa2gitZM-HwHrU_VV4T0x5r-Cl6S-hk1YQhEnEWhvxFc_k6d6jUzz71ZITB4Kd472Wdja6cxku6npH9ezirjJtzUDK8zFAHSbDBwLO86vS83h-zSVVMURrW3JU4m8Xx_emU6KNbKYB_ISzMSmmEhoFRFe2MWA3Iobo5wRR8_yYkd-GsmSCBzPvKQIwxNGIwAGwlJuNoNSooP1DK_QtFJkFA_6idLOcsKDFo0eVpo42fJpO12PJLfzy9hZ_ghMjrrIFyROuiP9baxyRWg04Elw4UxnIoLpU5cBPZssWJf9VL1CtZqaAQenc-Qad5TvYKMRYo9dDKT6IsHRb2o2wSe2f6gQEkqldtVBSW1EV3rhTv-BDevNVpfJF2FeAkwNiUZhB9q8nDGrtNRYsSB43GBcYK2q2pZOw47AGHc9XQHICvfKbjWICCnZV9JMlKh8H5ycbnRmteotgXxEMShnX9cQVpvOMMtWpR0ySo6PUV8PhHw36NL8r3Ed7Ey-w0f5IXogIwAl_Jx5DSYUsqjbpOlqM5KlrLfrcXZLygJ6Q6WUQrxAQ-TkXfMajUxBrkTBrKzJtXp7D6k1gZtZz3F_BLcrgoSvrgQ_4uHLKKgeetfnaeFUTsMlF3kKI0EjHxmUg7-NIXH7aP2Q87WmnWfdcUvFXwI_hp2Brp-Yzg_rM-0cq-sbRWa5PwWsHjjgrKQG5E_WYUJweOHRZb5zej-npVhHVPEDs_bKjelElobvz5qMtkQd1NGbsMraQ0OTtatH_g-uRmM-ZnfKDn03VbrVPG4E99GmDgL9nxenJANYK3PEQr4qAf6gvirqkaOzENpdVLDwzuWl7qR8dVn3xL2_s_HlTjJEZxW0LOqU154Uji0elfQffXUiPNIUuIpYlY5iJNN37WroGYPmdztOof5hP4x4G8ga6EZwxNoAslrfvX6KnXw5K5lIUNOokoc9Foe_M2wg9YWVDOlnM6FwaaA17Rj-oFos-wrrpPGwDvwdIfiYonyzWHsOpBl7HUopUfLIJQBykCHED38E8xURdX7gOp6oafHFoLXrNzUasv2vF3YxO-SDOtgRQlnloCO-0ZDVAo_a0FZA1r6VvjMbm4SzziRuZ16NjIOcXBV84s3Qt6oSVB6Z7gBEZX7dnwTMxW9LPJuP07McquXbQWyUfe9H51BGYltdiQgrRHBMt9Z8V5YcE3Z4ddYpUd5T5ID4N4KXf8wZHC2fEGYsJ2sJuhI-N5u1m98iBdGtYoBhuNOB6sbgTft6Wt04I_y72NPu2vpDR5DP5fM_K9U61KTWhG_QfyaqcFafMHjHbaHD7b3JMh9nfeiuK8NE8GuRWvFo1uVUdJyIvco5P73cFfK5CS8h8H5c14baaIeIm0WY4uIHSYlFjgCNojLM1vmHeiKE1ta5xmSwi2zOX5xR4kXtvR-BRygAvFCRpKIhEmf4Or6RynRxJNCTlShfvwCe2ZoJ1x5L-HAlDdBdifuffewB-AV498XAVKPTeiXEtcwKd2tcJBq-eu_CgQOjDYLTFvArWEKJhlvJX4jvqHJ4wuXM8sEJeTRKjbMnsVe89a-ISp35phgtg_pFMxF5o8Ryp44olHjldRJN_g6Mt_FzwgFxPrLRwJpILYywuW7a4E_721bOz3bCVg"
```

**RESPONSE-DIFF** (max 10 lines)
```json
// User A:
	"redirect_to": "/subscriptions/component-selection?id=btdcp6zh12nm"
// User B:
	"redirect_to": "/subscriptions/component-selection?id=3kxdxr3z71nc"
```
