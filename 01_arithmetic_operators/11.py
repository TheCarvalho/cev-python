
# *ex 11 = Create a program that reads the width and height of a wall in meters, calculates its area, and determines the amount of paint needed to paint it, knowing that each liter of paint covers an area of 2m².


width = float(input('Enter the width: '))
height = float(input('Enter the height: '))

paint = 2

print('The area is {:.1f}m² and you will need {:.1f} liters of paint.'
      .format(width*height, (height*width)/paint))
