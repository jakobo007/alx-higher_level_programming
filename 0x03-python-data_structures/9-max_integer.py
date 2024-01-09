#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) <= 0:
        return None
    else:
        highestInteger = my_list[0]
        for i in my_list:
            if my_list[i] > highestInteger:
                highestInteger = my_list[i]
            return highestInteger
