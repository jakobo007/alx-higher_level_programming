#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_num = set()
    for x in my_list:
        if x not in uniq_num:
            uniq_num.add(x)

        return sum(uniq_num)