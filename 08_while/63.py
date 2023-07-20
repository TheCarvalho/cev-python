
# *ex63 - Write a program that reads any integer N and displays the first N elements of a Fibonacci Sequence on the screen. Example: 0 – 1 – 1 – 2 – 3 – 5 – 8


n = int(input('N: '))
a, b = 0, 1

while a <= n:
    print(a, end=' ')
    a, b = b, a+b
