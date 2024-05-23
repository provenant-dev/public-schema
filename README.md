## Public Schema
This repo holds [ACDC](https://trustoverip.github.io/tswg-acdc-specification/draft-ssmith-acdc.html) schemas authored by Provenant that might be useful to a broad audience. Typically, schemas here are also registered in the community schema repo at https://github.com/WebOfTrust/schema.

All released schemas are enumerated in [registry.json](registry.json). This makes them discoverable in simple code, without crawling.

>NOTE: You can use the `register_all.py` script to regenerate all SAIDs and schemas, and rebuild the registry.json file. You can also use the `saidify-schema.py` or `saidify-sad.py` scripts to do lower-level work with the schema files. You must have keri installed (`pip install keri`) first.