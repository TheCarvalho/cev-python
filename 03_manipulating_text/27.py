
# * ex27 - Create a program that reads a person's full name, and then displays the first and last names separately.
# *   First = Peter
# *   Last = Parker

full_name = str(input('Enter your full name: ')).strip()
full_name = full_name.split()
print(f'\nYour first name is {full_name[0]}\nYour last name is {full_name[-1]}')
