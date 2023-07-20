
# * Ex68: Write a program that plays even or odd with the computer. The game will only stop when the player loses, showing the total number of consecutive wins he has achieved at the end of the game.

from os import system
from random import randint

won_rounds = 0

while True:
    system('cls')

    choice = int(input('0 - Even\n1 - Odd\n'))
    if choice != 1 and choice != 0:
        print('Invalid input')
        break
    system('cls')
    humans_move = int(input('Enter 0-10 for odd or even: '))
    if humans_move > 10:
        print('Invalid input')
        break

    machines_move = randint(0, 10)
    rest = (machines_move + humans_move) % 2

    system('cls')
    if rest == choice:
        won_rounds += 1
        print(f'\033[1;32mCongratulations, you won {won_rounds} times\033[m')
        print('Again?')
        input()
    else:
        print(f'\033[1;31mYou lost with {won_rounds} victories\033[m')
        break
