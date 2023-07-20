
# *Ex35 - Develop a program that reads the length of 3 lines and tells the user whether they can or cannot form a triangle.

a = int(input('Enter r1: '))
b = int(input('Enter r2: '))
c = int(input('Enter r3: '))

if (
    a < b + c and
    b < a + c and
    c < a + b
):
    print("It's possible to form a triangle!")
else:
    print("It's not possible to form a triangle!")
