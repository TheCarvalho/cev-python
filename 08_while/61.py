
# *ex61 - Redo CHALLENGE 51, reading the first term and the ratio of an AP, showing the first 10 terms of the progression using the while structure.

fterm = int(input('First term: '))
ratio = int(input('Ratio: '))

last = fterm + (10-1) * ratio

i = fterm

while i != last:
    print(i, end=', ')
    i += ratio
print(i)
