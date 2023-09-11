import pygame
import time
import threading
from pygame.locals import *

pygame.init()


#  WINDOW DISPLAY
screen_width = 720          #placeholder resolutions
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Clash Royale')
icon = pygame.image.load('assets/icon.png')
pygame.display.set_icon(icon)


# GAME LOGIC
elixir = 0
elixir_speed = 2.8
run = True
game_time = 300


#image loader
elixir_state = []
for elixir_level in range(0,11):
    eimg = pygame.image.load(f'assets/elixir{elixir_level}.png')
    elixir_state.append(eimg)
bg = pygame.image.load('assets/bg.png')    

#game sounds
pygame.mixer.music.load('assets/menu_theme.mp3')
pygame.mixer.music.play(-1)

#game font
font = pygame.font.Font('assets/Helvetica_Rounded_Bold.otf', 36)

def game_timer():
    global game_time
    while True:
        # update time and generate new image for current time
        if game_time > 0:
            game_time -= 1
        convert = time.strftime("%M:%S", time.gmtime(game_time))
        time_img = font.render(convert, True, (255,255,255))
        # create surface to draw time onto
        screen_surface = pygame.Surface((200, 100))
        screen_surface.fill((0,0,0))
        # draw updated time onto screen
        screen_surface.blit(time_img,(0,0))
        screen.blit(screen_surface, (600, 50))
        pygame.display.update()

        time.sleep(1)
        print(convert)

def elixir_counter():
    global elixir, elixir_speed, screen
    while True:
        # updating on-screen elixir to match elixir value  
        screen.blit(elixir_state[elixir], (72, 627))
        pygame.display.update()
        #double elixir grants +1 elixir to player
        if game_time == 180:
            if(elixir<10):
                elixir += 1
                print("elixir gained", elixir)  
        # double elixir
        if game_time <= 180:
            elixir_speed = 1.4
        # triple elixir
        if game_time == 60:
            elixir_speed = 0.9
        # elixir cap
        if elixir < 10:
            elixir += 1

        time.sleep(elixir_speed)
        print("elixir gained", elixir)

elixir_thread = threading.Thread(target=elixir_counter)
elixir_thread.daemon = True
elixir_thread.start()

gametimer_thread = threading.Thread(target=game_timer)
gametimer_thread.daemon = True
gametimer_thread.start()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update

pygame.quit()