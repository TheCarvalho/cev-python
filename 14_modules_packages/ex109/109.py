# **EXE_109**

# > Modifique as funções que foram criadas no **Desafio 107** para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pelo funções moeda(), desenvolvida no **Desafio 108**.

import moeda
#! python n importa se o nome do modulo for apenas número

p = float(input('Digite o preço: R$'))
# exemplo de como apresentar em outra moeda
print(f'\nA metade de {moeda.moeda(p, "US$")} é {moeda.metade(p, True )}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10% temos {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo 13% temos {moeda.diminuir(p, 13, True)}')
print()
