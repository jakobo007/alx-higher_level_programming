#!/usr/bin/python3
"""Imported module"""
import json
"""A function that returns the JSON of an object(string)"""

def to_json_string(my_obj):

    """obj is the object to convert"""
    return json.dumps(my_obj, separators=(',', ':'))
