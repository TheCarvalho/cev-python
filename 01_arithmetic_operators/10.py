
# *ex 10 = Create a program that reads how much money is in the wallet and shows how many dollars it can buy. Consider US$1 = R$3.27.


wallet = float(input('Enter the available amount in R$: '))
print('You can buy ${:.2f} dollars.'.format(wallet / 3.27))
