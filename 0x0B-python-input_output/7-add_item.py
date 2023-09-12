#!/usr/bin/python3
import sys
save_to_json_file  = __import__("5-save_to_json_file").save_to_json_file 
load_from_json_file  = __import__("6-load_from_json_file").load_from_json_file 
filename = "add_item.json"
with open(filename, "w+", encoding="UTF8") as f:
    ret = list(load_from_json_file(filename))
    ret.append(sys.argv[1:])
    save_to_json_file(ret, filename)