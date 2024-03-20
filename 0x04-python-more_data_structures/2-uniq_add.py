#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_num = set()
    if my_list:
        for x in my_list:
            uniq_num.add(x)

        return sum(uniq_num)