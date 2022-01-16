import pygame

# initialize pygame
pygame.init()


# displaysurface
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode( (WINDOW_WIDTH, WINDOW_HEIGHT) )
pygame.display.set_caption("Burger Dog")

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()