# -*- encoding: utf-8 -*-
"""
Saidify SAD Command
"""
import argparse
import json
import os

from keri.core import coring

parser = argparse.ArgumentParser(description="Saidify(compute SAID) the provided self addressing data(SAD) JSON")

parser.add_argument('--file', '-f', 
                    default="", 
                    required=True,
                    help='full file path of file containing SAD JSON to saidify')

parser.add_argument('--field-label', '-l',
                    default="d",
                    required=True,
                    choices=['$id', '@id', 'id', 'i', 'd'],
                    help='SAID field label in which to inject the computed said. '
                         'Possible values are $id, @id, id, i, d. Default is d.'
                    )

def saidify_sad(args):

    try:
        with open(args.file, 'r') as file:
            sad = json.load(file)
    except json.JSONDecodeError:
        print(f"Error: Invalid SAD JSON.")
        return
    
    if args.field_label not in sad:
        print(f"Error: Missing SAID field labeled {args.field_label} in json.")
        return

    _, output = coring.Saider.saidify(sad=sad, label=args.field_label)

    s = open(args.file, 'w')
    s.write(json.dumps(output, indent=2))
    s.close()

    print(f"File {args.file} updated with SAIDs successsfully!")

def main():
    args = parser.parse_args()
    saidify_sad(args)


if __name__ == "__main__":
    main()