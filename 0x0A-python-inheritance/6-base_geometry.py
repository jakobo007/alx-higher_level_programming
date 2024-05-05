#!/usr/bin/python3
"""my class"""


class BaseGeometry:
    """Public instance method that raises an Exception """
    def area(self):
        """Raises an Exception with message"""
        raise Exception("area() is not implemented")
