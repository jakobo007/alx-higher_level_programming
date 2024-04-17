#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
<<<<<<< HEAD
        if i % 3 == 0 and i % 5 != 0:
            print("Fizz", end='')
        elif i % 5 == 0 and i % 3 != 0:
            print("Buzz", end='')
        elif i % 5 == 0 and i % 3 == 0:
=======
        if i % 3 == 0:
            print("Fizz ", end='')
        elif i % 5 == 0:
            print("Buzz ", end='')
        elif (i % 3 == 0) and (i % 5 != 0):
>>>>>>> 1c6bdd794f791f9b6e76c3981d364379d8a6942d
            print("FizzBuzz ", end='')
        else:
            print("{} ".format(i), end='')

