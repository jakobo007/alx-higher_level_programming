#!/usr/bin/python3
"""function to check instance of object"""
def is_same_class(obj, a_class):
    """Returns True if the object is exactly ans instance of the specified class.
    Otherwise false
    """
    return type(obj) == a_class
