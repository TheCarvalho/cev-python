
# * Ex90: Make a program that reads a student's name and average, also saving the situation in a dictionary. At the end, show the contents of the structure on the screen.


student = dict()

student['name'] = str(input('name: '))
student['average'] = float(input(f'average of {student["name"]}: '))

if student['average'] >= 7:
    student['situation'] = 'approved'
elif 5 <= student['average'] < 7:
    student['situation'] = 'failed'

print('-'*30)
for k, v in student.items():
    print(f' - {k} = {v}')
