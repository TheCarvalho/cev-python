
#* ex22 - Create a program that reads a person's full name and displays:
# *  The name in all uppercase letters
# *  The name in all lowercase letters
# *  How many letters in all (not including spaces)
# *  How many letters are in the first name

full_name = str(input('Enter your full name: '))


print(full_name.upper())
print(full_name.lower())

print(f'\nYour name has {len(full_name) - full_name.count(" ")} letters')

full_name = full_name.split()
print('Seu primeiro nome tem {} letras'.format(len(full_name[0])))
