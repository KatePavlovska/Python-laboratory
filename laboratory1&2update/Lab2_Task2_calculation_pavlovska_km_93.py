print("Павловська Катерина. КМ-93. Варіант 14. ")
print("Task2: Given an integer N (> 0), which is a degree of 2: N = 2K. Finding an integer K is an exponent of this degree.")
print()

import re

re_integer = re.compile("^[-+]?\d+$")


def validator(pattern, promt):
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text


number = int( validator( re_integer, "Input number: "))
counter = 0

while number % 2 == 0:
    number /= 2
    counter += 1
if number != 1:
    print("This number is not a power of 2!")
else:
    print("This number is", counter, " power")
