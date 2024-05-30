# -*- encoding: utf-8 -*-
"""
schema api caching module

"""
import json
import os
from pathlib import Path

from keri.core import scheming


def cacheSchema(registry_file, d):    
    rootDir = os.path.abspath(os.path.join(os.curdir, os.pardir))  # go one directory up from root directory
    print(f"Root schema dir: {rootDir}")    

    registry_path = os.path.join(rootDir, registry_file)
    path = Path(registry_path)
    if not path.exists():
        return d

    print(f"Schema Registry: {registry_path}")
    print()

    with open(registry_path, 'r') as f:
        registry_content = f.read()
        registry = json.loads(registry_content)

        for said, file in registry.items():
            filePath = os.path.join(rootDir, file)
            with open(filePath, 'r') as f:
                ked = json.load(f)
                schemer = scheming.Schemer(sed=ked)
                print(f"caching schema {schemer.said}")
                d[schemer.said] = schemer.raw

    return d
