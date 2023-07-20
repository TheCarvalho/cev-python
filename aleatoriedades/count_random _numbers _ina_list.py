'''Escreva um algoritmo que recebe um valor inteiro m. Logo após, seu
programa receberá uma sequência de valores inteiros maiores ou iguais a 0 e
menores do que m, separados por vírgula. Seu programa deve imprimir na
tela quantas vezes cada número da sequência apareceu, em ordem.
Utilize o exemplo abaixo para entender como os dados serão recebidos e
como a saída deve ser exibida.
Exemplo de entrada:

4
3,1,3,0,1,1,1,3,1,3

Exemplo de saída:

0,1
1,5
3,4

No exemplo acima, as entradas m = 4 e 3,1,3,0,1,1,1,3,1,3 representa uma
sequência de números inteiros separados por vírgula. Já a saída indica que o
número 0 apareceu 1 vez, o número 1 apareceu 5 vezes e o número 3
apareceu 4 vezes na sequência. '''

import random

lista = []
m = int(input('Insira um numero inteiro: '))

for p in range(0, 10):
    # aparentemente randrange ignora o ultimo, se fosse <= m seria m+1
    a = random.randrange(0, m)
    lista.append(a)

lista.sort()

print(lista, '\n')
i = 0
contador = 1


for i in range(i, len(lista)-1):

    if lista[i] == lista[i+1]:
        contador += 1

        if i == len(lista)-2:
            print(lista[i], ',', contador)

    else:
        print(lista[i], ',', contador)
        contador = 1
if lista[8] != lista[9]:
    print(lista[9], ', 1')
