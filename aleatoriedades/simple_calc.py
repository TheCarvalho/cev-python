def getInput():
    f_num = int(input('Enter first number: '))
    s_num = int(input('Enter second number: '))
    return f_num, s_num


def add():
    x, y = getInput()
    return x + y


def sub():
    x, y = getInput()
    return x - y


def div():
    x, y = getInput()
    return x // y


def mul():
    x, y = getInput()
    return x * y


def errorHandler():
    return 'Invalid choice'


print('''
    1. add
    2. sub
    3. div
    4. mul
''')


choice = int(input('Enter your choice: '))

operations = {
    1: add,
    2: sub,
    3: div,
    4: mul

}

output = operations.get(choice, errorHandler)()
print(output)
