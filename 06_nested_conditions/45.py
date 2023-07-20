
# *ex45 - crie um programa que faça o computador jogar jokenpo com você

import os
import random
from time import sleep


def game():
    os.system('cls')
    jogada = str(input('''\033[1;31m
        ###############
        ### JOKENPO ###
        ###############
        \033[36m
        Faça sua jogada:\033[m
        ''')).strip().lower()

    a = random.choice(['pedra', 'papel', 'tesoura'])

    os.system('cls')

    vitoria = '\033[1;32mVITORIA\033[m'
    derrota = '\033[1;31mDERROTA\033[m'
    empate = '\033[1;33mEMPATE\033[m'

    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!')
    sleep(1)

    os.system('cls')

    print(f'Sua jogada > {jogada} <')
    print(f'Minha jogada > {a} <\n')

    if jogada == a:
        print(empate)
    elif jogada == 'pedra':
        if a == 'papel':
            print(derrota)
        elif a == 'tesoura':
            print(vitoria)
    elif jogada == 'papel':
        if a == 'pedra':
            print(vitoria)
        elif a == 'tesoura':
            print(derrota)
    elif jogada == 'tesoura':
        if a == 'pedra':
            print(derrota)
        elif a == 'papel':
            print(vitoria)
    else:
        os.system('cls')
        print('''\033[33m
        !Entrada invalida, escolha entre pedra, papel ou tesoura!\033[m
        Aperte qualquer tecla''')
        input()
    input()
    game()


if __name__ == "__main__":
    game()

'''
from random import randint

itens = ('pedra', 'papel', 'tesoura')
computador = randint (0,2)
print(itens[computador])
'''
