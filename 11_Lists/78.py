
# * EXE_78 - Write a program that reads 5 numerical values and stores them in a list. At the end, show which was the largest and smallest value typed and their respective positions in the list.

numbers_list = list()

for i in range(0, 5):
    num = int(input('Insira o valor: '))
    numbers_list.append(num)

print(
    f'O maior valor digitado foi {max(numbers_list)} '
    f'e sua posição é {numbers_list.index(max(numbers_list))+1}')
print(
    f'O menor valor digitado foi {min(numbers_list)} '
    f'e sua posição é {numbers_list.index(min(numbers_list))+1}')
