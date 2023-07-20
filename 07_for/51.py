
# *ex51 - Develop a program that reads the first term and ratio of an arithmetic progression. at the end show the first 10 terms of this progression

termo1 = int(input('Insira o primeiro termo: '))
razao = int(input('Insira a razão: '))

ultimo = termo1 + (10-1)*razao

for i in range(termo1, ultimo+1, razao):
    print(i)
