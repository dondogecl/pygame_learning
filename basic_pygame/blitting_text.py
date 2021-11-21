import pygame

# initialize PG
pygame.init()

# Create a display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode( (WINDOW_WIDTH, WINDOW_HEIGHT) )
pygame.display.set_caption("Yui Game 1.0")

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

# BACKGROUND COLOR
display_surface.fill(BLACK)

# See all available system fonts
fonts = pygame.font.get_fonts()
[print(font) for font in fonts]
# define fonts
system_font = pygame.font.SysFont('calibri', 64)
custom_font = pygame.font.Font('fonts\AttackGraffiti-3zRBM.ttf', 32)

# Define text fontx.render(string, antialias, colors)
system_text = system_font.render("Dragons rule", True,\
    GREEN, DARKGREEN)
system_text_rect = system_text.get_rect()
system_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

custom_text = custom_font.render("Move the dragon soon!", True,\
    GREEN)
custom_text_rect = custom_text.get_rect()
custom_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2+100)

# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # blit text surfaces to the display surface
    display_surface.blit(system_text, system_text_rect)
    display_surface.blit(custom_text, custom_text_rect)

   
    # update the display
    pygame.display.update()


# End the game
pygame.quit()
