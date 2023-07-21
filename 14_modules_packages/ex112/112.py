# **EXE_112**

# > Dentro do pacote utilidadesCev que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas valores que sejam monetários.

from utilidadescev import moeda, dados
#! python n importa se o nome do modulo for apenas número

p = dados.leiadinheiro('Digite o preço: R$')
moeda.resumo(p, 90, 25)
