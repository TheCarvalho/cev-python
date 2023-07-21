# **EXE_111**

# > Crie um pacote chamado utilidadesCev que tenha dois módulos internos chamados moeda e dado. Tranasfira todas as funções utilizandos nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.

from utilidadescev import moeda
#! python n importa se o nome do modulo for apenas número

p = float(input('Digite o preço: R$'))
moeda.resumo(p, 90, 25)
