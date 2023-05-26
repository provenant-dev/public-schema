## BindKey Credentials

These credentials let the controller of an AID make a formal, public declaration that they use another cryptographic key (besides the one bound to their AID) for a particular purpose.

![suggested bindkey visual](bindkey-256.png)<br>
Suggested visual: [svg](bindkey.svg) | [256 px](bindkey-256.png) | [128 px](bindkey-128.png) | [64 px](bindkey-64.png) | [32 px](bindkey-32.png)

Normally, we expect key control to be expressed in the KEL. However, there exist use cases where such things must be externalized. For example, the email security standards SPF, DKIM, and DMARC deal with how a company can force all email from their domain to meet a higher standard of proof (to eliminate phishing and other spoofing). These standards want a company to use RSA keys. We don't really want AIDs to be based on RSA crypto, but it could be useful for orgs to announce to the world that they are using an RSA key for these email security standards.

Schema is in [`bindkey.schema.json`](bindkey.schema.json); an informal example (that looks plausible but won't verify) is in [`example-bindkey.json`](example-bindkey.json).