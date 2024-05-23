import json
import os
import re

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

def register_all():
    my_folder = os.path.dirname(os.path.abspath(__file__))
    root = os.path.abspath(os.path.join(my_folder, '../../'))
    schemas = {}
    os.chdir(root)
    for item in os.listdir(root):
        if '.' not in item:
            path = os.path.join(root, item)
            if os.path.isdir(path):
                schema, sads = get_schema_and_sads(path)
                for sad in sads:
                    cmd = f"python3 tools/cli/saidify_sad.py --file {path}/{sad} -l d"
                    print('\n' + cmd)
                    os.system(cmd)
                if schema:
                    schema_file = f"{path}/{schema}"
                    cmd = f"python3 tools/cli/saidify_schema.py --file {schema_file}"
                    print()
                    os.system(cmd)
                    id = get_id(schema_file)
                    schemas[id] = f"{item}/{schema}"
    with open('schemas.json', 'w') as f:
        json.dump(schemas, f, indent=2)

if __name__ == '__main__':
    register_all()