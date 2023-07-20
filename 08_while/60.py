
# *ex60 - Write a program that reads any number and displays its factorial. Example: 5! = 5 x 4 x 3 x 2 x 1 = 120

num = int(input('Enter a number to do the factorial: '))
i = factorial = num

print(f'{num}! = {num}', end='')

while i != 1:
    i -= 1
    factorial *= i
    print(f' x {i}', end='')
print(' =', factorial)
