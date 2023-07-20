
# * Ex76: Create a program that has a single tuple with product names and their respective prices, in sequence. At the end, show a price list, organizing the data in tabular form.

list = (
    'Lapis', 1.75,
    'Borraca', 2,
    'Caderno', 15.99,
    'Estojo', 25,
    'Transferidor', 4.20,
    'Compasso', 9.99,
    'Mochila', 120.50,
    'Canetas', 22.50,
    'Livros', 34.99
)

print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)

for pos in range(0, len(list)):
    if pos % 2 == 0:
        print(f'{list[pos]:.<30}', end='')
    else:
        print(f'R${list[pos]:.2f}')
        # print(f'R${listagem[pos]:>6.2f}')  # Esse é um exemplo de como deixar ele encostado na direita
print('-'*40)
