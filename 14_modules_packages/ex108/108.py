# **EXE_108**

# > Adapte o código do **Desafio 107**, criando uma função adicional chamada moeda() que consiga os valores como um valor monetário formatado.

import moeda

p = float(input('Enter the price: R$'))
# exemplo de como apresentar em outra moeda
print(f'A metade de {moeda.moeda(p, "US$")} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(
    f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p,10))}')
print(
    f'Reduzindo 13%, temos {moeda.moeda(moeda.diminuir(p, 13))}')
print()
