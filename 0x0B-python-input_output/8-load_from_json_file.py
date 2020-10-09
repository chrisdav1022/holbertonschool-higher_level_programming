#!/usr/bin/python3
"""load_from_json_file"""


def load_from_json_file(filename):
    """Creates from 'JSON file'"""
    import json
    with open(filename, 'r') as fl:
        return json.loads(fl.read())
