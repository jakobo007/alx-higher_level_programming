#!/usr/bin/python3
"""Imported modlues"""
import json
"""Function that returns an object(Python data structure) represented by a JSON string"""


def from_json_string(my_str):

    """we're converting a JSON string to an object"""
    return json.loads(my_str)
