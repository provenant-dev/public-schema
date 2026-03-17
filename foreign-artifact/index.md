## Foreign Artifact

### Purpose

A Foreign Artifact ACDC is a wrapper that gives foreign credential types
or arbitrary non-credential data the attributes that it needs to participate
fully in an ACDC data graph.

The world is full of credential and quasi-credential data types: X509 certs,
W3C VCs, SD-JWTs, AnonCreds, ISO mDOC/mDL, a variety of tokens, and various
flavors of signed PDF. These formats have various ways to identify an artifact
and to point to parties that have a role relative to an artifact -- but we may
still want them to participate in ACDC data graphs. ([Verifiable Voice Protocol](https://datatracker.ietf.org/doc/draft-hardman-verifiable-voice-protocol/) is an example of a standard that explicitly contemplates such integration.)

In addition, the world is full of other forms of data that should often be formally
referenced as evidence, but that are not credential-like at all: spreadsheets, documents, photographs, audio and video recordings, genomic data files, videos, musical scores, and arbitrary binary data. It is not clear how to cite such data in an ACDC.

A Foreign Artifact credential bridges these worlds providing a verifiable envelope.
The artifact itself acquires a cryptographic identity either via its existing
signature (if it's a foreign credential type), or through one of the
algorithms defined in the *Bytewise and Externalized SAIDs* specification
(referred to below as the BES specification). The resulting tamper-evident identifier for the foreign artifact — a signature, a bytewise
SAID (bSAID) or externalized SAID (xSAID) — is recorded in the `content_identifier`
field of this ACDC type. The ACDC is then issued by the party attesting
to the artifact's integrity and provenance, and can be cited by a dossier edge
like any other ACDC.

### Relationship to other specifications

When data *inherently* carries a digitally signed (typically, a foreign credential type), the signature of the data is its identifier, and whatever specification describes its signing algorithm becomes normative for how that signature is verified. 

When data isn't inherently signed, it should be referenced as described in BES specification:
*Bytewise and Externalized SAIDs* by Daniel Hardman. Implementers should read
that specification before issuing Foreign Artifact credentials. In particular:

- The **bytewise SAID algorithm** (bSAID) is appropriate for artifacts whose
  byte content can be rewritten after creation by native tooling — for example,
  a JPEG whose Exif metadata can be updated, or a PDF that supports incremental
  updates. The artifact receives an insertion point containing the SAID, making
  the SAID intrinsic to the artifact's bytes.
- The **externalized SAID algorithm** (xSAID) is appropriate for artifacts that
  cannot be safely rewritten after creation — for example, a compressed archive
  or an encrypted file. The SAID is carried in the filename under a constraint
  expressed inside the file content.
- When neither algorithm is practical (for example, a data stream that was
  captured without an insertion point), `content_identifier` MAY hold a plain
  CESR-encoded hash. In this case the artifact does not carry its own SAID, and
  the integrity guarantee is weaker: the hash cannot be discovered by inspecting
  the artifact itself, only by consulting the wrapper credential.

In all cases, the CESR encoding of `content_identifier` is self-describing: the
primitive code identifies the hash algorithm, so no separate algorithm field
is needed.

### What belongs in this credential

A Foreign Artifact credential makes no claim about the *meaning* or *significance*
of the artifact — that interpretation is left to the dossier that cites it and
any applicable governance framework. The credential attests only to:

- The artifact's cryptographic identity (`content_identifier`)
- Its media type (`content_type`)
- Optionally: its size, location, filename, a human-readable description, and a
  provenance statement

For machine-verifiable provenance — for example, proving that a photograph was
captured by a specific device — the appropriate mechanism is an ACDC edge in the
dossier, not the `provenance` text field in this credential.

### Schema

See [fa_schema.json](fa_schema.json).

### Example

The example ([example.json](example.json)) shows a Foreign Artifact credential
wrapping a JPEG photograph of a traffic accident scene. The `content_identifier`
field holds an xSAID, reflected also in the `filename` field. The `provenance`
field records the human-readable chain of custody from the traffic camera to
the insurance adjustor.

### Extension

Implementers MAY define additional fields in the `a` section beyond those
defined in this schema. Any schema that satisfies the following minimum
requirements conforms to the Foreign Artifact contract and MAY be cited as
foreign-artifact evidence in a dossier:

1. The credential MUST be a valid ACDC with no issuee.
2. The `a` section MUST contain `content_identifier` (a CESR-encoded hash) and
   `content_type` (a MIME type string).
3. The `content_identifier` SHOULD be a bSAID or xSAID as defined in the BES
   specification.