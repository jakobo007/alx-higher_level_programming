#!/usr/bin/python3
"""A class Student that defines a student"""


class Student():

    """Attributes intialization"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """Public method"""
    def to_json(self):
        """Return a dictionary representation of the student."""
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
