#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
reminder = abs(number) % 10
if reminder < 0:
    reminder = -(reminder)
if reminder > 5:
    print("The last digit of {} is {} and is greater than 5".format(number, reminder))
elif reminder == 0:
    print("The last digit of {} is {} and is 0".format(number, reminder))
elif (reminder < 6) and (reminder != 0):
    print("The last digit of {} is {} and is less than 6 and not 0".format(number, reminder))