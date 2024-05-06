#!/usr/bin/python3
"""Imported module"""
import json
"""A function that returns the JSON of an object(string)"""


def to_json_string(my_obj):

    """obj is the object to convert to JSON string"""
    """function dumps() takes an object and converts to a """
    return json.dumps(my_obj, ensure_ascii=False, indent=4)
