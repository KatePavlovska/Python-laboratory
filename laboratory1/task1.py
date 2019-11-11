print('Павловська Катерина. КМ-93. Варіант №14.')
print("If you enter a definition from minus infinity to 13 inclusive, the program will perform function 1")
print(" If you enter a value from 14 inclusive plus infinity, the program will perform function 2")
X=float(input("Enter the value X =   "))
if X<=13:
    print ("You are performing function 2")
    print(-pow(X,3)+9)
else:
    print("You are performing function 2")
    print(-3/X+1)
print("The end.")