
# * Ex15: Write a program that asks for the amount of kilometers traveled by a rented car and the number of days it was rented for. Calculate the amount to be paid, knowing that the car costs R$60 per day and R$0.15 per kilometer traveled.

days = int(input('How many days rented? '))
km = float(input('How many kilometers traveled? '))
price = (days * 60) + (km * 0.15)


print('The total amount to be paid is R${:.2f}'.format(price))
