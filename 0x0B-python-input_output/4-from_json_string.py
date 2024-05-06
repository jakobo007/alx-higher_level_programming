#!/usr/bin/python3
import json
"""Function that returns an object(Python data structure) represented by a JSON string"""


def from_json_string(my_str):

    """Function to return JSON representation"""
    return json.dumps(my_str)
