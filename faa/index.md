## Foreign Artifact Affidavit (FAA)

### Purpose

A Foreign Artifact Affidavit (FAA, pronounced `/fa/` like the musical syllable) is a wrapper that gives non-ACDC data the attributes that are needed to participate fully in an ACDC data graph. It is a simple but powerful interoperability mechanism.

Modern life is full of credential and credential-like data types: X509 certs, W3C VCs, SD-JWTs, AnonCreds, ISO mDOC/mDL, remote attestations from a secure enclave, a variety of tokens, and various flavors of signed PDF are digital examples; birth certificates, passports, and citizen ID cards are physical examples. Instances of these artifacts have various ways to identify themselves and to point to parties that have a role relative to them -- but we may still want them to participate in standard ACDC data graphs. ([Verifiable Voice Protocol](https://datatracker.ietf.org/doc/draft-hardman-verifiable-voice-protocol/) is an example of an evidence-dependent industry mechanism that explicitly contemplates such integration.)

In addition, we know of other, arbitrary forms of data that often need to be formally referenced as evidence, but that are not credential-like at all: spreadsheets, documents, photographs, audio and video recordings, sensor readings, fingerprints, videos, musical scores, G-codes, blood-glucose measurements, courtroom transcriptions. And non-digital embodiments are also important here: soil samples, biopsies, genomes, analog recordings. It is not clear how to cite arbitrary data in an ACDC.

A FAA places non-ACDC data in an efficient, tamper-evident envelope with predictable metadata. This lets the ACDC ecosystem cite it, reason about it, and verify some of its properties in standard ways.

### Physical to digital

Specifying how to digitize data is out of scope, but we make the simplifying assumption that digitization will occur in some way that's meaningful to ecosystem participants. X-rays and ultrasounds turn into DICOM images, genomes turn into FASTQ or VCF, dental impressions turn into STL, analog signals from a radiotelescope turn into FITS, the bumper of a crashed car turns into photos at the accident scene, and so forth.

### Arbitrary digital to tamper-evident digital

Once a reference version of the data is available digitally, we need a way to refer to it. This reference must be tamper-evident (at least to the fidelity of the sample resolution, if quantized).

ACDCs use hashes of the full content of the data for this purpose. If data lends itself to standard *saidification*, the SAID of the data SHOULD identify it. Otherwise, the [bytewise or externalized SAID algorithms](https://doi.org/10.2139/ssrn.6128466) SHOULD be applied to the data, or the data MAY simply be hashed. In all cases, the resulting digest is encoded as CESR, and in this form becomes the tamper-evident, self-describing way to reference the digital data it derives from. This CESR-encoded digest is stored in the `art_digest` field in the FAA schema. The data identified by this digest is called the *artifact* of the FAA.

### What belongs in this credential

In and of itself, a FAA makes no claim about the *meaning* or *significance* of its artifact. That interpretation is left to the ACDC (e.g., a [dossier](https://trustoverip.github.io/kswg-dossier-specification) that cites it and to any governance framework that provides context. The FAA attests to:

- The artifact's cryptographic identity (`art_digest`)
- Optional metadata about the artifact: content type, size, location, filename, a human-readable description, a
  description of provenance, issuance date
- The issuer's posture with respect to the artifact (`art_posture`): did the issuer merely record `art_digest` at the request of a third party, or witness the artifact directly and compute `art_digest` from it, or actually verify the integrity of the artifact at a particular moment, according to that artifact's native rules?
- The issuer's assertion with respect to revocation of the artifact (`rev_latency`): if the artifact is revoked, does the issuer of the FAA attempt a corresponding revocation of this ACDC -- and if so, how quickly? (Normally, the issuer of an FAA makes no attempt to react to revocation events of its corresponding artifact, either because the artfact has no revocation semantics, or because tracking revocation is a burden on an issuer that's just trying to create a lightweight affidavit. However, if the FAA is issued by an entity that's actively trying to bridge between another credential ecosystem and ACDCs, a non-zero value here allows verifiers to treat the FAA as a proxy for the foreign credential, assuming they trust the FAA issuer.)

### Schema

See [foreign-artifact.schema.json](foreign-artifact.schema.json).

### Example

The example ([example.json](example.json)) shows a FAA wrapping a JPEG photograph of a traffic accident scene. The `art_digest` field holds an xSAID, reflected also in the `filename` field. The `provenance` field records the human-readable chain of custody from the traffic camera to the insurance adjustor.

### Extension

Implementers MAY define additional fields in the `a` section beyond those
defined in this schema.