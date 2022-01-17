import pygame
import random
import time

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
BOOST_ACCELERATION = 20
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
boost_bonus = 1.0


# Set Colors
ORANGE = (246, 170, 54)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BOOST_LOW_COLOR = (255, 0, 0)
BOOST_MEDIUM_COLOR = (255, 255, 0)
BOOST_FULL_COLOR = (0, 255, 0)


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

boost_text = font.render(f"Boost:", True, ORANGE)
boost_rect = boost_text.get_rect()
boost_rect.x = (WINDOW_WIDTH - boost_text.get_width() - 80 )
boost_rect.y = (50)

game_over_text = font.render(f"FINAL SCORE: {score}", True, ORANGE)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (CENTER_X, CENTER_Y)

continue_text = font.render("Press any key to play again", True, ORANGE)
continue_rect = continue_text.get_rect()
continue_rect.center = (CENTER_X, CENTER_Y + 64)


# Set music
bark_sound = pygame.mixer.Sound("sounds/6_burger_dog_bark_sound.wav")
bark_sound.set_volume(0.1)
miss_sound = pygame.mixer.Sound("sounds/6_burger_dog_miss_sound.wav")
miss_sound.set_volume(0.1)
pygame.mixer.music.load("sounds/bd_background_music.wav")


# Set Images
player_image_left = pygame.image.load("images/22215-dog-icon.png")
player_image_right = pygame.transform.flip(player_image_left, True, False)
player_image_dead = pygame.transform.flip(player_image_left, False, True)
player_image = player_image_left
player_rect = player_image.get_rect()
player_rect.centerx = CENTER_X
player_rect.bottom = WINDOW_HEIGHT

burger_image = pygame.image.load("images/32382-hamburger-icon.png")
burger_rect = burger_image.get_rect()
burger_rect.topleft = ( random.randint( 0, WINDOW_WIDTH - player_image.get_width() ), - BUFFER_DISTANCE )


# start screen
welcome_text = font.render("Catch the burgers and get a boost!", True, ORANGE)
welcome_text_rect = welcome_text.get_rect()
welcome_text_rect.centerx = CENTER_X
welcome_text_rect.centery = CENTER_Y
display_surface.blit(welcome_text, welcome_text_rect)

instructions_text = font.render("Instructions:\nUse arrows to Move and Space to get a boost", True, WHITE)
instructions_rect = instructions_text.get_rect()
instructions_rect.centerx = CENTER_X
instructions_rect.centery = CENTER_Y + 50
display_surface.blit(instructions_text, instructions_rect)
pygame.display.update()
time.sleep(3)

welcome_text_2 = font.render("(or the dog will die)", True, BOOST_LOW_COLOR)
welcome_text_rect_2 = welcome_text_2.get_rect()
welcome_text_rect_2.centerx = CENTER_X
welcome_text_rect_2.centery = CENTER_Y + 100
display_surface.blit(welcome_text_2, welcome_text_rect_2)
pygame.display.update()
time.sleep(1)

# Main game loop
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # movements
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player_rect.left > 0:
        if player_image == player_image_right:
            player_image = player_image_left
        player_rect.x -= player_velocity
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player_rect.right < WINDOW_WIDTH:
        if player_image == player_image_left:
            player_image = player_image_right
        player_rect.x += player_velocity
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and player_rect.top > 103:
        player_rect.y -= player_velocity
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and player_rect.bottom < WINDOW_HEIGHT:
        player_rect.y += player_velocity
    # engage boost
    if (keys[pygame.K_SPACE] or keys[pygame.K_RCTRL]) and boost_level > 0:
        player_velocity = PLAYER_BOOST_VELOCITY * boost_bonus
        boost_level -= 1
    else:
        player_velocity = PLAYER_NORMAL_VELOCITY
    
    # burger movement
    burger_rect.y += burger_velocity
    burger_points = int( (WINDOW_HEIGHT - burger_rect.y + 1) * burger_velocity )
    # burger missed
    if burger_rect.y > WINDOW_HEIGHT:
        player_lives -= 1
        miss_sound.play()
        burger_rect.topleft = ( random.randint( 0, WINDOW_WIDTH - player_image.get_width() ), - BUFFER_DISTANCE )
        burger_velocity = STARTING_BURGER_VELOCITY
        boost_bonus = 1

        player_rect.centerx = CENTER_X
        player_rect.bottom = WINDOW_HEIGHT
        boost_level = STARTING_BOOST_LEVEL
    # collision detection
    if player_rect.colliderect(burger_rect):
        score += burger_points
        burgers_eaten += 1
        bark_sound.play()
        burger_rect.topleft = ( random.randint( 0, WINDOW_WIDTH - player_image.get_width() ), - BUFFER_DISTANCE )
        burger_velocity += BURGER_ACCELERATION
        boost_level += BOOST_ACCELERATION
        if boost_level > STARTING_BOOST_LEVEL:
            boost_level = STARTING_BOOST_LEVEL
        if burger_velocity == 7.0:
            boost_bonus += 0.25
        if burger_velocity == 12.0:
            boost_bonus += 0.25

    # Update HUD
    points_text = font.render(f"Burger Points: {burger_points}", True, ORANGE)
    score_text = font.render(f"Score: {score}", True, ORANGE)
    eaten_text = font.render(f"Burgers Eaten: {burgers_eaten}", True, ORANGE)
    lives_text = font.render(f"Lives: {player_lives}", True, ORANGE)
    boost_text = font.render(f"Boost:", True, ORANGE)

    # Game Over
    if player_lives == 0:
        player_image = player_image_dead
        pygame.display.update()
        game_over_text = font.render(f"FINAL SCORE: {score}", True, ORANGE)
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        pygame.display.update()
        # pause game
        pygame.mixer.music.stop()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                # continue
                if event.type == pygame.KEYDOWN:
                    time.sleep(1)
                    score = 0
                    burgers_eaten = 0
                    boost_bonus = 1
                    player_lives = PLAYER_STARTING_LIVES
                    boost_level = STARTING_BOOST_LEVEL
                    burger_velocity = STARTING_BURGER_VELOCITY
                    player_image = player_image_left
                    pygame.mixer.music.play()
                    is_paused = False
                # quit
                if event.type == pygame.QUIT:
                    running = False
                    is_paused = False


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
    
    if boost_level < 50:
        pygame.draw.rect(display_surface, BOOST_LOW_COLOR, pygame.Rect(WINDOW_WIDTH-70, 60 ,boost_level//1.5,10))
    if boost_level >= 50 and boost_level < STARTING_BOOST_LEVEL:
        pygame.draw.rect(display_surface, BOOST_MEDIUM_COLOR, pygame.Rect(WINDOW_WIDTH-70, 60 ,boost_level//1.5,10))
    if boost_level == STARTING_BOOST_LEVEL:
        pygame.draw.rect(display_surface, BOOST_FULL_COLOR, pygame.Rect(WINDOW_WIDTH-70, 60 ,boost_level//1.5,10))

    # Blit Assets
    display_surface.blit(player_image, player_rect)
    display_surface.blit(burger_image, burger_rect)

    # Update screen and tick clock
    print(f"player:{player_velocity} burger:{burger_velocity} boost: {PLAYER_BOOST_VELOCITY * boost_bonus}")
    pygame.display.update()
    clock.tick(FPS)


pygame.quit()