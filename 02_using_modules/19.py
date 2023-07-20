
# * ex 19 = A teacher wants to draw one of his four students to clean the board.
# * Create a program to help him by reading their names and showing the chosen student's name.

from random import choice

students = list()

for i in range(4):
    students.append(input(f"Enter the student's name #{i+1}: "))

print(f'\nThe chosen one is: {choice(students)}')
