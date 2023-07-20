import datetime

day = 16
month = 1
year = 1998

datapadrao = datetime.date(year, month, day)
today = datetime.date.today()

if datapadrao > today:
    delta = datapadrao - today

elif datapadrao <= today:
    delta = today - datapadrao

print(f'{delta.days} days passed')
