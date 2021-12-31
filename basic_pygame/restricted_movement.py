import pygame
from pygame import display


# initialize pygame
pygame.init()


# display

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode( (WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Restricted movement")


# load graphics
dragon_image = pygame.image.load("images\dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)


# Control Variables
VELOCITY = 5
FPS = 60
clock = pygame.time.Clock()


# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # get a list of all keys currently being held
    keys = pygame.key.get_pressed()
    
    # movement
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and dragon_rect.left > 0:
        dragon_rect.x -= VELOCITY
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and dragon_rect.right < WINDOW_WIDTH:
        dragon_rect.x += VELOCITY
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and dragon_rect.top > 0:
        dragon_rect.y -= VELOCITY    
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and dragon_rect.bottom < WINDOW_HEIGHT:
        dragon_rect.y += VELOCITY
    
    # fill display
    display_surface.fill( (0,0,0))

    # blit assets
    display_surface.blit(dragon_image, dragon_rect)

    # udpate each frame
    pygame.display.update()

    # Tick the clock
    clock.tick(FPS)


# ends pygame
pygame.quit()