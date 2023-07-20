
# *ex49 - Redo CHALLENGE 009, showing the table of a number that the user chooses, only now using a for loop.

num = int(input('Enter the number for the table: '))

for i in range(1, 11):
    print(f'{num}  x {i:2} = {num*i:2}')
