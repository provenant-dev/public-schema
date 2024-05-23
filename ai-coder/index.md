## AI Coder License

### Purpose
This credential certifies that a software developer has appropriate training and experience to safely use AI tools while writing code.

Coding with AI tools can be fast and productive. However, AIs may misunderstand requirements, hallucinate, suggest unwise dependencies, or provide code with subtle bugs, vulnerabilities, or IP problems. Embedding AIs in software triggers additional concerns. Developers who have an AI coder license are committed to and capable of managing these issues.

### Suggested visual
![suggested visual](ai-coder-256.png)<br>
[svg](ai-coder.svg) | [800 px](ai-coder-800.png) | [256 px](ai-coder-256.png) | [64 px](ai-coder-64.png) | [32 px](ai-coder-32.png)

### Schema
Individual fields are described in [ai-coder.schema.json](ai-coder.schema.json). Some notable features:

* Awards can have an optional category (e.g., it's a Nobel prize, specifically in the *literature* category).

* Awards can have an optional timeframe (e.g., it's an employee=of-the-month award, specifically in the July 2026 timeframe).

* Awards can have an optional citation (e.g., it's a certified world record for the marathon, specifically "For running the 2024 Olympic Marathon in Paris in 2:01:03").

* Awards can have an optional image (e.g., it's a employee recognition that comes with a physical trophy, which is pictured in this image).

* The edges section is optional, meaning that these credentials may or may not chain to anything else. If present, it contains a single field, "issuer", that links to another credential of any type. vLEI credentials are recommended, if available.

### Graduated disclosure
Generally, recipients of an award want to share the award broadly, because it enhances their public reputation. However, awards may contain a recipient's name, and the recipient may want to prove they've received the award before they prove their name: "I will comment on this policy question as a recipient of a Nobel prize in economics, but I don't want to be quoted by name on the record." Also, an award may contain a formal citation that is identifying (or embarrassing, or irrelevant) in some contexts, and it may contain a data URL for an image, which could make the expanded form of the credential large.

Therefore, awards support the following layers of disclosure:

* compact
* partial (adds issuer_name, category, timeframe, SAID of details)
* full (adds details: issuee_name, citation, image)

### Governance Framework

The rules section is optional. If present, it is just the SAID of rules that are published elsewhere. Very formal awards like the Oscars, the Nobel prize, or an Olympic medal may have carefully defined rules; casual employee recognitions may have no strong rules about acceptance or usage.

