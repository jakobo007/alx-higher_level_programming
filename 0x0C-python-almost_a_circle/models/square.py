#!/usr/bin/python3
"""Imported module"""
from models.rectangle import Rectangle
"""class Square that inherits from rectangle"""


class Square(Rectangle):
    """class constructor"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.__width = size
        
    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.__width}"

    @property
    def size(self):
        return self.__width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError(f"{self.__width} must be an integer")
        elif value <= 0:
            raise ValueError(f"{self.__width} must be > 0")
        else:
            self.__width = value
            self.__height = value

    def update(self, *args, **kwargs):
        """asignng attributes"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
            else:
                for key, valeu in kwargs.items():
                    setattr(self, key, valeu)

    def area(self):
        return self.width * self.width

    def to_dictionary(self):
        """Return dictionary representation of a square"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }