#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    i = number % -10
if number >= 0:
    i = number % 10

if number % 10 == 0:
    print("Last digit of", number, "is", i, "and is 0")


elif number % 10 > 5:
    print("Last digit of", number, "is", i, "and is greater than 5")


else:
    print("Last digit of", number, "is", i, "and is less than 6 and not 0")
