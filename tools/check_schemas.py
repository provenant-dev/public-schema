#!/usr/bin/env python3
import sys
import os
import re
import json
from jsonschema import Draft202012Validator, exceptions as jsonschema_exceptions

IGNORE_FILE = os.path.join(os.path.dirname(__file__), ".ignore_check_schemas")
error_count = 0
ignore_regexes = []
folders = []
schemas_as_json = []  # List of (filename, jsonobj)

def load_ignore_regexes():
    global ignore_regexes
    if os.path.exists(IGNORE_FILE):
        with open(IGNORE_FILE, "r") as f:
            ignore_regexes = [re.compile(line.strip()) for line in f if line.strip()]
    else:
        ignore_regexes = []

def report_error(msg):
    global error_count
    for regex in ignore_regexes:
        if regex.search(msg):
            return  # Suppress error
    print(msg, file=sys.stderr)
    error_count += 1

def check_nothing():
    # Placeholder for a real check
    pass

# Helper to get repo root
def get_repo_root():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def populate_folders():
    global folders
    repo_root = get_repo_root()
    exclude = {"tools", "venv", "env"}
    for name in os.listdir(repo_root):
        path = os.path.join(repo_root, name)
        if os.path.isdir(path) and not name.startswith(".") and name not in exclude:
            folders.append(name)

def check_folder_names():
    kabob_case_re = re.compile(r'^[a-z0-9]+(-[a-z0-9]+)*$')
    for folder in folders:
        if not kabob_case_re.match(folder):
            report_error(f"Folder name '{folder}' is not lower-case kabob-case.")

def check_0_schema_basics():
    global schemas_as_json
    repo_root = get_repo_root()
    for folder in folders:
        schema_file = os.path.join(repo_root, folder, f"{folder}.schema.json")
        if not os.path.isfile(schema_file):
            report_error(f"Missing schema file: {schema_file}")
            continue
        # Check valid JSON
        try:
            with open(schema_file, "r") as f:
                schema = json.load(f)
                schemas_as_json.append((schema_file, schema))
        except Exception as e:
            report_error(f"Invalid JSON in {schema_file}: {e}")
            continue
        # Check valid JSON Schema
        try:
            Draft202012Validator.check_schema(schema)
        except jsonschema_exceptions.SchemaError as e:
            report_error(f"Invalid JSON Schema in {schema_file}: {e}")

def check_json_fragments():
    repo_root = get_repo_root()
    for folder in folders:
        folder_path = os.path.join(repo_root, folder)
        for fname in os.listdir(folder_path):
            if fname.endswith(".json") and not fname.endswith(".schema.json"):
                fpath = os.path.join(folder_path, fname)
                try:
                    with open(fpath, "r") as f:
                        json.load(f)
                except Exception as e:
                    report_error(f"Invalid JSON in {fpath}: {e}")

def check_fields():
    pattern_re = r'^(?:[BE][A-Za-z0-9_-]{43}|0[DEFG][A-Za-z0-9_-]{86})$'
    dt_regex = re.compile(r'.*\Wdt$')
    field_type_map = {}
    a_field_type_map = {}
    for filename, schema in schemas_as_json:
        props = schema.get('properties', {})
        for field, spec in props.items():
            ftype = spec.get('type')
            # Error if no type declared
            if ftype is None:
                report_error(f"In {filename}: Field '{field}' has no declared type.")
                ftype = 'unknown'
            field_type_map.setdefault(field, set()).add(ftype)
            # Check rules for d, i, s, ri
            if field in {"d", "i", "s", "ri"}:
                if ftype != "string":
                    report_error(f"In {filename}: Field '{field}' should be type string, got {ftype}.")
                pattern = spec.get('pattern')
                if pattern != pattern_re:
                    report_error(f"In {filename}: Field '{field}' should have pattern '{pattern_re}', got '{pattern}'.")
            # Check rule for dt and any field matching .*\Wdt$
            if field == "dt" or dt_regex.match(field):
                if ftype != "string":
                    report_error(f"In {filename}: Field '{field}' should be type string, got {ftype}.")
                fmt = spec.get('format')
                if fmt != "date-time":
                    report_error(f"In {filename}: Field 'dt' should have format 'date-time', got '{fmt}'.")
        # Also check fields inside /properties/a/properties
        a_spec = props.get('a')
        if a_spec:
            a_type = a_spec.get('type')
            if a_type != 'object':
                report_error(f"In {filename}: Field 'a' should be type object, got {a_type}.")
            # Handle oneOf or direct object
            a_props = None
            if a_type == 'object' and 'properties' in a_spec:
                a_props = a_spec['properties']
            elif 'oneOf' in a_spec:
                for option in a_spec['oneOf']:
                    if option.get('type') == 'object' and 'properties' in option:
                        a_props = option['properties']
                        break
            if a_props:
                for field, spec in a_props.items():
                    ftype = spec.get('type')
                    if ftype is None:
                        report_error(f"In {filename} (/a/properties): Field '{field}' has no declared type.")
                        ftype = 'unknown'
                    a_field_type_map.setdefault(field, set()).add(ftype)
                    # Check rule for dt and any field matching .*\Wdt$
                    if field == "dt" or dt_regex.match(field):
                        if ftype != "string":
                            report_error(f"In {filename} (/a/properties): Field '{field}' should be type string, got {ftype}.")
                        fmt = spec.get('format')
                        if fmt != "date-time":
                            report_error(f"In {filename} (/a/properties): Field 'dt' should have format 'date-time', got '{fmt}'.")
    # Output field name -> data types pairs for user
    print("Root field name -> data types:", file=sys.stderr)
    for field, types in field_type_map.items():
        print(f"  {field}: {', '.join(types)}", file=sys.stderr)
    print("a/properties field name -> data types:", file=sys.stderr)
    for field, types in a_field_type_map.items():
        print(f"  {field}: {', '.join(types)}", file=sys.stderr)

def main():
    # Set working dir to repo root
    os.chdir(get_repo_root())
    load_ignore_regexes()
    populate_folders()
    # Find all check_* functions
    check_funcs = [v for k, v in sorted(globals().items()) if k.startswith("check_") and callable(v)]
    for func in check_funcs:
        func()
    if error_count > 0:
        sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    main()
