#!/usr/bin/python3
"""
Module 0-add_integer
function that adds 2 integers
"""


def add_integer(a, b=98):
    """Function to add 2 ints"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a + b)
