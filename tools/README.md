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

### saidify-schema

`saidify-schema` command computes self addressing identifier (SAID) of ACDC schema json. It updates value of `$id` property in `a`, `e`, `r` objects(if present) and the `$id` property at root level with the SAIDs.

#### Usage

* Execute `saidify-schema` command from `tools` directory:    
    ```bash
    saidify-schema -f <file path of schema file(JSON) to saidify>
    ```

* Examples:
    ```bash
    saidify-schema -f tn/tn.schema.json

    # OR

    saidify-schema -f a2p-campaign/a2p-campaign.schema.json
    ```
