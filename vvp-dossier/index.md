## Verifiable Voice Dossier

### Purpose

This dossier packages the evidence needed to support a Verifiable Voice Protocol workflow. It is the container that ties together the accountable party, the telephone number allocation, delegated signing authority, and any brand or campaign evidence needed to justify the voice/messaging activity.

The schema is structured so that the dossier itself stays lightweight while the actual proof material lives in the edge block.

### Schema

See [vvp-dossier.schema.json](vvp-dossier.schema.json).

### Basic structure

The dossier has two main parts:

- `a` holds proximate metadata about the dossier itself, including its name, issuance time, assembly time, and purpose.
- `e` holds the evidence graph that links the dossier to the credentials the verifier needs to inspect.

### Required evidence

The current schema requires these edge references:

- `vetting` - proves the identity of the accountable party.
- `tnalloc` - proves right to use the telephone numbers involved.
- `delsig` - proves the signer is authorized to sign on behalf of the legal entity.

### Optional evidence

The schema also supports additional links when the use case needs them:

- `alloc` - accountable party tn managers
- `bownr` - brand ownership evidence.
- `bproxy` - brand proxy evidence for call-center representation.
- `a2pcamp` - A2P campaign evidence tied to the dossier.

### Multichannel readiness

Although the dossier is centered on voice workflows, it already anticipates related messaging evidence. The presence of `tnalloc` and `a2pcamp` lets the same dossier model support cases where a number, a delegated signer, and an approved campaign all need to be shown together.

This is useful when the same accountable party is operating across voice and SMS, because the dossier can carry the shared identity and number evidence once and then reference the channel-specific campaign or authorization material as needed.

### Dossier metadata

The `a` block is where the dossier is identified and described. The schema currently requires:

- `d` - SAID of the attributes block.
- `dt` - issuance datetime.
- `assembly_dt` - the time the dossier was assembled.
- `purpose` - a short statement describing why the dossier exists.

The optional `name` field can be used as a human-readable label.
