
#* ex21 = Create a Python program that opens and plays an MP3 audio file.

import pygame  # pip install pygame

pygame.init()
pygame.mixer.music.load('rapaz.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input()


# import os
# print(os.getcwd())   # para ver aonde está sendo executado o script
