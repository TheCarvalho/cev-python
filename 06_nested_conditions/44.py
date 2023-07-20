
# *ex44 - Create a program that calculates the amount to be paid for a product, considering its normal price and the payment condition:

# * Cash/check payment = 10% discount
# * 1x on credit card= 5% discount
# * 2x on credit card = normal price
# * 3x or more on credit card = 20% interest

price = float(input('Price of the product '))
payment = int(input("""
0 - cash/check
1 - 1x credit card
2 - 2x credit card
3 - 3x or more on credit card
> """))

if payment == 0:
    print('You have 10% off R$', price-(price*0.10))
elif payment == 1:
    print('You have 5% off R$', price-(price*0.05))
elif payment == 2:
    print('normal price R$', price)
elif payment == 3:
    print('20% interest R$', price+(price*0.20))
