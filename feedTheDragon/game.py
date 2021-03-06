import pygame
import os
import random

from pygame.constants import KEYDOWN

# initialize
pygame.init()

# display
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode( (WINDOW_WIDTH, WINDOW_HEIGHT) )
pygame.display.set_caption("Feed the Dragon")

# Set FPS and Clock
FPS = 60
clock = pygame.time.Clock()

# Set game values
PLAYER_STARTING_LIVES = 5
PLAYER_STARTING_VELOCITY = 5
PLAYER_ACCELERATION = 0.25
COIN_STARTING_VELOCITY = 7
COIN_ACCELERATION = 1
BUFFER_DISTANCE = 100
HUD_BOTTOM = 64
PLAYER_HEIGHT = 32
COIN_HEIGHT = 32

score = 0
player_lives = PLAYER_STARTING_LIVES
coin_velocity = COIN_STARTING_VELOCITY
player_velocity = PLAYER_STARTING_VELOCITY


# Set colors
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# Set fonts
font = pygame.font.Font(os.path.join("fonts", "AttackGraffiti-3zRBM.ttf"), 32)

# Text
score_text = font.render(f"SCORE: {score}", True, GREEN, DARKGREEN)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

title_text = font.render(f"Feed the Dragon", True, GREEN, WHITE)
title_rect = title_text.get_rect()
title_rect.centerx = WINDOW_WIDTH // 2
title_rect.y = 10

lives_text = font.render(f"LIVES: {player_lives}", True, GREEN, DARKGREEN)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH -10, 10)

game_over_text = font.render("GAMEOVER", True, GREEN, DARKGREEN)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

continue_text = font.render("Press any key to play again...", True, GREEN, DARKGREEN)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 32)


# Sounds and music
coin_sound =  pygame.mixer.Sound(os.path.join("sounds", "3_feed_the_dragon_coin_sound.wav"))
miss_sound = pygame.mixer.Sound(os.path.join("sounds", "3_feed_the_dragon_miss_sound.wav"))
coin_sound.set_volume(0.1)
miss_sound.set_volume(0.1)
pygame.mixer.music.load(os.path.join("sounds", "2_basic_pygame_music.wav"))
pygame.mixer.music.set_volume(0.08)


# Images
player_image = pygame.image.load(os.path.join("images", "dragon_right.png"))
player_rect = player_image.get_rect()
player_rect.left = 32
player_rect.centery = WINDOW_HEIGHT // 2

coin_image = pygame.image.load(os.path.join("images", "coin-icon_32x32.png"))
coin_rect = coin_image.get_rect()
coin_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
coin_rect.y = random.randint(HUD_BOTTOM, WINDOW_HEIGHT - COIN_HEIGHT)


# game loop
pygame.mixer.music.play(-1, 0.0)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # checking user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_rect.top > HUD_BOTTOM:
        player_rect.y -= player_velocity
    if keys[pygame.K_DOWN] and player_rect.bottom <  WINDOW_HEIGHT:
        player_rect.y += player_velocity

    # move the coin
    if coin_rect.x < 0: #player missed the coin
        player_lives -= 1
        miss_sound.play()
        coin_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
        coin_rect.y = random.randint(HUD_BOTTOM, WINDOW_HEIGHT - COIN_HEIGHT)
    else: # move the coin
        coin_rect.x -= coin_velocity

    # Checking collisions
    if player_rect.colliderect(coin_rect):
        score += 1
        coin_sound.play()
        if coin_velocity <= 20:
            coin_velocity += COIN_ACCELERATION
            player_velocity += PLAYER_ACCELERATION
        coin_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
        coin_rect.y = random.randint(HUD_BOTTOM, WINDOW_HEIGHT - COIN_HEIGHT)
        
        
        
    # Update values of the HUD
    score_text = font.render(f"SCORE: {score}", True, GREEN, DARKGREEN)
    lives_text = font.render(f"LIVES: {player_lives}", True, GREEN, DARKGREEN)

    # GAMEOVER
    if player_lives == 0:
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        display_surface.blit(lives_text, lives_rect)
        pygame.display.update()
        # pause the game
        pygame.mixer.music.stop()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    score = 0
                    player_lives = PLAYER_STARTING_LIVES
                    player_rect.y = WINDOW_HEIGHT // 2
                    coin_velocity = COIN_STARTING_VELOCITY
                    player_velocity = PLAYER_STARTING_VELOCITY
                    pygame.mixer.music.play(-1, 0.0)
                    is_paused = False
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

    
    # fill display
    display_surface.fill(BLACK)

    # blit HUD
    display_surface.blit(score_text, score_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(lives_text, lives_rect)
    pygame.draw.line(display_surface, WHITE, (0, HUD_BOTTOM), (WINDOW_WIDTH, HUD_BOTTOM), 2)
    
    # blit assets to the screen
    display_surface.blit(player_image, player_rect)
    display_surface.blit(coin_image, coin_rect)

    # update display and clock
    pygame.display.update()
    clock.tick(FPS)



# quit pygame
pygame.quit()