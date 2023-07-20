
# *ex41 - The National Swimming Confederation needs a program that reads the year of birth of an athlete and shows his category according to age.

# * Up to 9 years old is child.
# * Up to 14 years old is childish.
# * Up to 19 years is Junior.
# * Up to 20 years is senior.
# * Above is master.

birth = int(input('Enter the year of birth: '))
year = 2021
result = year - birth

if result <= 9:
    print('Child')
elif result <= 14:
    print('Childish')
elif result <= 19:
    print('Junior')
elif result <= 20:
    print('Senior')
else:
    print('Master')
