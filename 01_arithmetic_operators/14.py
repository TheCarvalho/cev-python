
#* Ex14: Write a program that converts a temperature entered in Celsius degrees to Fahrenheit degrees.

celsius = float(input('Enter the temperature in Celsius: '))
faren = 9 * celsius / 5 + 32

print('The temperature {:.0f} in Fahrenheit is {:.0f}'.format(celsius, faren))
