import pygame
from pygame.constants import QUIT

# initialize PG
pygame.init()

# Create a display surface and its caption
WINDOW_WIDHT = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode( (WINDOW_WIDHT, WINDOW_HEIGHT) )
pygame.display.set_caption("Yui Game 1.0")


# Define colors (RGB tuples)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# BACKGROUND COLOR
display_surface.fill(BLUE)

# Draws shapes on our display
# Line(surface, color, start point, end pint, thickness)
pygame.draw.line(display_surface, RED, (0,0), (100,100), 5)
pygame.draw.line(display_surface, GREEN, (100,100), (200,300), 2)

# Circle (surface, color, center, radius, thickness or 0 = fill )
pygame.draw.circle(display_surface, WHITE, \
 (WINDOW_WIDHT//2, WINDOW_HEIGHT//2), 200, 6)
pygame.draw.circle(display_surface, YELLOW, \
 (WINDOW_WIDHT//2, WINDOW_HEIGHT//2), 195, 0)

# Rectangle (surface, color, (top-left-x, top-left-y, width, height))
pygame.draw.rect(display_surface, CYAN, (500, 0, 100, 100))
pygame.draw.rect(display_surface, MAGENTA, (500, 100, 50, 100))


# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    # update the display
    pygame.display.update()


# End the game
pygame.quit()
