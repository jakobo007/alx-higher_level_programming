#!/usr/bin/python3
"""A class Student that defines a student"""


class Student():
    """Attributes intialization"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """Public method"""
    def to_json(self, attrs=None):
        """Return a dictionary representation of the student."""
        if attrs is None or not isinstance(attrs, list):
            return {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
            }
        else:
            return {
                key: getattr(self, key) for key in attrs if hasattr(self, key)
            }

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
