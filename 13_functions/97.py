
# * Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

# *  Ex: escreva('Olá, Mundo!')
# * saida = ------------
# *        Olá, Mundo!
# *        ------------


def acompanhamento(frase):
    a = len(frase) + 4
    print()
    print('~'*a)
    print(f'  {frase}')
    print('~'*a)


frase = str(input('Insira a frase: '))
acompanhamento(frase)
