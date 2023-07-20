
# *ex54 - Create a program that reads the year of birth of seven people. at the end, show how many people have not yet reached the age of majority and how many are already of age. Consider age of majority as 21 years old

from datetime import date
minors = adults = 0
year = date.today().year
colors = {
    'red': '\033[1;31m',
    'green': '\033[1;32m',
    'clear': '\033[m'
}

for i in range(0, 7):
    birth = int(input('Enter your date of birth: '))
    age = year - birth
    if age < 21:
        minors += 1
    else:
        adults += 1

print('{3}{0} adults{4} and {2}{1} minors{4}'.format(
    adults,
    minors,
    colors["red"],
    colors["green"],
    colors["clear"]
))
