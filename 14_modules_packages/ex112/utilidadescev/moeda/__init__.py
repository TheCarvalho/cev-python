def metade(valor=0, formato=False):
    res = valor/2
    return res if formato is False else moeda(res)


def dobro(valor=0, formato=False):
    res = valor*2
    return res if formato is False else moeda(res)


def aumentar(valor=0, porcentagem=0, formato=False):
    res = valor+(valor * porcentagem/100)
    return res if formato is False else moeda(res)


def diminuir(valor=0, porcentagem=0, formato=False):
    res = valor-(valor * porcentagem/100)
    return res if not formato else moeda(res)
#! lembra que if formato: => formato = True |||  if not formato: => formato = False


# aqui moeda fica como segundo parametro pois o primeiro a ser importado é o valor
def moeda(valor=0, moeda='R$'):  # Posso mudar a moeda apenas informando outra lá na hora de importar
    return f'{moeda}{valor:.2f}'.replace('.', ',')


def resumo(p=0, por1=10, por2=5):
    print('-'*40)
    # .rjust() => direita | .ljust() => esquerda | .center() => centralizar
    print('RESUMO DO VALOR'.center(40))
    print('-'*40)

    print(f'Preço Analisado:\t{moeda(p)}')
    print(f'Dobro do preço:\t\t{dobro(p,True)}')
    print(f'Metade do preço:\t{metade(p,True)}')
    print(f'{por1}% de aumento:\t\t{aumentar(p,por1,True)}')
    print(f'{por2}% de Redução:\t\t{diminuir(p,por2,True)}')

    print('-'*40)
