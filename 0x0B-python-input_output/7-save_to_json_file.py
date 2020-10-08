#!/usr/bin/python3
"""save_to_json_file"""


def save_to_json_file(my_obj, filename):
    """Writes an Object JSON"""
    import json
    with open(filename, 'w') as fl:
        fl.write(json.dumps(my_obj))
