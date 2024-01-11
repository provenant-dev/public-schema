# -*- encoding: utf-8 -*-
"""
Saidify Schema Command
"""
import argparse
import json
import os

from keri.core import coring, scheming

parser = argparse.ArgumentParser(description="Saidify schema json file")
parser.add_argument('--file', '-f',
                    default="",
                    required=True,
                    help='file path of schema file(JSON) to saidify')

def saidify(args):

    project_root = get_root_dir()
    file_path = os.path.join(project_root, args.file)
    print(f"Start saidify schema json file at path : {file_path}")
    file_name = os.path.basename(file_path)

    try:
        with open(file_path, 'r') as file:
            jsn = json.load(file)
    except json.JSONDecodeError:
        print(f"Error: Invalid schema JSON.")
        return
    
    sad = populateSAIDS(jsn)
    schemer = scheming.Schemer(sed=sad)
    
    s = open(file_path, 'w')
    s.write(json.dumps(schemer.sed, indent=2))
    s.close()

    print(f"Schema file {file_name} updated with SAIDs successsfully!")    

def populateSAIDS(d: dict, idage: str = coring.Saids.dollar, code: str = coring.MtrDex.Blake3_256):
    if 'properties' in d:
        props = d['properties']

        # check for top level ids
        for v in ["a", "e", "r"]:
            if v in props and '$id' in props[v]:
                vals = props[v]
                vals[idage] = coring.Saider(sad=vals, code=code, label=idage).qb64
            elif v in props and 'oneOf' in props[v]:
                if isinstance(props[v]['oneOf'], list):
                    # check each 'oneOf' for an id
                    ones = props[v]['oneOf']
                    for o in ones:
                        if isinstance(o, dict) and idage in o:
                            o[idage] = coring.Saider(sad=o, code=code, label=idage).qb64

    d[idage] = coring.Saider(sad=d, code=code, label=idage).qb64

    return d

def get_root_dir():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))


def main():
    args = parser.parse_args()
    saidify(args)


if __name__ == "__main__":
    main()