
# * ex50 - Develop a program that reads 6 integers and prints the sum of only those that were even. If the entered value is odd, disregard it.

b = 0
for x in range(0, 6):
    a = int(input('Enter the number: '))
    if a % 2 == 0:
        b += a
print('The sum of those that are even is', b)
