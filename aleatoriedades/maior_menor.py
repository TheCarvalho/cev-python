lista = [5, 4, 6, 8, 2, 1, 6, 8, 4]
maior = menor = 0

for c in range(0, len(lista)):
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]

print(maior)
print(menor)
