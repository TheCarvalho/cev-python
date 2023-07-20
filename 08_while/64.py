
# *ex64 - Create a program that reads several integers from the keyboard. The program will only stop when the user types the value 999, which is the stop condition. At the end, show how many numbers were entered and what was the sum between them (disregarding the flag).

num = sum = typed = 0

while num != 999:
    sum += num
    typed += 1
    num = int(input("Enter a number: "))
print('Were typed', typed-1, '\nTheir sum is', sum)
