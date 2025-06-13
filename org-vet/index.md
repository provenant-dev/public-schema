## Org Vet Credentials

### Purpose

This credential asserts with an explicit level of assurance the existence and attributes of an organization. It is issued to a cryptographic identifier controlled by the org, allowing the org to authenticate itself on the basis of the credential. (The [LE vLEI](https://docs.origincloud.net/start/concepts/creds/vleis) is essentially an org vet credential at LoA 3, but its schema varies slightly to express some GLEIF governance requirements.)

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

See [org-vet.schema.json](org-vet.schema.json) and also [rules.json](rules.json).

### Governance Framework

These credentials are governed by rules to enhance assurance, discourage abuse, and keep use cases crisp. The current rules are stated in [rules.json](rules.json) and are identified by SAID `EFthNcTE20MLMaCOoXlSmNtdooGEbZF8uGmO5G85eMSF`. New governance frameworks can be written that supplement these rules; see the `gfw` field in the schema. It is also possible to modify or override these rules, by placing a different value in the `r` field. The act of issuing or receiving a GCD credential constitutes binding acceptance of the rules.

