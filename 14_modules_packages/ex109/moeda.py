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


# aqui moeda fica como segundo parametro pois o primeiro a ser importado é o valor
def moeda(valor=0, moeda='R$'):  # Posso mudar a moeda apenas informando outra lá na hora de importar
    return f'{moeda}{valor:.2f}'.replace('.', ',')

#! lembra que if formato: => formato = True |||  if not formato: => formato = False
