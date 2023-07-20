
#* ex25 - Create a program that reads a person's name and tells if it contains 'Silva' in the name.

full_name = str(input('Enter your full name: ')).strip()
print(f'Does your name have Silva? {"SILVA" in full_name.upper()}')
