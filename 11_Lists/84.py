
# * Ex84: Make a program that reads name and weight of several people, keeping everything in a list. At the end, show:

# * A) How many people were registered
# * B) A list of the heaviest people
# * C) A listing with the lightest people

from os import system

list = list()
registered = maior = menor = 0


while True:
    print('-'*30)
    op = 'a'
    list.append(input('Your name: ').strip().lower())
    list.append(int(input('Your weight: ')))

    registered += 1

    while op not in 'yn':
        op = input('continue? [y/n]').strip().lower()
    if op == 'n':
        break
system('cls')

max = min = list[-1]

for i in range(1, len(list), 2):

    if list[i] > max:
        max = list[i]
    if list[i] < min:
        min = list[i]

print('Registered people:', registered)

print('Heaviest: ', end='')
for j, x in enumerate(list):
# enumarate pega tanto a posição quanto o valor, mas precisa de 2 variaveis
    if x == max:
        print(list[j-1], end=' ')
print(f'weighing {max}kg')


print('Lighter: ', end='')
for j, x in enumerate(list):
    if x == min:
        print(list[j-1], end=' ')
print(f'weighing {min}kg')

# indicesmax = [j for j, x in enumerate(lista) if x == max] # Isso cria uma outra lista com os valores que foram repetidos
