
# *ex 12 = Create an algorithm that reads the price of a product and shows its new price, with a 5% discount."

price = float(input('Enter the value: '))

discount = price * 0.05
new_price = price - discount

print('Novo valor com 5% de desconto: R${:.2f}'.format(new_price))
