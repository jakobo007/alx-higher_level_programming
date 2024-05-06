#!/usr/bin/python3
"""Function that appends a string at the end of a text file (UTF8)"""


def append_write(filename="", text=""):  
   
    """if the file doesn't exist it should be created
    Must use with statement
    """
    with open(filename, 'a', encoding="utf-8") as f:
        f.write(text)
        return len(text)
