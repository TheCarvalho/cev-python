
# *ex52 - make a program that reads an integer and says whether or not it is a prime number

remainder = 0
num = int(input('Enter a number: '))
for i in range(1, num+1):
    if num % i == 0:
        remainder += 1
if remainder == 2:
    print('\033[1;32m Prime\033[m')
else:
    print('\033[1;31mNot prime\033[m')
