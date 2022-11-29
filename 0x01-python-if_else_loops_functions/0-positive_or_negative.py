#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print("Number is positive")
elif number == 0:
    print("Number is zero")
else:
    print("Number is negative")
