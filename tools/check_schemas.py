#!/usr/bin/env python3
import sys
import os
import re

IGNORE_FILE = os.path.join(os.path.dirname(__file__), ".ignore_check_schemas")
error_count = 0
ignore_regexes = []
folders = []

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
    for name in os.listdir(repo_root):
        path = os.path.join(repo_root, name)
        if os.path.isdir(path) and not name.startswith(".") and name != "tools":
            folders.append(name)

def check_folder_names():
    kabob_case_re = re.compile(r'^[a-z0-9]+(-[a-z0-9]+)*$')
    for folder in folders:
        if not kabob_case_re.match(folder):
            report_error(f"Folder name '{folder}' is not lower-case kabob-case.")

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
