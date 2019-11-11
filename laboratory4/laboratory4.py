s = 0
n = 0
n1 = 0
n2 = 0
print("Павловська Катерина. КМ-93. Варіант - 14.")

def WordLenght(s,n):
    print("Введіть речення")
    s = input()
    s = s.split( )
    while True:
        print("Введіть цифру порядку, нумерація розпочинається з 0")
        n = input()
        try:
            n = int(n)
        except ValueError:
            print("Вводьте лише ціли цифри")
        else:
            if n < 0 or n >= len(s):
                print("Слова за таким символом не існує")
                continue
            break
    for i in range(len(s)):
        print("Довжина: ",len(s[n]))
        break

def Ro(n1, n2):
    while True:
        n1 = input("Введіть перше значення: " )
        n2 = input("Введіть друге значення: " )
        try:
            n1=int(n1)
            n2=int(n2)
        except ValueError:
            print("Ви ввели не коректне значення, спробуйте будь ласка ще раз")
        else:
            interseption = n1 & n2
            print(n1, "В двійковій формі: ", format(n1, "b"))
            print(n2, "В двійковій формі: ", format(n2, "b"))
            distance = 0
            for i in format(interseption, "b"):
                if i == "0":
                    distance += 1
            print("Відстань Гемінга", distance)
            break




while True:
    V = input("Веведіть 1 для того щоб запустити програму №1. Введіть 2 для того щоб запустити програму №2. Введіть 3 для того щоб вийти.\n \nВаша відповідь: ")

    try:
        V = int(V)
    except ValueError:
        print( "Ви ввели не коректне значення, спробуйте будь ласка ще раз" )

    if V == 1:
        WordLenght(s, n)
    elif V == 2:
        Ro(n1, n2)
    elif V == 3:
        exit()
    else:
        print("Введіть 1 чи 2!")

    resume = input("Продовжити виконання програми? Введіть y - так; n - ні: ")
    while resume.lower() != "y" and resume.lower() != "n":
        print( "Введений не вірний символ!" )
        resume = input("Продовжити виконання програми? Введіть y - так; n - ні: ")
    if resume.lower() == "n":
        break
