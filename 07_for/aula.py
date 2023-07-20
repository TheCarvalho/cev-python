
# *Estrutura de repetição FOR

for c in range(6, 0, -1):  # contar pra trás
    print(c)

for c in range(0, 11, 2):  # contando de 0 até 10 pulando de 2 em 2. Ele ignora o ultimo numero, por isso o 11
    print(c)

num = int(input('insira um numero: '))
for c in range(1, num+1):  # lembra que ele ignora o ultimo numero
    print(c)
