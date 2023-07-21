def metade(valor=0):
    res = valor/2
    return res


def dobro(valor=0):
    res = valor*2
    return res


def aumentar(valor=0, porcentagem=0):
    res = valor+(valor * porcentagem/100)
    return res


def diminuir(valor=0, porcentagem=0):
    res = valor-(valor * porcentagem/100)
    return res


# aqui moeda fica como segundo parametro pois o primeiro a ser importado é o valor
def moeda(valor=0, moeda='R$'):  # Posso mudar a moeda apenas informando outra lá na hora de importar
    return f'{moeda}{valor:.2f}'.replace('.', ',')
