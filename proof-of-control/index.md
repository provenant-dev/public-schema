## Proof of Control Credentials

### Purpose

These credentials assert that the issuee has demonstrated to the issuer the ability to control a social media handle, a web site, DNS records, an email account, a phone number, or a similar digital resource. They are NOT used to assert *possession of a physical object* such as a key or a driver's license. 

![suggested proof-of-control visual](proof-of-control-512.png)<br>
Suggested visual: [svg](face-to-face.svg) | [128 px](proof-of-control-128.png) | [64 px](proof-of-control-64.png) | [32 px](proof-of-control-32.png)

### Parties are only identifiers

Many credentials attempt to establish the legal identity of a human or organization, or they directly attach reputation to such an identity. Therefore, issuance must be preceded by strong identity assurance, so the issuer knows for sure which legal identity is receiving the credential.

Proof-of-control credentials are different. As far as the semantics of these credentials are concerned, issuer and issuee are simply identifiers that resolve to cryptographic keys. The issuer says, "I assert that identifier X controls resource Y" -- but makes no claim about whether X is associated with a higher-level identity construct like "Alice" (or Malfoy). Because of this primitive perspective, many of the common man-in-the-middle attacks on credentials are out of scope with proof-of-control (assuming identifier-to-key resolution is robust); there is no "man" to impersonate.

However, a proof-of-control credential can be *combined* (via a common issuee ID) with identity credentials. This allows it to be connected to more ambitious semantics, but also introduces man-in-the-middle issues. These must be handled by the identity credentials.

### Challenge and Response

The parties follows a standard challenge and response pattern to collect and evaluate evidence of the issuee's control:

1. Over any secure or insecure channel, the issuee gives to the issuer a handle, a URL, or similar identifier for the resource that the issuee claims to control. This allows the issuer to interact directly, but in an unprivileged way, with the resource that the issuee claims to control.

2. The issuer generates or captures entropy. This is random number that was unknown before step 1, and that neither party could have predicted in advance.

3. Over any secure or insecure channel, the issuer challenges the issuee to demonstrate a binding between the content of the resource and the entropy. How this happens depends on the nature of the resource.

    1. *Data Sources*: Some resources are widely readable, but can only be updated by the party that controls them. DNS records, social media feeds, and web sites are examples.
   
        In these cases, the issuer communicates the entropy to the issuee, and challenges the issuee to publish within the data source a version of that entropy that is strongly attributable to the issuee's identifier. The issuer then interacts directly with the data source to observe the update.

        >Example: The issuee proves they control a web site by publishing on the site a digital signature over the entropy."

   2. *Data Sinks*: Some resources exhibit the opposite behavior &mdash; they are widely writable (sendable), but readable only by the party that controls them. Email inboxes and phone numbers are examples.
   
        In these cases, the issuer communicates the entropy directly to the data sink (e.g., via an email, an SMS message, or a phone call), and challenges the issuee to prove they can read it. The issuee communicates back to the issuer, in a way that's strongly attributable to the issuee's idetifier, the entropy that they saw.

        >Example: The issuee digitally sign a message to the issuer that says, "You sent me entropy value X."

### Security Considerations

An issuee who does not directly control a resource, but who colludes with or is shadowed by the real controller of the resource to respond to the challenge, is indistinguishable from the real controller in the issuance procedure. This is because such an issuee really *does* control the resource &mdash; they just do so indirectly. Proof-of-control credentials don't distinguish between these cases.

Issuers should make reasonable efforts to ensure that certain assumptions hold, if they want to produce trustworthy credentials. Verifiers should judge their confidence in the credentials with these assumptions in mind, considering the issuer's reputation.

* Data sources really MUST be writable only by the controller (e.g., not a wiki that anybody can update), and data sinks really MUST be readable only by the controller (e.g., not an email distribution list).
* The response of the issuee to the challenge MUST be bound to the issuer's identifier via a cryptographic key. Ideally, this is done at the time the response is created, by affixing a digital signature. However, other methods are conceivable. For example, issuer and issuee could have a trust relationship based not on cryptographic identifiers but on accounts and traditional login. They could do steps 1-3 without cryptographic identifiers, within the trust context of a secure session, and then exchange crypographic identifiers after the fact, and transfer trust from the session to the identifiers. This is suboptimal because the transfer of trust may be clumsy or imperfect or unauditable &mdash; but it may be acceptable in some cases.
* Enough entropy must be used to make the chosen value unguessable to an appropriate level of assurance. Here "appropriate" may be influenced by how much friction is imposed by different resource types and interaction modalities. See the `be` field in the schema.

### Schema
See [proof-of-control.schema.json](proof-of-control.schema.json).
