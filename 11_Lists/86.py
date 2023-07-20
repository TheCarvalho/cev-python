
# * Ex86: Create a program that declares a 3×3 matrix and fills it with values read from the keyboard. At the end, show the matrix on the screen, with the correct formatting.

matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(0, 3):
    for j in range(0, 3):
        matrix[i][j] = int(input(f'Enter the number in position [{i}][{j}]: '))

print('-'*50)

for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matrix[i][j]:^5}]', end='')
    print()
