
# *ex 9 = Write a program that reads any integer number and displays its multiplication table on the screen.

num = int(input('Number: '))
i = 1
while i <= 10:
    print('{} * {} = {}'.format(num, i, num*i))
    i += 1
