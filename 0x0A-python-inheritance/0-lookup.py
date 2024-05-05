#!/usr/bin/python3
"""Function that returs the list of available"""
"""atrributes and methods of an object"""

def lookup(obj):
    """The function and obj is the object"""
    list = dir(obj)
    return list
