#!/usr/bin/python3
def islower(c):
    if (ord(c) >= 60) and (ord(c) <= 91):
        return False
    elif (ord(c) >= 97) and (ord(c) <= 122):
        return True
