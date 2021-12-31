import pygame
import os
import random


# init pygame
pygame.init()

# set FPS and clock

# display surface
WINDOW_WIDTH = 945
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode( (WINDOW_WIDTH, WINDOW_HEIGHT) )
pygame.display.set_caption("Catch the clown")

# Set FPS and clock
FPS = 60
clock = pygame.time.Clock()


# Set Game values
PLAYER_STARTING_LIVES = 5
CLOWN_STARTING_VELOCITY = 3
CLOWN_ACCELERATION = 1

score = 0
max_score = 0
player_lives = PLAYER_STARTING_LIVES
clown_velocity = CLOWN_STARTING_VELOCITY
clown_dx = random.choice([-1, 1]) # direction X
clown_dy = random.choice([-1, 1]) # direction Y

# Set colors
BLUE = (1, 175, 209)
YELLOW = (248, 231, 28)


# Set fonts
font = pygame.font.Font(os.path.join("fonts", "Franxurter.ttf"), 32)

# Texts
title_text = font.render("Catch the Clown", True, BLUE)
title_rect = title_text.get_rect()
title_rect.topleft = (50,10)

score_text = font.render(f"Score: {score}", True, YELLOW)
score_rect = score_text.get_rect()
score_rect.topright = (WINDOW_WIDTH - 50, 10)

lives_text = font.render(f"Lives: {player_lives}", True, YELLOW)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 50, 50)

gameover_text = font.render("GAME OVER", True, BLUE, YELLOW)
gameover_rect = gameover_text.get_rect()
gameover_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

continue_text = font.render("Click anywhere to play again", True, YELLOW, BLUE)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 64)

maxscore_text = font.render(f"Max: {max_score}", True, YELLOW)
maxscore_rect = maxscore_text.get_rect()
maxscore_rect.topright = (WINDOW_WIDTH -50, 90)

# Sound and music
hit_sound = pygame.mixer.Sound(os.path.join("sounds", "4_catch_the_clown_click_sound.wav"))
hit_sound.set_volume(0.1)
miss_sound = pygame.mixer.Sound(os.path.join("sounds", "4_catch_the_clown_miss_sound.wav"))
miss_sound.set_volume(0.1)

pygame.mixer.music.load(os.path.join("sounds", "4_catch_the_clown_ctc_background_music.wav"))
pygame.mixer.music.set_volume(0.2)

# Images
background_image = pygame.image.load(os.path.join("images", "background.png"))
background_rect = background_image.get_rect()
background_rect.topleft = (0,0)

clown_image = pygame.image.load(os.path.join("images", "clown.png"))
clown_rect = clown_image.get_rect()
clown_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)


# Main Game Loop
pygame.mixer.music.play(-1, 0.0)
running = True
while running:
    # EVENT LOOP
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Click listener
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            
            # check if there is a collision with the click
            if clown_rect.collidepoint(mouse_x, mouse_y):
                hit_sound.play()
                score += 1
                #print(score)
                clown_velocity += CLOWN_ACCELERATION
                #print(clown_velocity)
                # change direction
                previous_dx = clown_dx
                previews_dy = clown_dy
                while (previous_dx == clown_dx and previews_dy == clown_dy):
                    clown_dx = random.choice([-1, 1])
                    clown_dy = random.choice([-1, 1])
            else:
                miss_sound.play()
                player_lives -= 1
                #print(player_lives)

    
    # Move the clown character
    clown_rect.x += clown_dx * clown_velocity
    clown_rect.y += clown_dy * clown_velocity
    # bounce the clown off the edges
    if clown_rect.left <= 0 or clown_rect.right >= WINDOW_WIDTH:
        clown_dx = -1 * clown_dx
    if clown_rect.top <= 0 or clown_rect.bottom >= WINDOW_HEIGHT:
        clown_dy = -1 * clown_dy

    # Update HUD
    score_text = font.render(f"Score: {score}", True, YELLOW)
    lives_text = font.render(f"Lives: {player_lives}", True, YELLOW)
    maxscore_text = font.render(f"Max: {max_score}", True, YELLOW)
    # Blit background
    display_surface.blit(background_image, background_rect)
    # Blit HUD
    display_surface.blit(title_text, title_rect)
    display_surface.blit(score_text, score_rect)
    display_surface.blit(lives_text, lives_rect)
    display_surface.blit(maxscore_text, maxscore_rect)
    # blit images
    display_surface.blit(clown_image, clown_rect)

    # check Game Over condition
    if player_lives == 0:
        display_surface.blit(gameover_text, gameover_rect)
        display_surface.blit(continue_text, continue_rect)
        pygame.display.update()
        if score > max_score:
            max_score = score
        # Pause and continue
        pygame.mixer.music.stop()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    score = 0
                    player_lives = PLAYER_STARTING_LIVES
                    clown_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)
                    clown_velocity = CLOWN_STARTING_VELOCITY
                    clown_dx = random.choice([-1, 1])
                    clown_dy = random.choice([-1, 1])
                    pygame.mixer.music.play(-1, 0)
                    is_paused = False
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False
        


    #update display
    pygame.display.update()
    clock.tick(FPS)


# Quit pygame
pygame.quit()