#!/usr/bin/python3
"""
A function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Return a new matrix
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if not all(isinstance(value, (int, float)) for value in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(value / div, 2) for value in row] for row in matrix]

    return new_matrix
