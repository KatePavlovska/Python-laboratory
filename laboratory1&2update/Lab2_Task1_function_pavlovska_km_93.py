print("Павловська Катерина. КМ-93. Варіант 14. ")
print("Task1:Calculation of the product by the formula.")
print()

import re

re_float = re.compile("^[-+]?\d+(.?\d+)?$")
re_integer = re.compile("^[-+]?\d+$")

def validator(pattern, promt):
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text

x = float(validator(re_float,"Input x: "))
n = int(validator(re_float, "Input n: "))
result = x ** 2 / x
for i in range(1, n):
    result *= (x - i) ** 2 / x
    if result == 0:
        print("Result: ", result)
    else:
        print("Result: ", result)
        break