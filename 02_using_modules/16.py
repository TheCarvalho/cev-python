
# *ex 16 = Create a program that reads any real number from the keyboard and displays its integer part on the screen

from math import trunc

num = float(input('Enter a real number: '))
print('The integer part of this number is: {}'.format(trunc(num)))
