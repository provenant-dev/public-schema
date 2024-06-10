# Public Schema

This repo holds [ACDC](https://trustoverip.github.io/tswg-acdc-specification/draft-ssmith-acdc.html) schemas authored by Provenant that might be useful to a broad audience. Typically, schemas here are also registered in the community schema repo at https://github.com/WebOfTrust/schema.

All released schemas are enumerated in [registry.json](registry.json). This makes them discoverable in simple code, without crawling. Human-friendly documentation is in index.md files in each subdirectory &mdash; for example, [face-to-face/index.md](face-to-face/index.md).

>NOTE: You can use the `register_all.py` script to regenerate all SAIDs and schemas, and rebuild the registry.json file. You can also use the `saidify-schema.py` or `saidify-sad.py` scripts to do lower-level work with the schema files. See [tools/cli/README.md](tools/cli/README.md).

## Running public schema registry locally

```sh
docker compose up
```

This will start the http server that serves schema json for requested OOBIs. See [API endpoints](tools/README.md#endpoints)

## How to add new schemas

- If the schema is vLEI specific, then create new <schema-name>.json file in either [vLEI](vLEFI) folder or [vLEI/acdc] folder.
- Run docker compose with [register_all](tools/README.md#register_all) command `docker compose up --command=register_all`

## How to trigger build after adding new schema(s)

- Trigger a build manually in `schema-registry-deployment` repo. We don't want to run an automatic build from this public repo as of now. So, the action to trigger build generation and deployment are manual actions.
