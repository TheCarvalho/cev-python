
# * EXE_83 - Create a program where the user types any expression that uses parentheses. Your application should analyze whether the passed expression has the open and closed parentheses in the correct order.


expr = str(input('Enter the expression: '))
pile = []

for simb in expr:
    if simb == '(':
        pile.append('(')
    elif simb == ')':
        if len(pile) > 0:
            pile.pop()
        else:
            pile.append(')')
            break

if len(pile) == 0:
    print('Your expression is valid')
else:
    print('Your expression is wrong')
