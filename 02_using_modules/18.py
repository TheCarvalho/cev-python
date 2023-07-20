
# *ex 18 = Create a program that reads any angle and displays on the screen the values of sine, cosine, and tangent of that angle.

from math import cos, sin, tan, radians

ang = float(input('Enter any angle: '))
print('\nThe cosine is {:.2f} \nThe sine is {:.2f} \nand the tangent is {:.2f}'
      .format(cos(radians(ang)), sin(radians(ang)), tan(radians(ang))))
