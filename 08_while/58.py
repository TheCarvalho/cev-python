
# *ex58 - Improve the CHALLENGE 28 game where the computer will “think” a number between 0 and 10. But now the player will try to guess until he gets it right, showing in the end how many guesses were needed to win

from os import system
from random import randint

i = 1
print('='*30)
num = int(input('Guess the machine number from 0/10: '))

while num != randint(0, 10):
    system('cls')
    print(f'\033[1;31mYou missed {i}x try again!\033[m')
    num = int(input('Guess the machine number from 0/10: '))
    i += 1
system('cls')
print('\033[1;32mCongratulations, you win!!\033[m')
