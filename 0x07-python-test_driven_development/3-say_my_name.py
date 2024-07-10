#!/usr/bin/python3
"""
Function that prints name
"""


def say_my_name(first_name, last_name=""):
    """names must be strings"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name:
        return f"My name is {first_name} {last_name}"
    else:
        return f"My name is {first_name}"
