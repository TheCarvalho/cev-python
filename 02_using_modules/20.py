
# * ex 20 = The same teacher from the previous challenge wants to draw the presentation order of the students' assignments. Create a program that reads the names of the four students and displays the randomly sorted order.

from random import shuffle

students = list()

for i in range(4):
    students.append(input(f"Enter the student's  #{i+1}: "))


shuffle(students)
print('\nA ordem ficou: ',
      *students)
