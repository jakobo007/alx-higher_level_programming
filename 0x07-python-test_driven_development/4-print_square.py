#!/usr/bin/python3
"""
function that prints a square with the character #.
"""


def print_square(size):
    """
    size is the length of the square
    size must be an integer otherwise rasie Typerror
    if size > 0 raise TypeError
    if size is a float and less than 0 raise a TypeError
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        print('#' * size)
