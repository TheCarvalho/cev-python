# **EXE_107**

# > Create a module called coin.py that has built-in functions increase(), decrease(), double() half().
# > Also make a program that imports this module and uses some of these functions.

import coin

#! python won't import if module's name is only numbers

p = float(input('Enter the price: R$'))
print(f'\nthe half of {p} is {coin.half(p)}')
print(f'the double of {p} is {coin.double(p)}')
print(f'Increasing 10%, we get {coin.increase(p,10)}')
print(f'Decreasing 13%, we have {coin.decrease(p, 13)}')
