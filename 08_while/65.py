
# *ex65 - Create a program that reads several integers from the keyboard. At the end of the execution, display the average of all the values and which was the highest and lowest values read. The program should ask the user whether or not he wants to continue typing values.

list = []
continuee = 'y'

while continuee == 'y':

    num = int(input('Enter a number: '))
    list.append(num)
    continuee = str(input('Continue?? [y/n] ')).strip().lower()[0]

average = sum(list)/len(list)

print(
    f'the average is {average}\n'
    f'highest value is {max(list)}\n'
    f'lowest values is {min(list)}'
)
