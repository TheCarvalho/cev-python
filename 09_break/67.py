
# * Ex67: Write a program that displays the table of several numbers, one at a time, for each value entered by the user. The program will stop when the requested number is negative.

title = ' Table '
counter = 1

print(f'{title:=^30}')

while True:
    num = int(
        input('Enter a number for the multiplication table: [Negative number to leave]\n> '))
    print('-'*30)
    if num < 0:
        break
    while counter <= 10:
        print(f'{num}  x {counter:2}  =  {num * counter}')
        counter += 1
    print('-'*30)
    counter = 1
input()
