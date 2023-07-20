
# * ex24 - Create a program that reads the name of a city and tells whether it starts with the name 'Santo' or not.

cid = str(input('In which city were you born? ')).strip()
print(cid[:5].upper() == 'SANTO')
