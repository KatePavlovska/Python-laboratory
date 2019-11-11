print( 'Павловська Катерина. КМ-93. Варіант №14.' )
print("Task: Make a program that determines the result of divination on the camomile - love-does not love, taking the original given number of petals n (enter from the keyboard)." )
print()
print('You are welcomed by the guessing program')

import re

re_integer = re.compile("^[-+]?\d+$")


def validator(pattern, promt):
    text = input( promt )
    while not bool( pattern.match( text ) ):
        text = input( promt )
    return text


Petails = int( validator( re_integer, "Print some number of Peatils " ) )

while Petails <= 3:
    print( "The given values are incorrect, which flower does not exist, please try again" )
    Petails = int( input( "Number of petals: " ) )

Version = int(
    validator( re_integer, "If you want to start guessing with likes press - 1, if with dislikes press - 2" ) )

if Version == 1:
    print( 'You started guessing with loves' )
elif Version == 2:
    print( 'You started guessing with dislikes' )
while Version != 1 and Version != 2:
    print(
        "You have entered an incorrect value if you want to start guessing with likes press-1, if with dislikes press-2" )
    Version = int( input( "If you want to start guessing with likes press - 1, if with dislikes press - 2" ) )
if Petails // 2 == 0 and Version == 1:
    print( 'Your result of divination does not like' )
elif Petails // 2 != 0 and Version == 1:
    print( "Your divination result loves" )
elif Petails // 2 == 0 and Version == 2:
    print( 'Your divination result loves' )
elif Petails // 2 != 0 and Version == 2:
    print( 'Your divination result loves' )

print( "The end" )
