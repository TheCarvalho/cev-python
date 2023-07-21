
# EX113 - Rewrite the leiaint() function we did in 'Challenge 104', now including the possibility of typing an invalid type number. Create also a function LeiaFloat() with the same functionality.

def leiaint(num):
    while True:
        try:
            n = int(input(num))
        except (ValueError, TypeError):
            print('Error : Please enter a valid integer')
            continue
            print('teste')
        except (KeyboardInterrupt):  # ctrl c
            print('User preferred not to type')
            return 0
        else:
            return n


n1 = leiaint('Enter a integer: ')
print(f'The integer value entered was {n1}')
