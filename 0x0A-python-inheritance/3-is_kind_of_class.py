#!/usr/bin/python3
"""Function to check if object is same class or inherit from"""


def is_kind_of_class(obj, a_class):
    """Returns true if the object is an instance of or if the object is""" 
    """an instance of a class that inherited from
    otherwise return false
    """
    return isinstance(obj, a_class)
