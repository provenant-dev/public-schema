## Awards

### Purpose
This type of verifiable data embodies official praise of the issuee by an issuer. Usually, the issuer is an organization, and the recipient is an individual (e.g., a staff member). However, the schema and use cases are flexible &mdash; an individual can give another individual an award, and an organization can give an award to someone other than an employee. Awards do not necessarily confer privileges (and thus, are unlike most credentials). However, they do prove that the recipient received a formal recognition. A particular verifier can decide to confer privileges based on the award, if they wish.

### Suggested visual
As a general category, awards might be visualized like this: 

![suggested org award visual](award-256.png)<br>
[1024 px](award-1024.png) | [256 px](award-256.png) | [64 px](award-64.png) | [32 px](award-32.png)

However, each instance of an award supports inclusion of a unique image -- or subcategories can be defined that all share a common visual representation.

### Schema
Individual fields are described in [award.schema.json](award.schema.json). Some notable features:

* Awards can have an optional category (e.g., it's a Nobel prize, specifically in the *literature* category).

* Awards can have an optional timeframe (e.g., it's an employee=of-the-month award, specifically in the July 2026 timeframe).

* Awards can have an optional citation (e.g., it's a certified world record for the marathon, specifically "For running the 2024 Olympic Marathon in Paris in 2:01:03").

* Awards can have an optional image (e.g., it's a employee recognition that comes with a physical trophy, which is pictured in this image).

* The edges section is optional, meaning that these credentials may or may not chain to anything else. If present, it contains a single field, "issuer", that links to another credential of any type. vLEI credentials are recommended, if available.

* The rules section is also optional. If present, it is just the SAID of rules that are published elsewhere. Very formal awards like the Oscars, the Nobel prize, or an Olympic medal may have carefully defined rules; casual employee recognitions may have no strong rules about acceptance or usage.

### Graduated disclosure
Generally, recipients of an award want to share the award broadly, because it enhances their public reputation. However, awards may contain a recipient's name, and the recipient may want to prove they've received the award before they prove their name: "I will comment on this policy question as a recipient of a Nobel prize in economics, but I don't want to be quoted by name on the record." Also, an award may contain a formal citation that is identifying (or embarrassing, or irrelevant) in some contexts, and it may contain a data URL for an image, which could make the expanded form of the credential large.

Therefore, awards support the following layers of disclosure:

* compact
* partial (adds issuer_name, category, timeframe, SAID of details)
* full (adds details: issuee_name, citation, image)

### Governance Framework

These credentials are governed by rules to enhance assurance, discourage abuse, and keep use cases crisp. The current rules are stated in [rules.json](rules.json) and are identified by SAID `EDzA-H5YR2oc0sEUKzy_one8-jY2dxdOfjtT8PJJQds8`. New governance frameworks can be written that modify these rules, but each credential MUST reference its associated rules (in the `r` field) using a SAID or a similar pointer to immutable content. The act of issuing or receiving a face-to-face credential constitutes binding acceptance of the rules.

