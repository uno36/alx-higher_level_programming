#!/usr/bin/python3
from sys import argv
"""import argv"""

load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
"""import load_from_jason_file function"""

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
"""import save_to_json_file"""

filename = "add_item.json"
try:
    data = load_from_json_file(filename)
    data += argv[1:]
    save_to_json_file(data, filename)
except FileNotFoundError:
    data = argv[1:]
    save_to_json_file(data, filename)
