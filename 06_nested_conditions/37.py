
# *ex37 - Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1-binario 2-octal 3-hexadecimal

num = int(input('Enter a number: '))
op = int(input('Conversion to: 1-binary, 2-octal or 3-hexadecimal: '))

if op == 1:
    # esse [2:] é tratamento de string, fatiamento, da lista 'manipulando textos' 2 = começa a mostrar dps da segunda string até o final
    print(bin(num)[2:])
elif op == 2:
    print(oct(num)[2:])
elif op == 3:
    print(hex(num)[2:])
else:
    print('Invalid Input')
