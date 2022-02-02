import pygame
from pygame import sprite
import random

# initialize
pygame.init()
FPS = 60
clock = pygame.time.Clock()

# Display surface
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode( (WINDOW_WIDTH, WINDOW_HEIGHT) )
pygame.display.set_caption("Group collision")


# Define classes



# Instantiate objects



# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill display
    display_surface.fill(( 0,0,0 ))

    # update display
    pygame.display.update()
    clock.tick(FPS)


# Ends Pygame
pygame.quit()