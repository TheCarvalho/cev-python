
# * EXE_79 - Create a program where the user can type several numerical values and register them in a list. If the number already exists in there, it will not be added. At the end, all unique values entered will be displayed, in ascending order.

list = list()

while True:
    num = int(input('Enter a value: '))
    if num not in list:
        list.append(num)
        print('value added successfully')
    else:
        print('Duplicate value! Not added')
        op = str(input('Continue? [y/n]')).lower().strip()[0]
        if op == 'n':
            break

print('-'*30)
list.sort()
print(f'You typed these values {list}')
