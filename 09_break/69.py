
# * Ex69: Create a program that reads the age and gender of multiple people. For each person registered, the program should ask if the user wants to continue or not.
# * At the end, show: A) how many people are over 18 years old. B) how many men were registered. C) how many women are under 20 years old.

person = men = fminors = 0

while True:
    sex = option = 'y'

    print('-'*30)
    age = int(input('age: '))

    while sex not in 'mf':
        sex = input('sex: [m/f] ').lower().strip()[0]

    if age >= 18:
        person += 1
    if sex == 'm':
        men += 1
    if sex == 'f' and age < 20:
        fminors += 1

    option = input('Continue? [y or any] ').lower().strip()[0]

    if option == 'y':
        continue
    else:
        break

print(
    f'\n{person} people are over 18\n'
    f'{men} registered men\n'
    f'{fminors} women under 20'
)
