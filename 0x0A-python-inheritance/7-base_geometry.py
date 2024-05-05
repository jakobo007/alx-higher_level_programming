#!/usr/bin/python3
"""my class"""
class BaseGeometry:
    """Public instance method that raises an Exception """
    def area(self):
        """Raises an Exception with message"""
        raise Exception("area() is not implemeted")

    """Public instance method that validates value"""
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        self.value = value
        self.name = name
