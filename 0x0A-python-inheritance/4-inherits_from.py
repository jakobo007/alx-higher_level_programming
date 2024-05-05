#!/usr/bin/python3
"""Function to check inheritance of a class"""
def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class that inherited (directly or indirectly from the specified class)
    otherwise False
    """
    return isinstance(issubclass(type(obj), a_class), a_class)
