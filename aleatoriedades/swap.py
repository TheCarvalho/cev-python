def reverse_array(lista):
    """
    -> Funcao de inverter valores de uma lista
    :param lista: lista que ta sendo importada
    :return: Nao ta retornando nada, ele faz o esquema e executa la msm
    """
    print(f'Normal = {lista}')
    x = 0
    y = len(lista) - 1  # -1 Aqui pq len() retorna o número de valores q tem dentro e como eu vou usar isso como key preciso diminuir pois comeca com 0 e ele ignora o ultimo valor lembra??
    while x < y:

        temp = lista[x]
        lista[x] = lista[y]
        lista[y] = temp

        x += 1
        y -= 1
    print(f'Invertido = {lista}')


help(reverse_array)
input()
lista = [3, 5, 7, 2, 3, 5, 4, 0]
reverse_array(lista)


#!  Outros métodos de conseguir os valores invertidos de uma lista, só que criando outra lista

# Metodo 1 de conseguer uma lista inversa

# listareversa = []
# numbers = list(range(9))
# print(numbers)

# for i in range(numbers[-1], -1, -1):
#     listareversa.append(i)
# print(listareversa)

###### Metodo 2 ######

# numbers = list(range(9))
# print(numbers)
# newList = numbers[::-1]
# print(newList)

###### Metodo 3 ######

# numbers = list(range(9))

# novalista = list(reversed(numbers))

# print(numbers, novalista)

###### Metodo 4 ######

# numbers = list(range(9))
# # ! Isso aqui é interessante, primeira vez que tô vendo essa forma de atribuição
# # Ele vai adicionando valor por valor dentro daquela lista, só que reversed
# newList = [num for num in reversed(numbers)]
# print(numbers)
# print(newList)
