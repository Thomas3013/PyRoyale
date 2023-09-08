import pygame
from pygame.locals import *

pygame.init()


#  WINDOW DISPLAY
screen_width = 720          #placeholder resolutions
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Clash Royale')
icon = pygame.image.load('assets/icon.png')
pygame.display.set_icon(icon)

#game sounds
pygame.mixer.music.load('assets/menu_theme.mp3')
pygame.mixer.music.play(-1)


# GAME LOGIC
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update

pygame.quit()