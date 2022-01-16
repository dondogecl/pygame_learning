import pygame
import random

# initialize pygame
pygame.init()


# displaysurface
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CENTER_X = WINDOW_WIDTH//2
CENTER_Y = WINDOW_HEIGHT//2
display_surface = pygame.display.set_mode( (WINDOW_WIDTH, WINDOW_HEIGHT) )
pygame.display.set_caption("Burger Dog")

# Set FPS and Clock
FPS = 60
clock = pygame.time.Clock()

# Set game Values
PLAYER_STARTING_LIVES = 3
PLAYER_NORMAL_VELOCITY = 5
PLAYER_BOOST_VELOCITY = 10
STARTING_BOOST_LEVEL = 100
STARTING_BURGER_VELOCITY = 3
BURGER_ACCELERATION = .25
BUFFER_DISTANCE = 100

score = 0
burger_points = 0
burgers_eaten = 0

player_lives = PLAYER_STARTING_LIVES
player_velocity = PLAYER_NORMAL_VELOCITY

boost_level = STARTING_BOOST_LEVEL

burger_velocity = STARTING_BURGER_VELOCITY


# Set Colors
ORANGE = (246, 170, 54)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# Set Fonts
font = pygame.font.Font("fonts/WashYourHand.ttf", 32)

# Set Text
points_text = font.render(f"Burger Points: {burger_points}", True, ORANGE)
points_rect = points_text.get_rect()
points_rect.topleft = (10, 10)

score_text = font.render(f"Score: {score}", True, ORANGE)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 50)

title_text = font.render(f"Burger Dog", True, ORANGE)
title_rect = title_text.get_rect()
title_rect.centerx = CENTER_X
title_rect.y = 10

eaten_text = font.render(f"Burgers Eaten: {burgers_eaten}", True, ORANGE)
eaten_rect = eaten_text.get_rect()
eaten_rect.centerx = CENTER_X
eaten_rect.y = 50

lives_text = font.render(f"Lives: {player_lives}", True, ORANGE)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 10, 10)

boost_text = font.render(f"Boost: {boost_level}", True, ORANGE)
boost_rect = boost_text.get_rect()
boost_rect.topright = (WINDOW_WIDTH -10, 50)

game_over_text = font.render(f"FINAL SCORE: {score}", True, ORANGE)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (CENTER_X, CENTER_Y)

continue_text = font.render("Press any key to play again", True, ORANGE)
continue_rect = continue_text.get_rect()
continue_rect.center = (CENTER_X, CENTER_Y + 64)


# Set music
bark_sound = pygame.mixer.Sound("sounds/6_burger_dog_bark_sound.wav")
miss_sound = pygame.mixer.Sound("sounds/6_burger_dog_miss_sound.wav")
pygame.mixer.music.load("sounds/bd_background_music.wav")


# Set Images
player_image = pygame.image.load("images/22215-dog-icon.png")
player_rect = player_image.get_rect()
player_rect.centerx = CENTER_X
player_rect.bottom = WINDOW_HEIGHT

burger_image = pygame.image.load("images/32382-hamburger-icon.png")
burger_rect = burger_image.get_rect()
burger_rect.topleft = ( random.randint( 0, WINDOW_WIDTH - player_image.get_width() ), - BUFFER_DISTANCE )


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # FILL SURFACE
    display_surface.fill(BLACK)

    # Blit the HUD
    display_surface.blit(points_text, points_rect)
    display_surface.blit(score_text, score_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(eaten_text, eaten_rect)
    display_surface.blit(lives_text, lives_rect)
    display_surface.blit(boost_text, boost_rect)
    pygame.draw.line(display_surface, WHITE, (0,100),(WINDOW_WIDTH, 100), 3)

    # Blit Assets
    display_surface.blit(player_image, player_rect)
    display_surface.blit(burger_image, burger_rect)

    # Update screen and tick clock
    pygame.display.update()
    clock.tick(FPS)


pygame.quit()