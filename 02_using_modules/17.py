# *ex 17 = Create an algorithm that reads the length of the opposite side and the adjacent side of a right triangle. Calculate and display the length of the hypotenuse.

from math import hypot

opos = float(input('Enter the opposite side: '))
adj = float(input('Enter the adjacent side: '))

print('The hypotenuse is {}'.format(hypot(opos, adj)))
