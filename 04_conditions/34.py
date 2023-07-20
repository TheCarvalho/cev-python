
# *Ex34 - Write a program that asks for an employee's salary and calculates the value of their raise. For salaries above R$1250.00, calculate a 10% raise. For salaries equal to or below, the raise is 15%.


salary = int(input('Enter your salary: '))
print('Your salary will be adjusted to: R$', end='')
print(
    (salary * 0.1) + salary if salary > 1250
    else (salary * 0.15) + salary
)
