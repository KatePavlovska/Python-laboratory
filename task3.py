print('Павловська Катерина. КМ-93. Варіант №14.')
days=int(input("Input the amount of days: " ))
while days<0:
    print('This statement is uncorrect, try again')
    days=int(input('Input the amount of days:  '))
months=int(input("Input the amount of months: "))
while months<0:
    print('This statement is uncorrect, try again')
    months=int(input('Input the amount of months: '))
years=int(input('Input the amount of years: '))
while years<0:
    print('This statement is uncorrect, try again')
    years=int(input("Input the amount of years: "))
Sum=days+months*30+years*12*30
print("The sum of amounts of days is: " +  str(Sum))
print("The end.")