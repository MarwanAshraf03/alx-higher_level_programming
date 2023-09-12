#!/usr/bin/python3
"""Add Item Module"""
import json
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
"""
adds the arguments
of the file to list of
'add_item.json' file
"""


filename = "add_item.json"
ret = []
if os.path.exists(filename):
    ret = load_from_json_file(filename)
for i in range(1, len(sys.argv)):
    ret.append(sys.argv[i])
save_to_json_file(ret, filename)
