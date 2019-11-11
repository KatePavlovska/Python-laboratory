print('Павловська Катерина. КМ-93. Варіант №14.')
print("Task: The user enters the number of weeks, months, years and receives the number of days during that time. Consider that a month is 30 days.")

import math
import re

re_integer = re.compile("^[-+]?\d+$")

def validator(pattern, promt):
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text

days = int(validator(re_integer, "Input the amount of days: "))
months = int(validator(re_integer, "Input the amount of mounth: "))
years = int(validator(re_integer, "Input the amount of years: "))

while days < 0:
    print('This statement is uncorrect, try again')
    days = int(input('Input the amount of days:  '))

while months < 0:
    print('This statement is uncorrect, try again')
    months = int(input('Input the amount of months: '))

while years < 0:
    print('This statement is uncorrect, try again')
    years=int(input("Input the amount of years: "))
Sum = days+months*30+years*12*30
print("The sum of amounts of days is: " + str(Sum))
print("The end.")