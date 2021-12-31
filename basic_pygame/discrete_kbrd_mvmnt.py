import pygame

# initialize pg
pygame.init()

# display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Yui discrete movement")

# set game values
VELOCITY = 10

# Load images
dragon_image = pygame.image.load(r'C:\dev\python\pygame\basic_pygame\images\dragon_right.png')
dragon_rect = dragon_image.get_rect()
dragon_rect.centerx = WINDOW_WIDTH // 2
dragon_rect.bottom = WINDOW_HEIGHT


# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # check for discrete movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dragon_rect.x -= VELOCITY
            if event.key == pygame.K_RIGHT:
                dragon_rect.x += VELOCITY
            if event.key == pygame.K_UP:
                dragon_rect.y -= VELOCITY
            if event.key == pygame.K_DOWN:
                dragon_rect.y += VELOCITY


    # fill display surface to clear
    display_surface.fill((0,0,0))

    # blit images
    display_surface.blit(dragon_image, dragon_rect)

    # update display
    pygame.display.update()


# end game
pygame.quit()