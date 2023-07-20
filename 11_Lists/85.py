
# * Ex85: Create a program where the user can enter seven numeric values and register them in a single list that keeps even and odd values separate. At the end, show the even and odd values in ascending order.

num = [[], []]
value = 0

for i in range(1, 8):
    value = int(input(f'Enter the value #{i}: '))

    if value % 2 == 0:
        num[0].append(value)
    else:
        num[1].append(value)

print('--' * 30)

num[0].sort()
num[1].sort()

print(f'The even values entered were: {num [0]}')
print(f'the odd values entered were: {num[1]}')
