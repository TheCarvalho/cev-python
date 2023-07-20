
# *Ex5 - Create a program that reads any year and shows if it is LEAP year.

year = int(input('Enter a year: '))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("It's leap year!!")
else:
    print("It's not leap year!!")
