## OVC Org Identity Credential

### Purpose

This credential **connects different identifiers for the same organization**, binding legal entity identity to a cryptographic identifier (AID). It is issued to an AID that is provably controlled by the named legal entity, allowing verifiers to confirm that the AID belongs to a real, legally-recognized organization.

This is the foundational trust anchor for the OVC ecosystem. Brand owner credentials, telephone number allocation credentials, and campaign credentials all trace back to an org identity credential as proof that the parties involved are real, accountable legal entities — not anonymous actors.

The OVC Org Identity Credential is analogous in intent to the [LE vLEI](https://docs.origincloud.net/start/concepts/creds/vleis) defined by GLEIF (which maps to LoA 3), but its schema is designed to be simpler and to accommodate a wider range of national registry sources.

![suggested org vet visual](org-vet-256.png)<br>
Suggested visual: [svg](org-vet.svg) | [256 px](org-vet-256.png) | [128 px](org-vet-128.png) | [64 px](org-vet-64.png) | [32 px](org-vet-32.png)

### Levels of assurance

Levels of assurance (LoAs) are well known and often referenced for individual identity; they are less adopted in organizational identity. In the United States, the FBCA [defines](https://www.idmanagement.gov/docs/fbca-cp.pdf) *basic*, *medium*, and *high* assurance for certificates issued to federal agencies, but these LoAs are not typically referenced in other contexts. In the EU, eIDAS ([EU regulation 910/2014](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32014R0910), article 28) defines "nonqualified" and "qualified/QSeal" assurance for certificate issuance &mdash; but its rollout is young, and its application for non-certificate-based technologies is unclear.

Org vet credentials convey a level of assurance with a positive number, where larger numbers map to higher levels of assurance (1 &lt; 2 &lt; 3). Normally, these numbers are expected to be integers, but nuances within a given integer can be modeled by using a floating point value instead (2.1 &lt; 2.2). This allows verifiers to decide what level of assurance will satisfy them, and accept any credential having an LoA >= their threshhold. The meaning of the integer values are defined as follows:

LoA | intended meaning | verification procedures | mappings
--- | --- | --- | ---
1 aka "bronze"| basic proof of control + authorization of requester; no claim about legalities, tools, governance, tools, or competence | <ol><li>Prove that a non-cryptographic identifier (e.g., an LEI) references an org that exists and is not defunct.</li><li>Prove org owns domain.</li><li>Prove requester is human and has email in domain.</li><li>Prove requester has modified a DNS record for the domain to claim the issue's cryptographic identifier (AID).</li></ol> | Similar to FBAC "basic" or eIDAS "nonqual".
2 aka "silver"| cryptographic proof of control + authz, legal accountability, tools; no claim about governance or competence | <ol><li>Satisfy requirements for LoA 1.</li><li>Prove the legal identity of the requester via a digital credential having eIDAS *substantial* assurance, or use a physical credential that meets ISO/IEC 2915 LoA2 or NIST IAL2 requirements.</li><li>Prove cryptographically (e.g., using a [GCD credential](../gcd/index.md) and/or a KERI delegated AID) that the requester was authorized by the org to request a credential for it.</li><li>Use at least 1 witness for the org's AID.</li></ol> | Similar to FBAC "medium", X509 extended verification, or eIDAS nonqual with deep vet. However, not a perfect analog; we are proving that the org has the tools to maintain their identity for a long time.
3 aka "gold" | <ol><li>Satisfy requirements for LoA 2.</li><li>Prove that the requester has legal signing authority for the org.</li></li>Prove that the org has a multisig signing committee to manage risk and human turnover.</li><li>Issue the credential in a ceremony where it is proved that there is no MITM between any two members of the signing committee, and between each member of the signing committee and at least one external observer.</li><li>Require that the AID of the org use enough witnesses to reliably detect and recover from duplicity.</li></ol> | This approximates FBAC "high" and eIDAS "QSeal", but goes slightly beyond. It maps directly to the LE vLEI defined by GLEIF.
4 aka "platinum" | TBD, but could require use of hardware security and/or proof of specialized org attributes such as a security clearance. | none




### Schema

See [ovc-org-vet.schema.json](ovc-org-vet.schema.json).

### Legal identifiers (`legalIdentifiers`)

The `legalIdentifiers` field lists the external identifiers the vetter used to confirm the organization's existence and attributes at the time of issuance. Each entry has a `type` (the registry or source) and a `value` (the identifier within that registry).

**At least one identifier should be globally unambiguous and portable across jurisdictions** — typically an LEI. National registry IDs (like UK Companies House `gb` or Swiss `che` numbers) are also valid and can coexist with the LEI.

Domain names and social media handles are intentionally excluded: they do not unambiguously identify a legal entity across jurisdictions.

Examples of valid types:

| type | example value | source |
|---|---|---|
| `lei` | `5493001KJTIIGC8Y1R12` | GLEIF (ISO 17442) |
| `uk-crn` | `01234567` | UK Companies House |
| `che` | `CHE-123.456.789` | Swiss UID Register |
| `us-ein` | `12-3456789` | US IRS EIN |
| `duns` | `123456789` | Dun & Bradstreet |
| `edgar` | `0001234567` | US SEC EDGAR |

### Levels of Assurance (`LOA`)

The `LOA` field is a positive number where larger values denote higher assurance. Integer values represent defined tiers; decimal sub-values (e.g., 2.1) allow nuance within a tier. Verifiers should accept any credential where `LOA >= their required threshold`.

| LOA | Informal name | Intended meaning |
|---|---|---|
| 1 | Bronze | Basic proof of control + authorization of requester; no claim about legalities, tools, or governance. |
| 2 | Silver | Cryptographic proof of control + legal accountability and tooling; no claim about governance or competence. |
| 3 | Gold | Full legal signing authority proven; multisig signing committee; ceremony with no MITM. Equivalent to LE vLEI (GLEIF). |
| 4 | Platinum | TBD — reserved for hardware security or specialized org attributes (e.g., security clearance). |

### Edge structure

The `e` (edges) block is optional. When present, it may contain:

| Edge | Required in block? | Purpose |
|---|---|---|
| `issuer` | No | Links to an identity credential proving the identity of the issuing vetter (OVC). Uses `I2I` operator — the issuer AID of this credential must be the issuee AID of the referenced credential. |

### Rules and governance

The `r` (rules) block uses citation-style rules inherited from the credential design: the listed legal identifiers are citations — they point to external registry records. When the rules block is expanded (object form), it MUST contain `governance` and MAY include:

- `onlyCommitToPoint` — Pointing to an identifier does **not** imply endorsement of or agreement with the cited content.
- `useViaEdges` — The credential is not meant to be used in isolation; its semantics are communicated via referencing ACDCs.
- `undefinedVerification` — Verifying the authenticity of the cited external data is the verifier's responsibility.
- `undefinedRevocation` — Revocation of the credential and revocation of the cited data are independent events.
- `governance` — Identifies the governance framework under which the credential was issued.

### Multichannel readiness

This credential is entirely channel-agnostic. It asserts the legal identity of an organization, regardless of how that organization communicates (voice, SMS, web, etc.). It is a building block used by channel-specific credentials, not a channel-specific credential itself.

