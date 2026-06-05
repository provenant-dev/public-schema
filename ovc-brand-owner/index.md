## OVC Brand Owner Credential

### Purpose

This credential is issued to a legal entity that has the **right to use a brand** because it is either the direct owner of the brand or a licensee authorized to act under it. It establishes that a specific organization is the legitimate operator of a brand identity — including its name, logo, contact information, and communications channels.

In voice and messaging ecosystems, the OVC Brand Owner Credential is the mechanism by which a verifier can answer the question: *"Is this call or message legitimately coming from the organization it claims to represent?"* By chaining the brand credential back to both an identity credential (proving the legal entity exists) and a brand authority credential (proving the right to use the brand), a verifier gets cryptographic assurance that the brand presentation is authentic.

### Schema

See [ovc-brand-owner.schema.json](ovc-brand-owner.schema.json).

### Required and optional attributes

The attributes block requires `d` (attributes SAID), `i` (issuee AID), and `dt` (issuance datetime). `vcard` and `goals` are both optional, though in practice a brand owner credential without a `vcard` is of limited use. Both fields may be selectively disclosed.

### Brand attributes (`vcard`)

The `vcard` field is an ordered array of unfolded VCard content lines (RFC 6350). This is the canonical representation of the brand's identity — the information a verifier would present to a call recipient or SMS recipient to describe who is contacting them.

Key conventions:

- Property and parameter names are **upper case**.
- Parameter names appear in **lexicographic order**.
- Telephone number values MUST be in **strict E.164 format** (leading `+`, no spaces or punctuation).
- The `CHATBOT` property is standard and takes a URI value.
- For `LOGO` and other static media URIs, the `HASH` parameter SHOULD be included and MUST be the CESR-encoded Blake3-256 digest of the content at the URI. This prevents a logo from being silently swapped after issuance. Alternatively, a data URI may be used to embed the media directly.
- URIs pointing to mutable content SHOULD NOT be used — if present, the credential asserts only the location, not the content.

Example vcard entries:

```
ORG:Acme Space Travel, Ltd.
NICKNAME:Acme Rockets
CHATBOT:https://acmespacetravel.biz/chat
LOGO;HASH=EK2r6EnDXre2pecTBO8s99j4OtNaaDIhVyr7uGugDhmp;VALUE=URI:https://acmespacetravel.biz/logo64x48.png
TEL;TYPE=support:+14155550199
EMAIL:support@acmespacetravel.biz
URL:https://www.acmespacetravel.biz
ADR;TYPE=work:;;1 Rocket Road;Hawthorne;CA;90250;United States
TZ:America/Los_Angeles
LANG:en-US
```

### Goal codes (`goals`)

The optional `goals` field lists [Hyperledger Aries goal codes](https://bit.ly/49V8YqV) that enumerate the formally-defined activities in which this brand may legitimately engage using the asserted brand attributes. If specified, any activity **not** covered by these goal codes is considered a context in which legitimate use of the brand is not asserted by this credential.

This field is the primary mechanism for **constraining channel and purpose**. For example:
- A brand that only does outbound voice calls would include goal codes for voice.
- A brand that only does A2P SMS marketing would include goal codes for SMS campaigns.
- A brand operating in both channels would include goal codes for both.

This allows a single OVC Brand Owner Credential to serve multiple channels without schema proliferation.

### Edge structure

The `e` (edges) block is optional. When present, it may contain:

| Edge | Required in block? | Purpose |
|---|---|---|
| `issuer` | No | Links to an identity credential (e.g., OVC Org Identity, vLEI) proving the identity of the issuer. Defaults to `I2I` operator. |
| `brandauth` | No | Links to a credential proving brand authority — e.g., a trademark registration or license agreement. Defaults to `I2I` operator. |

### Multichannel readiness

A single OVC Brand Owner Credential is designed to work across voice, SMS, and other channels. The `vcard` field captures the brand's full contact profile; the `goals` field constrains which channels and activities the credential covers. This avoids the need for separate brand credentials per channel.

If a brand's voice and SMS operations have materially different contact information (e.g., different numbers or chatbot endpoints), separate credentials can be issued — but in the common case, one credential is sufficient.

### Rules and governance

The `r` (rules) block must contain:

- **`governance`** — A statement identifying the governance framework under which this credential was issued. Issuers must populate this field with the URI of their applicable governance document.

Additional rules may be present and are governed by the issuer's governance framework.

The act of issuing or accepting this credential constitutes binding acceptance of those rules.
