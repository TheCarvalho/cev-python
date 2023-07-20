
# *EXE_82 - Create a program that will read several numbers and put them in a list. After that, create two extra lists that will contain only the even values and odd values entered, respectively. At the end, show the contents of the three generated lists.


num = list()
even = list()
odd = list()

while True:
    num.append(int(input('Enter a number: ')))
    op = str(input('Continue? [Y/N] ')).lower().strip()[0]
    if op == 'n':
        break

for i, j in enumerate(num):
    if j % 2 == 0:
        even.append(j)
    else:
        odd.append(j)

print('-'*30)
print(f'The complete list is {num}')
print(f'The list of pairs is {even}')
print(f'The odd list is {odd}')
