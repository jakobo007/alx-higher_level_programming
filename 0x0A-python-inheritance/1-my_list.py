#!/usr/bin/python3
"""MyList class that inherits from list"""
class MyList(list):
    """MyList class"""
    def print_sorted(self):
        """Public instance method that prints the list but sorted(ascending)"""
        new_list = print(sorted(self))
        return new_list
