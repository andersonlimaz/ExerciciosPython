#faça um programa em python que abra e reproduza o audo em um arquivo MP3
import pygame 
import time
pygame.init()
pygame.mixer.music.load('Musica.mp3')
pygame.mixer.music.play()
pygame.time.delay(5000)
pygame.event.wait()