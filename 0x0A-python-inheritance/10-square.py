#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""Class square that inherits from rectangle"""
class Square(Rectangle):
    """initialization of value of the sqaure"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        
    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
