
# * Ex75: Develop a program that reads four values from the keyboard and stores them in a tuple. At the end, show:

# * A) How many times did the value 9 appear.
# * B) In what position was the first value entered 3.
# * C) What were the even numbers.

i = even = 0

tuple = (
    int(input('Enter a value: ')),
    int(input('Enter a value: ')),
    int(input('Enter a value: ')),
    int(input('Enter a value: ')),
)

print('-'*20)

# A)
print(f'Value 9 appears: {tuple.count(9)} times')

# B)
if 3 not in tuple:
    print('There is no value 3 in the tuple')
else:
    print('Value 3 is in position: ', tuple.index(3)+1)

# C)
print('Inserted even values: ', end='')
for x in tuple:
    if x % 2 == 0:
        print(x, end=' ')
        even = 1
if even == 0:
    print('there are no even values')
