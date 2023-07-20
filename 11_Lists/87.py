
# * Ex87: Improve the previous challenge, showing at the end:

# * A) The sum of all even values entered.
# * B) The sum of the values in the third column
# * C) The largest value of the second line

sum_third_column = sum_evens = 0
matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(0, 3):
    for j in range(0, 3):
        matrix[i][j] = int(
            input(f'Enter the number in position [{i+1}][{j+1}]: '))
        if matrix[i][j] % 2 == 0:
            sum_evens += matrix[i][j]
    print()

print('-'*50)
sum_third_column = matrix[0][2] + matrix[1][2] + matrix[2][2]

for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matrix[i][j]:^5}]', end='')
    print()

print()
print(f'The sum of all even values is: {sum_evens}')
print(f'The sum of the values of the third column is: {sum_third_column}')
print(f'The largest value in the second line is: {max(matrix[1])}')
input()
