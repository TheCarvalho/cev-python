
# * Ex70: Create a program that reads the name and price of various products. The program should ask whether the user is going to continue or not. At the end, show:
# * A) what is the total amount spent on the purchase. B) how many products cost more than R$1000. C) what is the name of the cheapest product.

expensive = 0
name = []
value_list = []


while True:
    print('-'*30)
    name.append(input('Enter product name: '))

    value = int(input('Enter the value of the product R$'))
    value_list.append(value)

    if value > 1000:
        expensive += 1

    if continuee := input('Continue? (y or any) ').lower().strip()[0] == 'y':
        continue
    else:
        break


lower_value = min(value_list)
localizacao = value_list.index(lower_value)

print(
    f'\nThe sum of all products = R${sum(value_list)}'
    f'\n{expensive} Products cost more than R$1000'
    f'\n{name[localizacao]} is the cheapest product and costs R${lower_value}'
)
