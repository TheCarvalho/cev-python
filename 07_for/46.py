
# *ex46 - make a program that shows on screen a countdown for the burst of fireworks, going from 10 to 0 with a 1 second pause between them

from os import system
from time import sleep

for x in range(10, 0, -1):
    print(x)
    sleep(1)
    system('cls')
print('\033[1;31mBOOOOM\033[m')
