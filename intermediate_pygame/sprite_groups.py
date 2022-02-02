import pygame
from pygame.sprite import Sprite
import random

# Initialize pygame
pygame.init()
FPS = 60
clock = pygame.time.Clock()

# Display surface
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode( (WINDOW_WIDTH, WINDOW_HEIGHT) )
pygame.display.set_caption("Sprite groups")

# Define Classes
class Monster(Sprite):
    """
    Class for the monster
    """
    def __init__(self, x, y):
        super().__init__()
        self.image= pygame.image.load("images/Blue-Monster-icon.png")#.convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.velocity = random.randint(1, 10)

    def update(self):
        """ Update and move monster """
        self.rect.y += self.velocity


# Create monster group
monster_group = pygame.sprite.Group()
for i in range(10):
    monster = Monster(i*64, 10)
    monster_group.add(monster)


# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill display
    display_surface.fill(( 0,0,0))

    # draw
    monster_group.update()
    monster_group.draw(display_surface)

    # update display
    pygame.display.update()
    clock.tick(FPS)


# Ends Pygame
pygame.quit()