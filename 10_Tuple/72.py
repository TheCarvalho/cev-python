
# *Ex72: Create a program that has a fully populated tuple with a count spelled out from zero to twenty. Your program should read a number from the keyboard (between 0 and 20) and display it in full.

from os import system

numbers = (
    'zero', 'one', 'two', 'three', 'four', 'five', 'six',
    'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen',
    'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
    'nineteen twenty'
)

while True:
    system('cls')
    while True:
        num = int(input('Enter a number from 0 to 20: '))
        if 0 <= num <= 20:
            break
        system('cls')
        print('Try again!')
    print(numbers[num])

    continuar = input('Wanna try again? [y/n] ').lower().strip()[0]

    if continuar == 'n':
        break
