
# *EXE_81 - Create a program that will read several numbers and put them in a list. After that show:

# * A) How many numbers were entered.
# * B) The list of values, sorted in descending order.
# * C) Whether the value 5 was entered and is or is not in the list.

values = []
while True:
    values.append(int(input('Enter a value: ')))
    op = str(input('Continue? [y/n]'))
    if op in 'Nn':
        break

print('-'*30)

print(f'You entered {len(values)} elements')
values.sort(reverse=True)

print(f'The values in descending order are {values}')

if 5 in values:
    print('The value 5 is part of the list!!')
else:
    print('The value 5 was not found in the list!')
