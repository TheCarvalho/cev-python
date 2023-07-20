
# *ex48 - make a program that calculates the sum of all odd numbers that are multiples of 3 and that are in the range from 1 to 500

sum = 0

for x in range(1, 501):
    if x % 3 == 0 and x % 2 == 1:
        sum += x
print('The sum of all numbers divisible by 3 and odd is:', sum)
