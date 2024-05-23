# Schema CLI

## Installation

### Dependencies

* Ensure [Python](https://www.python.org/downloads/) `version 3.10.4+` is installed
* Install [Keripy dependency](https://github.com/WebOfTrust/keripy#dependencies) (`libsodium 1.0.18+`)

#### Setup

* Navigate to `tools` directory from root directory:
    ```bash
    cd tools
    ```
* Setup virtual environment(recommended):
    ```bash
    python3 -m venv venv
    ```
* Activate virtual environment:
    ```bash
    source venv/bin/activate
    ```
* If required, update pip in the virtual environment:
    ```bash
    python3 -m pip install --upgrade pip
    ```
* Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```


## Commands

### register_all
`register_all` runs the other commands on all relevant files in the repo, updating whatever SADs and schemas are out-of-date, and re-writing the registry.json file. It takes no arguments.

### saidify_schema

`saidify_schema` command computes self addressing identifier (SAID) of ACDC schema json. It updates value of `$id` property in `a`, `e`, `r` objects(if present) and the `$id` property at root level with the SAIDs.

#### Usage

* Execute `saidify_schema` command from `tools` directory:    
    ```bash
    saidify_schema -f <file path of schema file(JSON) to saidify>
    ```

* Examples:
    ```bash
    saidify_schema -f tn/tn.schema.json

    # OR

    saidify_schema -f a2p-campaign/a2p-campaign.schema.json
    ```

### saidify_sad

`saidify_sad` command computes self addressing identifier (SAID) of the provided self addressing data(SAD) JSON. It updates computed SAID as the value of SAID field label in the JSON as per the argument `field-label`. Possible field label options are `$id`, `@id`, `id`, `i`, `d`.


#### Usage

* Execute `saidify_sad` command from `tools` directory:    
    ```bash
    saidify_sad -f <full file path of file containing SAD JSON to saidify> -l <SAID field label>
    ```

* Examples:
    ```bash

    ## saidify tn/rules.json file
    saidify_sad -f ~/Projects/public-schema/tn/rules.json -l 'd'

    # OR

    saidify_sad -f ~/Projects/public-schema/tn/rules.json -l '$id'
    ```