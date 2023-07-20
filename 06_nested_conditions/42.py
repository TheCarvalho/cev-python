
# *ex42 - Re-challenge 35 of the triangles adding the feature to show what kind of triangle will be formed.

# * Equilateral = all sides are equal.
# * Isosceles = 2 equal sides.
# * scalene = all sides different.

side1 = float(input('Enter the side of the triangle: '))
side2 = float(input('Enter the side of the triangle: '))
side3 = float(input('Enter the side of the triangle: '))

if side1 < side2 + side3 and side2 < side1 + side3 and side3 < side1 + side2:
    print('Triangle', end=' ')
    if side1 == side2 == side3:
        print('Equilateral')
    elif side1 != side2 != side3 != side1:  # tem que dar essa volta
        print('Scalene')
    else:
        print('Isosceles')
else:
    print('Not a triangle')
