#!/usr/bin/python3
"""function that converts an instance of a class with serializable attributes"""
"""into a dictionary that is ready for JSON serialization"""

def class_to_json(obj):
    """Obj is instance of a class
    all it's attributes sre serializable"""

    if not hasattr(obj, "__dict__"):
        return obj

    serial_obj = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serial_obj[key] = value
        elif isinstance(value, type(None)):
            serial_obj[key] = None
        else:
            serial_obj[key] = str(value)
    return serial_obj
