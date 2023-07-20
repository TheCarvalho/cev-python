
from os import system

system('cls')

numero = primos = 0
lista = list()
nova_lista = list()


while primos != 50:
    numero += 1
    cont = 0

    for regressivo in range(numero, 0, -1):
        if numero % regressivo == 0:
            cont += 1
    if cont == 2:
        primos += 1
        lista.append(numero)


lista = iter(lista)
contador = 1
largura = 100


for _ in range(5):
    nova_lista.clear()

    for i in range(contador):
        nova_lista.append(next(lista))
    contador += 2

    print(str(nova_lista).replace('[', '').replace(']', '').center(largura))
    print()
print(('| |').center(largura))
