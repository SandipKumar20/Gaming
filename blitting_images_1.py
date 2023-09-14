from tkinter.tix import WINDOW
import pygame

# Initilializing pygame
pygame.init()

# Creating a display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Blitting Images!!!")

# Create Images
dog_image = pygame.image.load("Golden_Retriever_256.png")
dog_rect = dog_image.get_rect()
dog_rect.center = (300,150)

cat_image = pygame.image.load("Orange_Cat_128.png")
cat_rect = cat_image.get_rect()
cat_rect.topleft = (0,0)


# The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Blit a surface object at the given coordinates of our display
    display_surface.blit(dog_image,dog_rect)
    display_surface.blit(cat_image,cat_rect)

    # Update the display
    pygame.display.update()


# End the game
pygame,quit()