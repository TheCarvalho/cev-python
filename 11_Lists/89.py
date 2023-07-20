
# * Ex89: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# * No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

from os import system

lista = list()
temp = list()
op = 'a'

while op not in 'n':
    op = 'a'
    temp.append(str(input('Insira o nome do aluno: ')).strip())
    temp.append(int(input('Insira a primeira nota: ')))
    temp.append(int(input('Insira a segunda nota: ')))

    lista.append(temp[:])
    temp.clear()

    while op not in 'sn':
        op = str(input('Gostaria de continuar? [s/n] ')).lower().strip()
    system('cls')
    if op == 'n':
        break

print('='*33)
print(f'{"Nº":<6}{"NOME":<13}{"MEDIA"}')
print('-'*33)

for i in range(0, len(lista)):
    print('{:<6}{:<13}{}'.format(
        i+1, lista[i][0], (lista[i][1] + lista[i][2])/2))
print('-'*33)

while True:
    op = int(input('Mostrar notas de qual aluno? (999 interrompe): '))

    if op == 999:
        print('Até mais!')
        quit()
    elif 0 <= op <= len(lista):
        print(f'Notas de {lista[op][0]} são {lista[op][1]} e {lista[op][2]}')
        print('-'*33)
    else:
        system('cls')
        print('Entrada invalida, tente novamente')
