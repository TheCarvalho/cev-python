from random import choice
from string import ascii_uppercase


alphabet = ascii_uppercase
random = choice(alphabet)

print('random letter: {}{}{}'.format('\033[1;31m', random, '\033[m'))
