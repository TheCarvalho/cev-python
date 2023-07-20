
# *ex40 - Create a program that reads 2 grades from a student and calculates their average, showing a message at the end according to the average achieved:

# * Average lower than 5.0 = failed.
# * Average between 5.0 and 6.9 = recovery.
# * Average 7.0 or higher = approved.

nota1 = float(input('Enter your first grade: '))
nota2 = float(input('Enter your second grade: '))

average = (nota1 + nota2) / 2

if average < 5:
    print('failed')
elif average < 6.9:
    print('recovery')
else:
    print('approved')
