## Citations

### Purpose

This type of verifiable data embodies a formal reference to non-ACDC evidence. Citations resemble affidavits more than credentials; they have no issuee, and do not prove entitlement.


![suggested citation visual](citation-256.png)<br>
Suggested visual: [svg](citation.svg) | [256 px](citation-256.png) | [64 px](citation-64.png) | [32 px](citation-32.png)

### Use cases

Citations could be used to point to:

* Digital credentials such as a [W3C VC](https://www.w3.org/TR/vc-data-model-2.0/) or an [ISO mobile driver's license](https://www.iso.org/standard/69084.html)
* Cryptographically signed data, such as an X509 cert, a Bitcoin transaction, or a DID document
* Arbitrary digital files: invoices, bills of lading, regulatory reports, the score of a symphony that a composer wants to assert as their original work...
* Digital representations of physical evidence: biometric readings, photos of a crime scene, an audio or video interview with a witness, the PDF of a physical affidavit, a genome, a medical lab report, data from sensors and scientific instruments...
* Social media posts, chat transcripts, or the text of SMS/RCS/email messages (which SHOULD be [canonicalized](https://dhh1128.github.io/canonical-quoted-text/form.html) and hashed or [SAIDified](https://dhh1128.github.io/papers/bes.pdf) before citing)
* Physically published books
* Academic publications, legal precedents, and other content types that are referenced in traditional footnotes, endnotes, or bibliographies

Citations enrich KERI's verifiable data ecosystem, allowing it to gain value from numerous high-stakes contexts where evidence already plays a vital role. Imagine an ACDC that documents the outcome of a medical malpractice lawsuit. Instead of limiting itself to a simple assertion that the plaintiff prevailed, such an ACDC could include edges that link to Citation ACDCs: one citing the formal judgment filed with the clerk, another citing videos of expert testimony, another citing X-rays ([DICOM](https://en.wikipedia.org/wiki/DICOM) files), and another citing a key legal precedent according to [Bluebook conventions](https://www.legalbluebook.com/bluebook/v21/quick-style-guide).

### Semantic precision

We commonly assume that a physical or digital signature constitutes an endorsement of the signed content. An issuer signs an ACDC to assert whatever facts the ACDC asserts. Thus, it might be tempting to assume that the issuer of a Citation ACDC is asserting whatever facts are embodied or implied by the cited content. Verifiers MUST NOT make this mistake.

In careful, non-ACDC contexts, a citation proves that the issuer *intentionally referenced* some content, but it does not always mean more. An attorney may remind a hostile witness of what they previously said under oath. A doctor may reference a lab report to raise questions about an internal inconsistency. An academic may list a peer's paper with the express purpose of disagreeing with it.

A Citation ACDC has a similarly narrow meaning. *Analyzed without context* (a crucial caveat) it embodies a cryptographically provable reference by the issuer, and nothing more. It MUST NOT be construed as an endorsement by the issuer of the content it references. This is true whether or not the issuer created that content.

In order to eliminate the caveat about context, Citation ACDCs are designed to be referenced *only* via the edge of another ACDC (a *referencing ACDC*) that clarifies the intended semantics. Much like the running text of an academic paper contextualizes a footnote, the referencing ACDC MUST make it clear what the reference intends.

For example, imagine that Alice and Bob are bitter rivals in an election for the mayor of their town. Because Alice wants to skewer Bob, she creates a new ACDC citation each time Bob makes a counterfactual statement on social media. In isolation, each ACDC citation has no self-evident purpose; an outside observer can only conclude that Alice is curating verifiable evidence. Eventually, Alice assembles a single ACDC to document Bob's foolishness. Her ACDC has a dozen edges, one for each citation, and when Alice presents it to journalists, it becomes clear that she's using the citations to dispute Bob's commitment to facts.

Suppose Alice loses the debate and the election, and goes back to her original job as a professor at the local community college. In the class she teaches on social media marketing, she can use the same citations in an ACDC that shows interesting examples of creative copywriting; context now takes factuality off the table and makes the purpose of the citations instructive rather than political.

Verifiers MUST also remember that even when a citation exists for the simple purpose of supporting an assertion that the issuer endorses, the mere existence of the citation does not prove the referenced content accomplishes its purpose. A citation may point to content that doesn't exist, or to content that exists but is untrustworthy for various reasons. The algorithm that validates ACDCs (fetching key state, verifying a signature, testing revocation, and comparing data and structure to a schema) can prove that an issuer remains committed to a citation &mdash; but only the interaction context between verifier and prover, plus governance, plus possible validation external to the world of ACDCs, can tell a verifier whether cited evidence satisfies their standards of proof.

To guarantee that all of these assumptions remain explicit, every Citation ACDC includes a [rules](rules.json) section that binds all parties to terms and conditions based on proper assumptions. 

### Schema

See [citation.schema.json](citation.schema.json) and also [rules.json](rules.json).

### Governance Framework

These credentials are governed by rules to enhance assurance, discourage abuse, and keep use cases crisp. The current rules are stated in [rules.json](rules.json) and are identified by SAID `EFthNcTE20MLMaCOoXlSmNtdooGEbZF8uGmO5G85eMSF`. New governance frameworks can be written that supplement these rules; see the `gfw` field in the schema. It is also possible to modify or override these rules, by placing a different value in the `r` field. The act of issuing or receiving a GCD credential constitutes binding acceptance of the rules.

