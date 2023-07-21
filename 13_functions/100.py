
# * Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint


def sorteia():
    global lista
    for i in range(0, 5):
        num = randint(0, 10)
        lista.append(num)
    print(f'Números sorteados da lista: ', end='')
    print(*lista)


def somarpar():
    listapar = list()
    for i in lista:
        if i % 2 == 0:
            listapar.append(i)
    print(f'Somando os valores pares de {lista}, temos {sum(listapar)}')


lista = list()
sorteia()
somarpar()

#*######################### tem esse outro metodo aqui tbm ###################
''' 

from random import randint


def sorteia(lista):

    for i in range(0, 5):
        num = randint(0, 10)
        lista.append(num)
    print(f'Números sorteados da lista: ', end='')
    print(*lista)


def somarpar(lista):
    listapar = list()
    for i in lista:
        if i % 2 == 0:
            listapar.append(i)
    print(f'Somando os valores pares de {lista}, temos {sum(listapar)}')


lista = list()
sorteia(lista)
somarpar(lista)
'''
