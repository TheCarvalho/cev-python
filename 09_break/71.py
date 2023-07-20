
# * Ex71: Create a program that simulates the operation of an ATM. At the beginning, ask the user what will be the amount to be withdrawn (integer number) and the program will inform how many bills of each value will be delivered. NOTE: consider that the cashier has R$50, R$20, R$10 and R$1 bills.

print('='*30)
print('{:^30}'.format(' ATM '))
print('='*30)

value = int(input('What amount do you want to withdraw? R$'))
total = value
ced = 50
totced = 0

while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total {totced} cells of R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 30)
