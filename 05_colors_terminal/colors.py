
# Colors in the terminal

print('\033[1;31m' 'Hello World again' '\033[m')
print('GoodBye World')


test = '\033[1;31m' 'DEV' '\033[m'
print(f"I am {test}")

# ====================================================

cores = {  # vou fazer desse jeito
    'limpa': '\033[m',
    'vermelho': '\033[1;31m'
}

print(f'Muito prazer em te conhecer '
      f'{cores["vermelho"]}Chefe{cores["limpa"]}, bom dia')


# ====================================================
first = 'Peter'
second = 'Parker'
third = 'Spidey'
print('{2} {0} {0} {1} {0} {2}'.format(first, second, third))
