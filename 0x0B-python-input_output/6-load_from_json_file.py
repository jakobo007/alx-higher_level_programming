#!/usr/bin/python3
"""imported Modules"""
import json
"""Function that creates an obj from a JSON file"""


def load_from_json_file(filename):
    """Must use with statement"""

    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
