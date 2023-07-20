
# * ex66: Create a program that reads integers from the keyboard. The program will only stop when the user types the value 999, which is the stop condition.
# * At the end, show how many numbers were entered and what was the sum between them (disregarding the flag).

typed = sum = 0

while True:
    num = int(input('Enter a number [999 to quit]: '))
    if num == 999:
        break
    sum += num
    typed += 1
print(f'{typed} numbers were entered and their sum is {sum}')
