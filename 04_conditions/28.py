
# * Ex28 - Write a program that makes the computer 'think' of an integer number between 0 and 5 and asks the user to try to guess the chosen number by the computer. The program should display on the screen if the user won or lost.

from random import randint

num = int(input('Enter a number from 0 to 5: '))

print(
    '\nYou win' if num == randint(0, 5)
    else 'You lose'
)
