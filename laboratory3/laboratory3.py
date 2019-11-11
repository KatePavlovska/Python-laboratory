print("Павловська Катерина. КМ-93. Варіант - 14.")

def task_1():
    text = input("Введіть слово або речення: ")
    counter = 0
    for i in range(len(text)):
        vowel = "аоуеиіяюєї" + "eyuioa" + "уеаыояиё"
        if text[i] in vowel + vowel.upper():
            text = text[0:i] + "*" + text[i + 1: len(text)]
            counter +=1
    print("Кількість знайдених голосних: ", counter)
    print(text)


while True:
    V = input("Веведіть 1 для того щоб запустити програму, 2 для того щоб вийти")
    try:
        V = int(V)
    except ValueError:
        print("Ви ввели не коректне значення, спробуйте будь ласка ще раз")

    if V == 1:
        task_1()
    elif V == 2:
        exit()
    else:
        print("Введіть 1 чи 2!")

    resume = input("Продовжити виконання програми? Введіть y - так; n - ні: ")
    while resume.lower() != "y" and resume.lower() != "n":
        print("Введений не вірний символ!")
        resume = input("Продовжити виконання програми? Введіть y - так; n - ні: ")
    if resume.lower() == "n":
        break

