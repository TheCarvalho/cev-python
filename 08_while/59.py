
# *ex59 - Create a program that reads two values and displays a menu on the screen:
# * [ 1 ] add [ 2 ] multiply [ 3 ] greater [ 4 ] new numbers [ 5 ] exit program
# * Your program should perform the requested operation in each case.

from os import system
option = 0

while option != 5:
    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number: '))

    option = int(input('''
    ============== MENU ==============
    [ 1 ] SUM
    [ 2 ] MULTIPLY
    [ 3 ] BIGGER
    [ 4 ] NEW NUMBERS
    [ 5 ] EXIT
    '''))
    if option == 1:
        print(f'{num1} + {num2} = {num1 + num2}')
        input()
    elif option == 2:
        print(f'{num1} X {num2} = {num1 * num2}')
        input()
    elif option == 3:
        print('the biggest number is ', num1 if num1 > num2 else num2)
        input()
    elif option == 4:
        print('So, new numbers')
        input()
    system('cls')
system('cls')
