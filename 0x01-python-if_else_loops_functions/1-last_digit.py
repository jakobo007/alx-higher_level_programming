#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10 if number >= 0 else -(abs(number) % 10)
str = "Last digit of {} is {}".format(number, last_digit)
if last_digit > 5:
    print(f"{str} and is greater than 5")
elif last_digit == 0:
    print(f"{str} and is 0")
elif (last_digit < 6) and (last_digit != 0):
    print(f"{str} and is less than 6 and not 0")
