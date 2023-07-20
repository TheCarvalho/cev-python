
# *ex8 - Develop a logic that reads a person's weight and height, calculates their BMI and shows their states according to the table below:

# * Under 18.5 = Underweight.
# * Between 18.5 and 25 = Ideal weight.
# * 25 to 30 = Overweight.
# * 30 to 40 = Morbid obesity.

weight = float(input('enter your weight: '))
height = float(input('enter your height (x.xx): '))
bmi = weight / (height ** 2)

if bmi < 18.5:
    print('Underweight')
elif bmi < 25:
    print('Ideal weight')
elif bmi < 30:
    print('Overweight')
elif bmi < 40:
    print('Morbid obesity')
else:
    print('Get some help!!')
