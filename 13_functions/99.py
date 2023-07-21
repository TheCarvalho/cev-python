
# * Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep
from os import system


def maior(*num):

    print('Valores inseridos: ', end='')
    for i in (num[0]):
        sleep(0.8)
        print(i, end=' ', flush=True)

    print(f'\nQuantidade de valores inseridos = {len(num[0])}')
    print(f'O maior valor informado foi = {max(num[0])}')


# principal
lista = list()

while True:
    num = int(input('Insira o valor para ser processado: (00 para terminar) '))
    if num == 00:
        break
    lista.append(num)

system('cls')
maior(lista)
