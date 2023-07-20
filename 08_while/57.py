
# *ex57 - Make a program that reads a person's gender, but only accepts the values 'M' or 'F'. If it is wrong, ask for typing again until you have a correct value.

# [0] vai pegar só a primeira letra do input | upper = pega input em forma maiuscula | strip = desconsidera os espaços no inicio e no final do input
gender = str(input('Enter your gender (m/f): ')).strip().upper()[0]

while gender not in 'MF':
    print('invalid gender')
    gender = str(input('Enter your gender: ')).strip().upper()[0]
print('OKAY')
