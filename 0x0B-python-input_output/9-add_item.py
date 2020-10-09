#!/usr/bin/python3
"""Adds all arguments to Python list"""
from sys import argv


save = __import__('7-save_to_json_file').save_to_json_file
load = __import__('8-load_from_json_file').load_from_json_file

try:
    sv = load("add_item.json")
except FileNotFoundError:
    sv = []
for c in argv[1:]:
    sv.append(c)

save(sv, "add_item.json")
