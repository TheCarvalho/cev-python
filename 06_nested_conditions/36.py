
# *ex36 - Write a program to approve the bank loan for buying a house. The program will ask for the house value, the buyer's salary, and the number of years they will pay. Calculate the monthly installment value, knowing that it cannot exceed 30% of the salary, otherwise, the loan will be denied.

housevalue = float(input('House value: '))
salary = float(input('Your monthly salary.: '))
years = float(input('How many years will you pay? '))

installment = (housevalue / years) / 12

print('The installment will be {:.2f}'.format(installment))

if installment > ((salary * 30) / 100):
    print('Loan Denied')
else:
    print('Loan Accepted')
