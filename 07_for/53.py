
# *ex53 - crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços apos a sopa, a sacada da casa, a torre da derrota, o lobo ama o bolo, anotaram a data da maratona

frase = str(input('Insira a frase: ')).lower()
frase = frase.replace(' ', '')
inverso = frase[::-1]  # inverter a frase, fatiamento

if frase == inverso:
    print('É um polindromo')
else:
    print('Não é polindromo')


'''
frase = str(input('Insira a frase: ')).lower().strip()
frase = frase.split()
frase = ''.join(frase)
inverso = ''

for letras in range (len(frase) -1, -1, -1):  #len(frase) -1 = o ultimo caractere |,-1 se ele sempre começa do 0 e vamos na contra mão, ele vai ignorar o ultimo, então anterior de 0 é -1|,-1 significa que vamos na contra mão
    inverso += frase[letras]  # ele vai colocando letra por letra nessa variavel na contra mão da original até terminar o loop

if frase == inverso:
    print('É um polindromo')
else:
    print('Não é polindromo')
'''
