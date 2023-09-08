import pygame
from pygame.locals import *

pygame.init()


#  WINDOW DISPLAY
screen_width = 720          #placeholder resolutions
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Clash Royale')



# GAME LOGIC
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update

pygame.quit()