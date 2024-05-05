#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Class that inherits from BaseGeometry"""
class Rectangle(BaseGeometry):
    """Instantion of values width and height"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
        