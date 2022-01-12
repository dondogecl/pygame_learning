import pygame
import os
import random

from pygame.constants import K_LEFT

# initialize pygame
pygame.init()

# set display
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("The Snake")

# Set FPS and clock
FPS = 20
clock = pygame.time.Clock()


# Set Game Variables
SNAKE_SIZE = 20

head_x = WINDOW_WIDTH // 2
head_y = WINDOW_HEIGHT //2 + 100
snake_dx = 0
snake_dy = 0
score = 0
max_score = 0


# Set Colors
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
RED = (255, 0, 0)
DARKRED = (150, 0, 0)
WHITE = (255, 255, 255)

LIGHT = (199, 240, 216)
DARK = (67, 82, 61)

# Set Fonts
font = pygame.font.SysFont('gabriola', 48)

# Set Text
title_text = font.render("~Snake~", True, GREEN, DARKGREEN)
title_rect = title_text.get_rect()
title_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

score_text = font.render(f"Score: {score}", True, GREEN, DARKRED)
score_rect = score_text.get_rect()
score_rect.topleft = (10,10)

max_score_text = font.render(f"Max: {max_score}", True, DARKGREEN, WHITE)
max_score_rect = max_score_text.get_rect()
max_width = max_score_rect.width
max_score_rect.topright = (WINDOW_WIDTH - 30, 10)
print(max_score_rect)


game_over_text = font.render("GAME OVER", True, RED, DARKGREEN)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

continue_text = font.render("Press any key to play again", True, RED, DARKGREEN)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 100)

# Set Sounds and Music
pick_up_sound = pygame.mixer.Sound(os.path.join("sounds", "5_snake_pick_up_sound.wav"))
pick_up_sound.set_volume(0.3)

# Set Images. For the rects it needs their coordinates (top-leftx, top-lefty, width, height)
apple_coord = (500, 500, SNAKE_SIZE, SNAKE_SIZE)
head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
body_coords = []

apple_rect = pygame.draw.rect(display_surface, RED, apple_coord)
head_rect = pygame.draw.rect(display_surface, DARK, head_coord)
#pygame.image.load()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # move the snake discreete
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT:
                snake_dx = -1 * SNAKE_SIZE
                snake_dy = 0

            if event.key == pygame.K_RIGHT:
                snake_dx = 1 * SNAKE_SIZE
                snake_dy = 0
            if event.key == pygame.K_UP:
                snake_dx = 0
                snake_dy = -1 * SNAKE_SIZE
            if event.key == pygame.K_DOWN:
                snake_dx = 0
                snake_dy = 1 * SNAKE_SIZE
            #print(event.key)
            #print(snake_dx, snake_dy)
            #print(head_x, head_y)

    # add the head coor to the 1st index of the body coor list
    # move all of the snakes body by one pos in the list
    body_coords.insert(0, head_coord)
    body_coords.pop()
    
    # update position of x, y of the snake head and makes a new coordinate
    head_x += snake_dx
    head_y += snake_dy
    head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)

    # Check for GAME OVER
    if head_rect.left < 0 or head_rect.right > WINDOW_HEIGHT or head_rect.top < 0 or head_rect.bottom > WINDOW_HEIGHT or head_coord in body_coords:
        print("game over condition")
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        if score > max_score:
            max_score = score
        pygame.display.update()
        # pause
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    score = 0
                    head_x = WINDOW_WIDTH //2
                    head_y = WINDOW_HEIGHT // 2 + 100
                    head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
                    body_coords = []
                    snake_dx = 0
                    snake_dy = 0
                    is_paused = False
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False


    # check collisions
    if head_rect.colliderect(apple_rect):
        score += 1
        pick_up_sound.play()
        #print("collision")

        apple_x = random.randint(0, WINDOW_WIDTH - SNAKE_SIZE)
        apple_y = random.randint(0, WINDOW_HEIGHT - SNAKE_SIZE)
        apple_coord = (apple_x, apple_y, SNAKE_SIZE, SNAKE_SIZE)
        body_coords.append(head_coord)
        title_text = font.render("", True, WHITE, WHITE)
    
    # Update HUD
    score_text = font.render(f"Score: {score}", True, GREEN, DARKRED)
    max_score_text = font.render(f"Max: {max_score}", True, DARKGREEN, WHITE)

    # fill surface
    display_surface.fill(WHITE)
    # HUD
    display_surface.blit(title_text, title_rect)
    display_surface.blit(score_text, score_rect)
    display_surface.blit(max_score_text, max_score_rect)

    # Blit assets
    head_rect = pygame.draw.rect(display_surface, GREEN, head_coord)
    apple_rect = pygame.draw.rect(display_surface, RED, apple_coord)
    for body in body_coords:
        pygame.draw.rect(display_surface, DARKGREEN, body)

    # Update display
    pygame.display.update()
    clock.tick(FPS)


# Ends the game
pygame.quit()