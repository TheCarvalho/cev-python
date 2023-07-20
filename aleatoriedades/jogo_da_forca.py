from os import system
from time import sleep
from random import choice

with open("palavras.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))

    resposta = choice(words)


secreto = '-'*len(resposta)
temp = ''
tentativa = 5


def titulo():
    system('cls')
    print('--- JOGO DA FORCA ---\n')


def checador():
    global secreto, temp, letra, resposta
    for key, value in enumerate(resposta):
        if letra == value:
            temp += letra
        else:
            temp += secreto[key]
    secreto = temp
    temp = ''


def vitoria():
    print('Parabéns!!!')
    print(f'A Palavra era {resposta.upper()}')
    quit()


def derrota():
    system('cls')
    print(f'A Palavra era {resposta.upper()}')
    sleep(2)
    system('cls')
    print('GAME-OVER')
    quit()


while tentativa != 0:
    if secreto == resposta:
        vitoria()

    titulo()
    print(secreto.upper().center(19))

    letra = input(
        f'\n{tentativa} tentativas restantes!\nLetra: ').strip().lower()[0]
    system('cls')

    if letra not in resposta or letra in secreto:
        tentativa -= 1
    elif letra in resposta:
        checador()
derrota()
