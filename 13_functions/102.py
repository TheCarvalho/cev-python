# ### **EXE_102**

# > Crie um programa que tenha uma função fatorial() que receba dois parâmentros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico(opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.


def fatorial(n, show=False):
    """
    -> Calculo fatorial de um numero.
    :param num: O numero a ser calculado
    :param show: (opcional) Mostrar ou não a conta 
    :return: O valor fatorial de um número
    """
    f = 1
    for c in range(n, 0, -1):
        if show:  # ! Isso aqui é interessante, se show for verdadeiro
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# programa principal

num = int(input('Insira o valor para '))

show = 'a'
while show not in 'sn':
    show = str(input('Quer ver o processo? [s/n] ')).lower().strip()[0]
print(f'{fatorial(num, show=True)}' if show == "s" else f'{fatorial(num)}')
