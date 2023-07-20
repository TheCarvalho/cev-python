
# * Ex88: Make a program that helps a MEGA-SENA player to create guesses. The program will ask how many games will be generated and will raffle 6 numbers between 1 and 60 for each game, registering everything in a composite list.

from os import system
from random import randint
from time import sleep

lista = list()
temp = list()

print('{:=^33}'.format(' MEGA-SENA numbers '))
games = int(input('Enter number of games: '))
print()

for i in range(0, games):
    for j in range(0, 6):
        num = randint(1, 60)
        while num in temp:
            num = randint(1, 60)
        temp.append(num)
    temp.sort()
    lista.append(temp[:])
    temp.clear()

system('cls')
print('{:=^33}'.format(' MEGA-SENA numbers '))

for i in range(0, games):
    print(f'Game #{i+1} = ', end='')
    for j in range(0, 6):
        print(f'{lista[i][j]:^3}', end=' ')
    sleep(0.5)
    print()

print('='*33)
print('Good Luck!!')
input()
