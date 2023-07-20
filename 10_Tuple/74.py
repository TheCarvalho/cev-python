
# * Ex74: Create a program that will generate five random numbers and put them in a tuple. After that, show the list of generated numbers and also indicate the smallest and largest values that are in the tuple.

from random import randint


tuple = (randint(1, 10), randint(1, 10), randint(
    1, 10), randint(1, 10), randint(1, 10))

print('Values: ', end='')

for n in tuple:
    print(f'{n}', end=' ')
print(f'\nmin: {min(tuple)}')
print(f'max: {max(tuple)}')
