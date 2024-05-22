## AI User Code of Conduct Attestation (ai-user-coca)

### Purpose
This verifiable data attests that the issuer is committed to abide by a specific code of conduct in relation to their personal use of AI. It is a public declaration, not a credential. However, it may be cited as evidence that justifies credentials such as an [AI coder license](../ai-coder/index.md). 

### Suggested visual
![suggested visual](scroll-256.png)<br>
[640 px](scroll-640.png) | [256 px](scroll-256.png) | [64 px](scroll-64.png) | [32 px](scroll-32.png)
<br>Image credit: <a href="https://www.kindpng.com/imgv/hRbmxmh_scroll-icon-png-transparent-png/" target="_blank">Иконки Для Сторис @kindpng.com</a>

### Schema
The schema for this data is extremely simple. It only has two fields: `dt` (the issuance date) and `coc` (the code of conduct). The `coc` field SHOULD hold the SAID of a document published elsewhere, OR HTML encoded as a data URL. MAY also contain an ordinary URL. In the latter case, the issuer is asserting a commitment to whatever is published at that location, but not to specific content (since the content can change after the issuance date). This may or may not justify the trust of the verifier.

One example of a recommended code of conduct is provided in [coc1.json](coc1.json). If you would like to reference it in your AI User Code of Conduct attestations, the SAID you should place in the `coc` field is: `EMwE-XevWy8DkCf2oXSsDRjAUuQOXeuVSdKx8BRpCH-g`.