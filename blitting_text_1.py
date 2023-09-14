import pygame

# Initialize pygame
pygame.init()

# Create a display surface
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Blitting Text!!!")

# Define colors as RGB Tuples
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0) 
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255) 
MAGENTA = (255, 0, 255)

# Display surface is of color GREEN
display_surface.fill(GREEN)


# See all available system fonts
fonts = pygame.font.get_fonts()
for font in fonts:
    print(font)

# Define fonts
system_font = pygame.font.SysFont('gentium', 64)
custom_font = pygame.font.Font('AttackGraffiti.ttf',32)

# Define text
system_text = system_font.render('Start the game!', True, RED, YELLOW)
system_text_rect = system_text.get_rect()
system_text_rect.center = (WINDOW_WIDTH//2,WINDOW_HEIGHT//2)

custom_text = custom_font.render("Play the game!", True, BLACK, WHITE)
custom_text_rect = custom_text.get_rect()
custom_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 120)

# The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Blit the text surfaces to the display surface
    display_surface.blit(system_text,system_text_rect)
    display_surface.blit(custom_text,custom_text_rect)
    # Update the display
    pygame.display.update()

# End the game
pygame.quit()
