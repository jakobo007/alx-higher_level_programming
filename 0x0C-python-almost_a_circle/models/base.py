#!/usr/bin/python3
"""Imported modules"""
import json
"""A class Base"""


class Base:
    """Our Base parent class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the json string rep of list_dictionaries"""
        if not isinstance(list_dictionaries, list):
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """method that writes json rep to a file"""
        if isinstance(list_objs, None):
            list_objs = []
            return list_objs
        json_string_data = cls.to_json_string(list_objs)
        filename = f'{cls.__name__}.json'
        with open(filename, 'w', encoding="utf-8") as f:
            f.write(json_string_data)
