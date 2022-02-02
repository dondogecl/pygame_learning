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


class Player(Sprite):
    """
    Class for the player
    """
    def __init__(self, x, y, monster_group):
        super().__init__()
        self.image= pygame.image.load("images/Knight-icon.png")#.convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.velocity = 5
        self.monster_group = monster_group

    def update(self):
        self.move()
        self.check_collisions()

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.velocity
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.velocity
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.velocity

    def check_collisions(self):
        if pygame.sprite.spritecollide(self, self.monster_group, True):
            print(len(self.monster_group))


# Create monster group
monster_group = pygame.sprite.Group()
for i in range(10):
    monster = Monster(i*64, 10)
    monster_group.add(monster)

# Create player group
player_group = pygame.sprite.Group()
player = Player(WINDOW_WIDTH//2, 500, monster_group)
player_group.add(player)





# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill display
    display_surface.fill(( 0,0,0))

    # draw
    player_group.update()
    monster_group.update()
    player_group.draw(display_surface)
    monster_group.draw(display_surface)

    # update display
    pygame.display.update()
    clock.tick(FPS)


# Ends Pygame
pygame.quit()