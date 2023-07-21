
# * Anotações que fiz na aula funções parte 1
'''
something = 0
print('\t\t\tHello World')
if something > 0:
    print()


def soma(a, b):
    return a + b


def divisão(a, b):
    pass                    #! pass me permite ter uma função sem apresentar erros mesmo que n esteja pronta


def contador(* num):        #! O nome desse * é desempacotamento, ele me permite adicinar adicionar varios numeros dentro desse parametro, vai me devolver com todos eles dentro de uma tupla
    tam = len(num)
    print(tam)

contador(3,2,1,4,5)         #! Empacotamento



def dobra(lista):
    pos = 0
    while pos < len(lista):  # lembrando q ele ignora o ultimo valor e começamos com 0
        # engraçado q se tu printar len(lista) ele diz tudo certinho sem começar do 0
        lista[pos] *= 2
        pos += 1


valores = [7, 2, 5, 0, 4]
dobra(valores)  # o que fizer na lista 'lista' vai atribuar em valores
print(valores)

#x = int(input('Insira um numero: '))
#y = int(input('Insira um numero: '))


#soma(x, y)
#contador(2, 2, 2, 2, 2)'''

#*###########################################################################################
# *Anotações que fiz durante aula funções parte 2

#! interactive help

#   help() = escrever isso no terminal python. Ele mostra meio que um manual para algum comando que vc digitar lá
#   help(print)   = posso usar assim tbm, num programa normal

#   outra forma maneira de conseguir informação sobre alguma coisa é desse jeito: print(input.__doc__)


#! docstring

def contador(i, f, p):  # esses valores dentro de parenteses são chamados de parametros
    """
    -> Faz uma contagem e mostra na tela
    :param i: inicio da contagem
    :param f: fim da contagem               #! Isso é docstring. Lembrar que são 3 aspas " " "
    :param p: passo da contagem 
    :return: sem retorno
    """
    c = 1
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')


help(contador)


#! parametros opcionais

def somar(a=0, b=0, c=0):  # ! Esse negocio de colocar paramentro = 0 se chama de parametro opcional para usar em casos de eu inserir menos parametros do que aqueles q se espera
    """
    FAZ A SOMA DE 3 VALORES
    :param 1: PRIMEIRO VALOR
    :param 2: SEGUNDO VALOR
    :param 3: TERCEIRO VALOR
    FUNCAO CRIADA POR CURSO EM VIDEO
    """
    s = a+b+c
    print(f'A soma vale {s}')


# help(somar) # me mostra a docstring
somar(3, 2, 5)
somar(c=3, b=2)  # ! Como esse exemplo


# end ='' < é um parametro opcional da função print q tem o valor de = '\n'
# help(print) #mostra os parametros opcionais como sep =' ', end ='\n', file=sys.stdout, flush=false


'''
O print usa stdout, como C. Isso nada mais é do que o "arquivo" no sistema operacional pra onde a saída de texto de um programa é mandada, e assim pode ser mostrada pro usuário.

Por padrão, o stdout é bufferizado; quer dizer, ele guarda os dados que recebe sem mostrá-los até que receba o código especial de nova linha \n.

A função print do Python por padrão automaticamente bota um caractere de nova linha em qualquer string que você mande pra ela. Mas às vezes, esse comportamento não é desejado e você deseja usar dois prints pra mostrar alguma coisa na mesma linha. Nesse caso, você vai usar o argumento end da função print pra terminar a string com alguma coisa diferente do caractere de nova linha (ou com uma string vazia, pra não printar nada além do que você mandou).

Por exemplo, você pode esperar que o código a seguir printe vários pontos na mesma linha, um a cada 0.5s:

import time

for _ in range(5):
    print('.', end='')
    time.sleep(0.5)
print(' Pronto!')
Mas o que realmente acontece na maioria dos casos é que nada acontece por 2.5s e depois todos os pontos aparecem de uma vez.

Isso acontece porque o stdout por padrão não mostra nada até que ele receba uma linha nova, que não estamos mandando até o final.

Então como remediamos esse problema?

Simples, basta usar o flush pra forçar que o resultado apareça imediatamente, mesmo sem linha nova:

import time

for _ in range(5):
    print('.', end='', flush=True)
    time.sleep(0.5)
print(' Pronto!')
Vale mencionar que o flush como argumento pro print só está disponível a partir do Python 3.3. Antes disso, ele tinha que ser chamado manualmente:

import sys
import time

for _ in range(5):
    print('.', end='')
    sys.stdout.flush()
    time.sleep(0.5)
print(' Pronto!')
'''


#! escopo de variaveis

# variaveis globais e locais
# se A global for 5 e A local eu botar 8 ele vai criar outra variavel que serial local com o valor de 8 entao a global permaneceria com o valor de 5
# vc pode importar parametros de 2 modos, se tu colocar dentro dos parenteses da função ele vai criar uma variavel local com o valor da variavel com que vc chamou a função
# outro jeito é vc n colocar nada dentro dos parenteses e declarar em baixo global + variavel global que vc quer importar, as mudanças serão feitas tanto localmente quanto global

def teste(b_com_valor_de_a):
    global a
    print(a)  # variavel global

    print(b_com_valor_de_a)  # variavel local com uma copia do valor de A
    b_com_valor_de_a = 2  # atribuindo outro valor a variavel local
    print(b_com_valor_de_a)  # variavel local com valor alterado

    a = 1  # alterando o valor da variavel global


a = 5
teste(a)
print(f'Fora de teste {a}')  # variavel com valor alterado fora da função


#! return de valores

def somar(a=0, b=0, c=0):
    s = a+b+c
    return s


# atribuindo a r1 o valor que será retornado da função a partir dos valores que foram inseridos
print(somar(3, 2, 5))
r2 = somar(1, 7)
r3 = somar(4)

print(f'{r2} {r3}')

#!############## aula pratica #################

# def fatorial(num=1):
#     f = 1
#     for c in range(num, 0, -1):
#         f *= c
#     return f


# f1 = fatorial(5)
# f2 = fatorial(4)
# f3 = fatorial()

# print(f'Os resultados são {f1}, {f2} e {f3}')

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')

#! escopo de chamada de biblioteca/função
