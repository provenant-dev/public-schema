## Face-to-Face (f2f) Credentials

### Purpose

These credentials document an assertion by one human being, that they have interacted with another human being, face-to-face, in "real" (non-digital, non-remote) life. An individual face-to-face credential provides moderate assurance (with a documented, specific basis) that the issuee is not an AI, an org, or an IoT device. See [this slidedeck](https://docs.google.com/presentation/d/17_QEAt5SIBOrKbZdkPW0K8XYNGyA4Fn8Tg-h0kvJTCE/edit?usp=sharing) for background.

![suggested face-to-face visual](face-to-face-256.png)<br>
Suggested visual: [svg](face-to-face.svg) | [512 px](face-to-face-512.png) | [256 px](face-to-face-256.png) | [128 px](face-to-face-128.png) | [64 px](face-to-face-64.png) | [32 px](face-to-face-32.png)

Face-to-face credentials prove a party's humanness, NOT their identity. They do NOT replace high-assurance credentials such as passports, drivers licenses, or KYC, because they don't make strong claims about most of the legally definitive attributes of the issuees.

It is possible for Alice to work with Bob for years, and to issue Bob a face-to-face credential on that basis (`knownAs = "Bob", basis = "colleague"`), but to not know that Bob's legal name is actually Roberto. It is also possible for Bob to thoroughly deceive Alice about his name. Neither of these issues invalidates Alice's claim that the party she knows as Bob (whatever his legal identity might be) is a human being rather than a piece of technology or a faceless organization. *That* is what a face-to-face credential asserts -- and until we have [more realistic androids](https://futuretechenthusiast.com/10-most-realistic-humanoid-robots/), it is something Alice can decide easily, in even a brief face-to-face interaction.

Knowledge about the existence of real-life humans is generated all the time, with virtually no effort, as we go about our ordinary lives. Thus, face-to-face credentials tap into a source of trust that is cheap, common, and neglected by heavier-weight mechanisms. Importantly, this knowledge is not dependent on institutions; face-to-face credentials democratize and decentralize trust on their focus question, and they limit ["big desk and little people" power imbalances](https://medium.com/@daniel-hardman/big-desks-and-little-people-e1b1b9e92d79). 

Face-to-face credentials might be used to tell the difference between true and fake reports of a news event (since bots claiming to have witnessed the fake events should have trouble proving their humanness). They might be used as a replacement for a CAPTCHA. They might be a requirement for the issuance of other credentials that are intended to be held only by humans.

As with any credential, the trust that a verifier places in an individual face-to-face credential MUST depend on what they know about the issuer (top-level `i` field). Trust SHOULD also be influenced by the data that the issuer offers about the nature and duration of the face-to-face interaction they had with the issuee (`basis` field). Multiple face-to-face credentials from issuers that are widely separated in time, kind, and public reputation are much harder to manipulate. Since high-assurance face-to-face interactions are common (work or school colleagues we've known for years, family and close friends), we hope that people give and get face-to-face credentials regularly, thus creating a web that provides pretty good assurance of humanness in many contexts.

In most situations, face-to-face interactions are reciprocal; each party can achieve similar confidence in the other party's humanness. Reciprocal issuance is encouraged whenever conditions permit.

### Schema
See [face-to-face.schema.json](face-to-face.schema.json) and also [rules.json](rules.json).

### Privacy

Face-to-face credentials allow (but do not require) the issuer to assert the name (`knownAs` field) and/or handles (`confirmedHandles` field) that they have *personally* used to interact with the issuee. They also allow (but do not require) the issuer to endorse the hash of biometrics (e.g., a photo or voice print) that they agree characterized the issuee as they observed them in real life interactions (`biometricHashes` field). The issuee can carry the actual biometric data and present it to verifiers, thus allowing a verifier to confirm that they are interacting with the same human that the issuer knew.

Issuing and later disclosing this information are both optional. Face-to-face credentials support contractually protected and graduated disclosure. Best practice for privacy would be to disclose no more than is strictly required.

By design, face-to-face credentials do not protect the privacy of the issuer. This means they should be issued by a public persona of the issuer, not a highly private one. Issuers and issuees should carefully consider the tradeoff between assurance and privacy that's associated with disclosing the nature of their face-to-face interactions in a face-to-face credential's `basis` field.

### Governance Framework

These credentials are governed by rules to enhance assurance, discourage abuse, and keep use cases crisp. The current rules are stated in [rules.json](rules.json) and are identified by SAID `EDzA-H5YR2oc0sEUKzy_one8-jY2dxdOfjtT8PJJQds8`. New governance frameworks can be written that modify these rules, but each credential MUST reference its associated rules (in the `r` field) using a SAID or a similar pointer to immutable content. The act of issuing or receiving a face-to-face credential constitutes binding acceptance of the rules.

