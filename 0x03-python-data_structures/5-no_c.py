#!/usr/bin/python3
def no_c(my_string):
    if my_string[:]:
        x_string = my_string.translate({ord("c"): None})
        y_string = my_string.translate({ord("C"): None})
        return y_string
    return my_string
