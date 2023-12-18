## Generalized Cooperative Delegation (GCD) Credentials

### Purpose

These credentials document the specifics of a KERI-style cooperative delegation.

The delegation relationship itself is not embodied in a credential, but rather in a special delegate AID that's bound to the delegator's AID via an inception event on the delegate side, and an interaction event in the KEL on the delegator side. See section 2.3.4 in [version 2.6 of the KERI whitepaper](https://github.com/SmithSamuelM/Papers/blob/master/whitepapers/KERI_WP_2.x.web.pdf). This interlocking two-way binding is what gives rise to the term "cooperative delegation", and it is signifcantly more secure and flexible than many other delegation mechanisms.

However, the binding between AIDs only proves the state of the delegation relationship, and defines how it is controlled. It does not specify which specific actions are expected of the delegate, or what constraints govern the exercise of the authority they receive. That is the purpose of the Generalized Cooperative Delegation (GCD) credentials described here. 

![suggested gcd visual](gcd-256.png)<br>
Suggested visual: [svg](gcd.svg) | [256 px](gcd-256.png) | [64 px](gcd-64.png) | [32 px](gcd-32.png)

### Types of authority

In the physical world, authority can be exercised in many modalities, and constraints often take advantage of these modalities. For example, a king might delegate to a treasurer access to the royal vault, and this delegation might take the form of a key that unlocks a door. In such cases, there could never be risk that the treasurer could sign a treaty that sends the kingdom to war, since the door and the treaty have different affordances.

In the digital world, authority may be asserted in many ways, but it is always proved by a digital signature. A delegate always signs something, whether it be a message in the [Trust-Spanning Protocol](https://trustoverip.org/blog/2023/08/31/mid-year-progress-report-on-the-toip-trust-spanning-protocol/), an SMS message, a purchase order, an XBRL report, etc. The fact that they've signed is easily verified; the question GCD credentials answer is whether the delegate had the authority to act in behalf of the delegator when they affixed that signature.

### Schema

See [gcd.schema.json](gcd.schema.json) and also [rules.json](rules.json).

### Constraints

Delegated authority may need to be constrained in many ways. For example, the talent agent for a famous rock 'n roll diva may be able to represent her, subject to constraints like these:

* The agent cannot represent her outside the context of the music business (can't vote on the diva's behalf in an election, can't sign their will, can't make medical decisions).
* The agent may only have authority to represent the diva in a particular geography or language or market.
* The agent's authority may be contingent on the agent remaining licensed by the industry.

GCD credentials allow the issuer to express analogous constraints. They do this with optional constraint fields. For example:

* The `c_goal` field constrains the goal-driven behaviors in which the delegate can engage on behalf of the delegator (e.g., to sign SMS messages, to buy, to sell, to schedule appointments...)
* The `c_pgeo` field constrains the locations in which a physically present delegate can excercise their delegated authority. See [the schema](gcd.schema.json) for details.
* The `c_rgeo` field constrains where a potentially remote delegate can be located while excercising their delegated authority. See [the schema](gcd.schema.json) for details.
* The `c_jur` field constrains the legal jurisdictions in which the delegate can undertake actions with their delegated authority that legally bind the delegator (e.g., to sign a contract on the delgator's behalf).
* The `c_ical` field constrains the days and times, and possibly the URLs, in which the delegate can exercise their delegated authority (e.g., only when, in India's timezone, it is a Saturday or Sunday between midnight and noon, and only in a particular slack channel).
* The `c_proto` field constrains protocol+role combinations in which the delegate can exercise their delegated authority (e.g., the delegate is allowed to play the `getter` role in the `vtp` protocol).
* The `c_prove` field identifies schemas for proof requests in the IPEX protocol; the delegate's authority depends on their ability to prove what the schema demands (e.g., a chauffeur is allowed to drive the delegator's limosine as long as they can prove they have a valid driver's license). *This constraint should not be confused with ACDC edges (chained credentials), which justify the delegator's status in the first place, and which are the SAIDs of concrete credentials rather than identifiers of schemas which could satisfy a constraint.*

Other constraint fields are also defined (see [the schema](gcd.schema.json)), and GCD credentials can contain non-standard constraint fields as well.

All constraint fields have the following semantic rules in common:

1. The name of the field begins with `c_`. If a custom field does not begin with this prefix, it MUST NOT contain a constraint.
2. Each constraint field MUST identify one or more values that are allowed (e.g., with a regex or an allow list). *Within a single field*, constraints that allow multiple values are effectively ORed, meaning that any match is enough to satisfy the constraint for that field. If the `c_jur` field says that valid jurisdictions are `["fr", "de", "in"]`, then the delegator authorizes the delegate to take legally binding actions if they are enforceable in France OR Germany OR India.
3. *Across all constraint fields*, matches are ANDed, meaning that all of the constraints must be satisfied. Building on the previous example of `c_jur`, if the `c_rgeo` field also says that valid locations for the remote delegate are `["fr", "de", "in"]`, then the delegate's actions are valid if they are legally enforceable in one of the 3 legal jurisdictions (first constraint field), AND if the delegate appears to be operating from one of those same 3 countries (second constraint field).

Because of the third rule, these credentails do not support graduated disclosure. All constraints must be disclosed every time a verifier is evaluating delegated authority.

### Governance Framework

These credentials are governed by rules to enhance assurance, discourage abuse, and keep use cases crisp. The current rules are stated in [rules.json](rules.json) and are identified by SAID `EFthNcTE20MLMaCOoXlSmNtdooGEbZF8uGmO5G85eMSF`. New governance frameworks can be written that supplement these rules; see the `gfw` field in the schema. It is also possible to modify or override these rules, by placing a different value in the `r` field. The act of issuing or receiving a GCD credential constitutes binding acceptance of the rules.

