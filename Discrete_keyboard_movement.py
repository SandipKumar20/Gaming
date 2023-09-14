import pygame

# Initializing Pygame
pygame.init()

# Create the display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('Discrete Keyboard Movement!!')

# Set game values
VELOCITY = 10

# Load in images
cat_image = pygame.image.load("Orange_Cat_128.png")
cat_rect = cat_image.get_rect()
cat_rect.centerx = WINDOW_WIDTH//2
cat_rect.bottom = WINDOW_HEIGHT


# The main game loop
running = True
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
        
        # Check for discrete movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                cat_rect.x -= VELOCITY
            if event.key == pygame.K_RIGHT:
                cat_rect.x += VELOCITY
            if event.key == pygame.K_UP:
                cat_rect.y -= VELOCITY
            if event.key == pygame.K_DOWN:
                cat_rect.y += VELOCITY

    

    # Fill the display surface to cover old images
    display_surface.fill((0,0,0))
        

    # Blitting images onto the gaming screen
    display_surface.blit(cat_image,cat_rect)

    # Update the display
    pygame.display.update()

# End the game
pygame.quit()

