import pygame
from pygame.locals import *
from unitclass import Unit
pygame.init()

# WINDOW DISPLAY
screen_width = 540
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Clash Royale')
icon = pygame.image.load('assets/icon.png')
pygame.display.set_icon(icon)

# Calculate the position to center the arena horizontally and align it to the top vertically
arena_width = 430  # Width of the arena
arena_height = 720  # Height of the arena
arena_x = (screen_width - arena_width) // 2
arena_y = 0

# GAME LOGIC
current_elixir = 0  # Initialize current_elixir to 0
max_elixir = 10
elixir_generation_rate = 1 / 2.8  # Elixir every 2.8 seconds
run = True
background = pygame.image.load('assets/bg.png')
deck_background = pygame.image.load('assets/deck_bg.png')

elixir_bar_images = []
for i in range(11):
    image = pygame.image.load(f'assets/elixir{i}.png')
    image = pygame.transform.scale(image, (532, 30))
    elixir_bar_images.append(image)

def display_elixir_bar(screen, current_elixir):
    # Ensure the elixir is within the valid range (0-10)
    current_elixir = max(0, min(10, current_elixir))

    # Calculate the index of the elixir bar image
    elixir_bar_index = int(current_elixir)

    # Get the corresponding elixir bar image
    elixir_bar_image = elixir_bar_images[elixir_bar_index]

    # Display elixir bar and deck bg images at correct pos
    screen.blit(deck_background,(0,screen_height - 192))
    screen.blit(elixir_bar_image, (4, screen_height - 45))

# Get the current time in milliseconds
current_time = pygame.time.get_ticks()
start_time = pygame.time.get_ticks()  # Record the starting time in milliseconds
time_limit = 300000  # 5 minutes in milliseconds (5 * 60 * 1000)

# game sounds
pygame.mixer.music.load('assets/menu_theme.mp3')
pygame.mixer.music.play(-1)

# game font
font = pygame.font.Font('assets/Helvetica_Rounded_Bold.otf', 36)

# Store the current time as the last time
last_time = current_time

# Define the size of the timer background
timer_bg_width = 100  # Adjust this as needed
timer_bg_height = 50  # Adjust this as needed
# Define some sample values for the unit parameters
# Define values for the parameters
cost = 100
hp = 250  # You didn't provide a value, so I'll assume 250
dmg = 50  # You didn't provide a value, so I'll assume 50
splash = True
hit_speed = 1.5
speed = 20  # You didn't provide a value, so I'll assume 20
deploy_time = 5
range = 6  # I assume you meant to use `_range` instead of `range`
target = "Ground"
count = 3
transport = True
height = 20.0
width = 10.0
colors = [255, 0, 0]
unit_object = Unit(
    cost, hp, dmg, splash, hit_speed, speed, deploy_time, range,
    target, count, transport, height, width, colors,0
)
toSpawn = []
# Create a Unit object

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Get the current time in milliseconds
    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - last_time

    # Calculate the time required for 1 elixir to generate (2.8 seconds in milliseconds)
    elixir_generation_time = 2.8 * 1000  # 2.8 seconds to milliseconds

    # Update elixir amount based on the elapsed time and generation rate
    elixir_to_generate = elapsed_time / elixir_generation_time
    current_elixir += elixir_to_generate

    # Ensure elixir doesn't exceed the cap
    current_elixir = min(current_elixir, max_elixir)

    # Update the last_time to the current_time for the next frame
    last_time = current_time

    # Calculate the remaining time in milliseconds
    remaining_time = time_limit - (current_time - start_time)

    # Ensure the timer doesn't go below 0
    remaining_time = max(remaining_time, 0)

    # Convert remaining time to seconds
    timer = remaining_time // 1000  # Convert milliseconds to seconds

    # Calculate minutes and seconds
    minutes = timer // 60
    seconds = timer % 60

    # Convert to "MM:SS" format
    timer_text = f"{minutes:02}:{seconds:02}"

    # Create a semi-transparent grey background for the timer text
    timer_bg_surface = pygame.Surface((timer_bg_width, timer_bg_height), pygame.SRCALPHA)
    pygame.draw.rect(timer_bg_surface, (128, 128, 128, 128), timer_bg_surface.get_rect())

    screen.fill((0, 0, 0))  # Fill the screen with a black background

    # Draw the arena in the center of the screen
    screen.blit(background, (arena_x, arena_y))

    # Call the function to display the elixir bar
    display_elixir_bar(screen, current_elixir)

    # Blit the timer background onto the screen in the top right corner
    timer_bg_rect = timer_bg_surface.get_rect(topright=(screen_width - 10, 10))
    screen.blit(timer_bg_surface, timer_bg_rect)

    # Display the timer text on top of the timer background
    timer_surface = font.render(timer_text, True, (255, 255, 255))
    timer_rect = timer_surface.get_rect(topright=(screen_width - 10, 10))
    screen.blit(timer_surface, timer_rect)
    if pygame.mouse.get_pressed()[0]:
        toSpawn = unit_object.spawnUnits(screen, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    for toDraw in toSpawn:
        pygame.draw.rect(screen,unit_object.getColor(), toDraw)

    pygame.display.update()

pygame.quit()
