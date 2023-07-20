
# *ex38 - Write a program that reads 2 integers and compares them, showing a message on the screen.
# * The first value is greater.
# * The second value is greater.
# * There is no higher value, the 2 are equal.

num = int(input('Enter a number: '))
num2 = int(input('Another one: '))

if num == num2:
    print('There is no higher value')
elif num > num2:
    print('The first value is greater.')
else:
    print('The second value is greater.')
