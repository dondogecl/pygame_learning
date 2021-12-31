import pygame
import random


# initialize pygame
pygame.init()

# display
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode( (WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Collision detection")


# Control variables
FPS = 60
clock = pygame.time.Clock()
VELOCITY = 5
SCORE = 0


# Define colors (RGB tuples)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
DARKGREEN = (10, 50, 10)
# define fonts
system_font = pygame.font.SysFont('calibri', 20)
# Define text fontx.render(string, antialias, colors)
system_text = system_font.render("SCORE {}".format(SCORE), True,\
    GREEN, DARKGREEN)
system_text_rect = system_text.get_rect()
system_text_rect.topleft = (0, 0)


# Loading assets
dragon_image = pygame.image.load("images\dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.topleft = (25, 25)

coin_image = pygame.image.load("images\coin-icon_32x32.png") # coin icon by https://awicons.com
coin_rect = coin_image.get_rect()
coin_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

# Load sound effects
sound_1 = pygame.mixer.Sound(r'sounds\2_basic_pygame_sound_1.wav')


# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Capture keys being pressed down
    keys = pygame.key.get_pressed()
    # Movement
    if keys[pygame.K_a] and dragon_rect.left > 0:
        dragon_rect.x -= VELOCITY # LEFT
    if keys[pygame.K_d] and dragon_rect.right < WINDOW_WIDTH:
        dragon_rect.x += VELOCITY # RIGHT
    if keys[pygame.K_w] and dragon_rect.top > 0:
        dragon_rect.y -= VELOCITY # UP
    if keys[pygame.K_s] and dragon_rect.bottom < WINDOW_HEIGHT:
        dragon_rect.y += VELOCITY # DOWN

    # checking collisions
    if dragon_rect.colliderect(coin_rect):
        coin_rect.x = random.randint(0, WINDOW_WIDTH - coin_rect.width)
        coin_rect.y = random.randint(0, WINDOW_HEIGHT - coin_rect.height)
        sound_1.play()
        SCORE += 1
    

    # Fill surface
    display_surface.fill( (0,0,0))
    # draw rectangle around sprites
    pygame.draw.rect(display_surface, (0,255,0), dragon_rect, 1)
    pygame.draw.rect(display_surface, (255,255,0), coin_rect, 1)

    # blit assets
    display_surface.blit(dragon_image, dragon_rect)
    display_surface.blit(coin_image, coin_rect)
    # blit text surfaces
    system_text = system_font.render("SCORE: {}".format(SCORE), True,\
    GREEN, DARKGREEN)
    display_surface.blit(system_text, system_text_rect)

    # update display
    pygame.display.update()

    # framerrate
    clock.tick(FPS)


# Quit pygame
pygame.quit()