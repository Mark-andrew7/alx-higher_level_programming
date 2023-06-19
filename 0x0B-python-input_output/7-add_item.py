#!/usr/bin/python3
"""
Load, add arguments and save them to a file.
"""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        original_list = load_from_json_file(add_item.json)
    except FileNotFoundError:
        original_list = []
    original_list.extend(sys.argv[1:])
    save_to_json_file(original_list, "add_item.json")
