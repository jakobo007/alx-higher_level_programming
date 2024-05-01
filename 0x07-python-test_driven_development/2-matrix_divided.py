#!/usr/bin/python3"""
"""A function that divides all elements of a mtrix"""
def matrix_divided(matrix, div):
    """
    matrix must be a list of integers or floats otherwise raise typeerror
    each row of matrix must be same size
    div must be a number(integer or float)
    return a new list with the value rounded to 2dp
    """
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for value in row:
            if not isinstance(value, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        row_size = len(matrix[0])
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

    if div == 0:
        raise ZeroDivisionError("division by 0")

    new_matrix = [[round(val / div, 2) for val in row] for row in matrix]

    return new_matrix