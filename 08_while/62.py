
# *ex6 - Improve ex61 by asking the user if he wants to show some more terms. The program will exit when it says it wants to show 0 terms.

terms = 10
fterm = int(input('first term: '))
ratio = int(input('ratio: '))

while terms != 0:

    last = fterm + (terms-1) * ratio

    i = fterm

    while i != last:
        print(i, end=', ')
        i += ratio
    print(i)
    terms = int(input('Would you like more terms? How many? '))
