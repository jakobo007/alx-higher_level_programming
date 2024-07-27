#!/usr/bin/python3
"""Function the peak in an unsorted list of integers"""


def find_peak(list_of_integers):
    """Returns peak of list or none"""
    if not list_of_integers:
        return None

    def binary_search(arr, low, high):
        if low == high:
            return arr[low]

        mid = (low + high) // 2
        if arr[mid] < arr[mid + 1]:
            return binary_search(arr, mid + 1, high)
        else:
            return binary_search(arr, low, mid)

    return binary_search(list_of_integers, 0, len(list_of_integers) - 1)
