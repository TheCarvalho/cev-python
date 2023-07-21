# ### **EXE_101**

# > Crie um programa que tenha uma função chamada voto() que vai rereber como parâmentros o ano de nascimento de uma pessoa, retornando um valor literal indicando uma pessoa tem voto **NEGADO**, **OPCIONAL** ou **OBRIGATÓRIO** nas eleições.

# from datetime import datetime


# def voto(ano_nasc):
#     idade_atual = datetime.today().year - ano_nasc

#     if idade_atual < 18:
#         return(f'Com {idade_atual} anos: Voto Negado!')             #! Eu fiz esse
#     elif idade_atual < 65:
#         return(f'Com {idade_atual} anos: Voto Obrigatório!')
#     else:
#         return(f'Com {idade_atual} anos: Voto Opcional!')


# ano_nasc = int(input('Em que ano você nasceu? '))

# print(voto(ano_nasc))

#!#####################################################################################

def voto(ano):
    # * Escopo de importação => Essa importação só funciona para dentro dessa função, economiza memoria.
    from datetime import date
    atual = date.today().year
    idade = atual - ano

    if idade < 16:
        return f'Com {idade} anos: Não Vota'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: Voto Opcional'
    else:
        return f'Com {idade} anos: Voto Obrigatorio'


# Programa Principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
