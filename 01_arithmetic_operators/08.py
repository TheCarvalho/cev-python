
# *ex 8 = Write a program that reads a value in meters and displays it converted to centimeters and millimeters.

meters = float(input('Enter the value in meters: '))
print('\nThe value in centimeters is: {:.0f}cm and in millimeters is: {:.0f}mm'
      .format(meters * 100, meters * 1000))
