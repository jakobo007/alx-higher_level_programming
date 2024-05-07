#!/usr/bin/python3
"""Imported modlues"""
import json
"""Function that writes an object to a text file as JSON"""


def save_to_json_file(my_obj, filename):

    """function implementation
    Must use with statment
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return json.dump(my_obj, f)
   