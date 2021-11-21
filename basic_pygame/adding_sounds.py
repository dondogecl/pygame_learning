import pygame


# initialize PG
pygame.init()

# create a display surface
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Yui adding sounds")

# Load sound effects
sound_1 = pygame.mixer.Sound(r'sounds\2_basic_pygame_sound_1.wav')
sound_2 = pygame.mixer.Sound(r'sounds\2_basic_pygame_sound_2.wav')

# load bgm
pygame.mixer.music.load(r'sounds\2_basic_pygame_music.wav')
# play and stop the music
# (1, 2, 3 times... or infinite -1), starting time
pygame.mixer.music.play(-1, 0.0)

# play sound 
sound_1.play()
pygame.time.delay(2000)
# change volume of a sound
sound_2.set_volume(.1)
sound_2.play()
pygame.time.delay(1000)

# fade out
volume = 1
for second in range(20):
    volume -= 0.1
    pygame.mixer.music.set_volume(volume)
    pygame.time.delay(500)

pygame.mixer.music.stop()


# Main Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False




    
# end pygame
pygame.quit()