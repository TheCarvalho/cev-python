
# * EXE_80 - Create a program where the user can enter five numerical values and register them in a list, already in the correct insertion position (without using sort()). At the end, show the sorted list on the screen.

list = list()

for i in range(0, 5):

    number = int(input('Enter a value: '))

    if i == 0 or number > list[-1]:
        list.append(number)
        print('Added to end of list')
    else:
        pos = 0
        while pos < len(list):
            if number <= list[pos]:
                list.insert(pos, number)
                print(f'Added at position {pos} of list')
                break
            pos += 1

print('-' * 30)
print(f'The values entered in order were {list}')
