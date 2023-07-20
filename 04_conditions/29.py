
# *Ex29 - Write a program that reads the speed of a car. If it exceeds 80Km/h, display a message saying that it was fined. The fine should cost R$7.00 for each Km above the limit.


speed = int(input('Enter the car speed: '))
if speed >= 80:
    print('You have just been fined')
    print('The fine amount is R${}'.format((speed - 80)*7))
else:
    print('All good')
