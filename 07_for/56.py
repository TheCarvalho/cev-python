
# *ex56 - Write a program that reads the name, age and gender of 4 people. At the end of the program show:
# * The average age of the group
# * What is the name of the older man
# * How many women are under 20

previously_age = average = age_counter = 0

for i in range(0, 4):
    name = str(input('Name: ')).strip()
    age = int(input('Age: '))
    average += age

    if age > previously_age:
        oldest = name

    gender = str(input('Gender: ')).strip()

    if gender == 'mulher':
        if age < 20:
            age_counter += 1

    previously_age = age
    print('-'*20)

average = average / 4

print('A média do grupo é {} anos\nO nome do mais velho é {}\n{} mulheres com menos de 20 anos'.format(
    round(average),
    oldest,
    age_counter
))
