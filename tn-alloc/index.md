## Telephone Number Allocation Credential

### Purpose

This credential proves that an enterprise or individual holds the **right to use (RTU)** one or more specific telephone numbers. The right-to-use may come directly from a telecommunications regulator or may be sub-allocated through a telephone number provider. The credential is channel-agnostic: the same number can carry voice calls, SMS messages, or both, and a single Telephone Number Allocation Credential covers the number regardless of channel.

### Why this credential matters

In telephony fraud and spam ecosystems, a caller or sender can trivially spoof any number they choose. Downstream recipients — call analytics platforms, carriers, campaign registries — have no way to distinguish a legitimate originator from a bad actor by looking at the calling number alone. The Telephone Number Allocation Credential establishes a cryptographic chain of custody from the regulator (who originally assigned the number block) to the enterprise that legitimately operates the number today.

A verifier who holds this credential, together with the edges that chain back to the regulating authority, has a strong basis to assert that a call or message from the claimed number was originated by the holder of this credential — and only that holder.

### Schema

See [tn-alloc.schema.json](tn-alloc.schema.json).

### Number expressions

The `numbers` attribute is an array of **number expressions**. Each expression is either:

- A **single E.164 number** — e.g., `+15551234567`
- An **inclusive range** — two E.164 numbers joined by a hyphen, e.g., `+15551230000-+15551239999`

All numbers in a single credential must share the **same granting authority** — the issuer uses a single edge to point to the party that granted the right to use those numbers. If a holder has numbers from two different source authorities, they must hold two separate credentials.

Verifiers evaluate each expression in the array. For a single number, it must match exactly. For a range, the number under test must be numerically between the start and end values, inclusive.

### Multichannel readiness

This schema supports both **voice** and **SMS** use cases without modification:

- For **voice**, the holder uses the credential to assert origin identity when initiating a call.
- For **SMS / A2P campaigns**, the holder presents this credential to a campaign registry (e.g., The Campaign Registry) as proof of number ownership before campaign provisioning. The credential does not carry a campaign ID — campaign-level attributes belong in a separate campaign credential that references this one.

The credential is channel-agnostic: it is valid for any use of the allocated numbers and does not restrict to a specific channel. This design keeps number ownership and campaign intent cleanly separated, avoiding schema proliferation and making it easy to reuse the same number credential across multiple campaigns or channels over time.

### Optional fields

| Field | Type | Purpose |
|---|---|---|
| `startDate` | ISO-8601 datetime | Earliest date from which the allocation is valid. Useful for proving long-term continuous ownership. |
| `endDate` | ISO-8601 datetime | Expiry date of the allocation. If absent, the allocation is open-ended and governed solely by credential revocation. |

### Edge structure

The `e` (edges) block is optional to accommodate **regulators** who originate numbers directly and have no parent issuer. When present, the edges block may contain:

| Edge | Required in block? | Purpose |
|---|---|---|
| `tnalloc` | No | Chain to a parent Telephone Number Allocation Credential, proving sub-allocation authority all the way back to the regulator. |
| `issuer` | No | Links to an identity credential (e.g., Org Identity, vLEI) that proves who the issuer is. Intentionally generic — does not constrain the schema of the identity credential. |

### Rules and governance

The `r` (rules) block must contain:

- **`noSharing`** — The credential holder agrees not to share or lend the allocated numbers to other parties in a way that would obscure traffic origin. This rule exists because phone numbers are the accountability anchor for calls and messages: if a number is informally lent, regulators and recipients lose the ability to trace bad traffic back to a responsible party.
- **`governance`** — A statement identifying the governance framework under which this credential was issued. Issuers must populate this field with the URI of their applicable governance document.

The act of issuing or accepting this credential constitutes binding acceptance of these rules.