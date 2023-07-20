
# *Ex33 -  Create a program that reads 3 numbers and shows which one is the largest and which one is the smallest.

num = list()

for i in range(3):
    num.append(int(input(f'Enter number #{i+1}: ')))

print('\nlargest number: ', max(num))
print('smallest number: ', min(num))
