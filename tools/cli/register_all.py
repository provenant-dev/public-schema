import argparse
import json
import os
import re

parser = argparse.ArgumentParser(description="Register all schemas")

def get_schema_and_sads(folder):
    schema = None
    sads = []
    for item in os.listdir(folder):
        if '.json' in item:
            if 'schema' in item:
                schema = item
            elif 'example' not in item:
                sads.append(item)
    return schema, sads

id_pat = re.compile(r'"\$id"\s*:\s*"(.*?)"')
def get_id(file):
    with open(file) as f:
        match = id_pat.search(f.read())
        if match:
            return match.group(1)

def register_all(args):
    my_folder = os.path.dirname(os.path.abspath(__file__))
    root = os.path.abspath(os.path.join(my_folder, '../../'))
    vlei_dir = 'vLEI/acdc'
    schemas = {}
    os.chdir(root)
    for item in os.listdir(root):
        if '.' not in item:
            path = os.path.join(root, item)
            if os.path.isdir(path):
                print()
                print('processing dir: ' + path)
                schema, sads = get_schema_and_sads(path)
                for sad in sads:
                    cmd = f"python3 tools/cli/saidify_sad.py --file {path}/{sad} -l d"
                    print(cmd)
                    os.system(cmd)
                if schema:
                    schema_file = f"{path}/{schema}"
                    cmd = f"python3 tools/cli/saidify_schema.py --file {schema_file}"
                    print()
                    os.system(cmd)
                    id = get_id(schema_file)
                    schemas[id] = f"{item}/{schema}"
    
    vlei_dir_path = os.path.join(root, vlei_dir)
    for item in os.listdir(vlei_dir_path):
        if item.endswith('.json'):
            print('\nprocessing ' + item)
            schema_file = os.path.join(vlei_dir, item)
            id = get_id(schema_file)
            schemas[id] = f"{vlei_dir}/{item}"

    with open('registry.json', 'w') as f:
        json.dump(schemas, f, indent=2)

def main():
    args = parser.parse_args()
    register_all(args)

if __name__ == '__main__':
    main()