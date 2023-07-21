
# ### **EXE_104**

# > Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
# > Ex:
# > n = leiaInt('Digite um n')


def leiaint(msg):
    ok = False
    valor = 0
    while True:
        # ! parece que só consigo deixar um input em branco se for string
        n = str(input(msg))
        if n.isnumeric():  # ! sendo string consigo analisar para ver se é numero
            valor = int(n)
            ok = True
        else:
            print('Erro. Insira um valor válido')
        if ok:  # ! Se ok for verdadeiro
            break
    return valor


# ! Isso é interessante, não só ele pega as variaveis como tbm posso mostrar mensagens antes de pegar o valor
n = leiaint('Digite um n: ')
print(f'Você acabou de digitar o número {n}')
