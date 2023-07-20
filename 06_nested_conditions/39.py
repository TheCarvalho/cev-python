
# *ex39 - Make a program that reads the year of birth of a young person according to their age:
# * If he is still going to enlist in the military
# * If it's time to enlist.
# * If the enlistment time has passed.
# * Your program should also show the time left or overdue.

from datetime import date
year = date.today().year


birth = int(input('Birth date: '))
result = year - birth

if result == 18:
    print("It's time to enlist")
elif result < 18:
    print(f"{(result-18)*-1} years left for you to enlist")
else:
    print(f"it's been {(result-18)} years past your enlistment time")
