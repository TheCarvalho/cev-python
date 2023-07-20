
#* ex23 - Create a program that reads a number from 0 to 9999 and displays on the screen each of its digits separately. Example: unit, ten, hundred, and thousand.

num = int(input('Enter a number from 0 to 9999: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'\nUnit: {u}')
print(f'Ten: {d}')
print(f'Hundred: {c}')
print(f'Thousand: {m}')
