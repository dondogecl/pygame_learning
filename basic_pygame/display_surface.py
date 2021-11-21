import pygame

# initialize PG
pygame.init()

# Create a display surface
WINDOW_WIDHT = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode( (WINDOW_WIDHT, WINDOW_HEIGHT) )

pygame.display.set_caption("Yui Game 1.0")


# main Game loop
running = True

while running:
    # iterate queue of game events
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False

# End of the game
pygame.quit()