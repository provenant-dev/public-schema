## A2P Campaign Credential

### Purpose

A credential issued to a brand that represents a registered A2P messaging campaign and the telephone numbers associated with that campaign.

### Schema

See [a2p-campaign.schema.json](a2p-campaign.schema.json).

### Attributes

The attributes block records the approved campaign and sender context:

| Field | Purpose |
|---|---|
| `brandId` | Legal or registry identifier for the approved organization. |
| `campaignId` | Campaign identifier assigned by the approval authority or registry. |
| `usecase` | Campaign use-case category, such as `Fraud Alert`, `2FA`, or `Public Service Announcement`. |
| `numbers` | E.164 numbers approved for use in the campaign. |
| `authorizedServiceProvider` | Service provider authorized to originate or manage traffic for this campaign. |
| `campaignAttributes` | Subscriber opt-in, opt-out, help, link, and affiliate-marketing attributes used by governance and verifiers. |

The `startDate` and `endDate` fields are optional and can be used when the campaign approval is time-bounded.

### Edge structure

The `e` (edges) block may contain:

| Edge | Purpose |
|---|---|
| `issuer` | Links to an identity credential proving who issued the campaign credential. |
| `tnalloc` | Links to a Telephone Number Allocation credential proving right to use the campaign telephone numbers. |
| `brandid` | Links to a brand or organization identity credential associated with the campaign. |


### Rules and governance

The `r` (rules) block must contain:

- `governance` - A statement identifying the governance framework under which this credential was issued.
