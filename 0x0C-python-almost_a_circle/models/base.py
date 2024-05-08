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
            return json.dumps([obj.to_dictionary() for obj in list_dictionaries])

    @classmethod
    def save_to_file(cls, list_objs):
        """method that writes json rep to a file"""
        if list_objs is None:
            list_objs = []
        json_data = cls.to_json_string(list_objs)
        filename = f"{cls.__name__}.json"
        with open(filename, 'w', encoding="utf-8") as file:
            return file.write(json_data)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the json string representation"""
        if not json_string or json_string == "[]":
            return []
        else:
            return json.loads(json_string)            
    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all the attributes set"""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a JSON file
        or empty list if no file"""
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, 'r', encoding="utf-8") as file:
                json_data = file.read()
                data_list = cls.from_json_string(json_data)
                instances_list = [cls.create(**data) for data in data_list]
                return instances_list
        except FileNotFoundError:
            return []