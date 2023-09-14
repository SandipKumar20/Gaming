import pygame

# Initializing Pygame
pygame.init()

# Create a display surface and set its caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Drawing Objects")

# Define colors as RGB Tuples
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255) 
MAGENTA = (255, 0, 255)

# Give a background color to the display
display_surface.fill(GREEN)


# Draw disparate geometric shapes on our display surface
# Line(surface, color, starting point, ending point, thickness)
pygame.draw.line(display_surface, BLACK, (0,0), (80,80), 7)
pygame.draw.line(display_surface, RED, (90,100),(250,250),2)

# Circle(surface, color, center, radius, thickness)
pygame.draw.circle(display_surface, BLUE, (WINDOW_WIDTH//2,WINDOW_HEIGHT//2),100,6)
pygame.draw.circle(display_surface, CYAN, (100,200), 50, 0)

# Rectangle(surface, color, (top-left x, top-left y, width, height))
pygame.draw.rect(display_surface, YELLOW, (400,300,100,200))

# Open Rectangle
pygame.draw.rect(display_surface, WHITE , (200,400,50,50),4)

# Ellipse(surface, color, rect, width=0)
pygame.draw.ellipse(display_surface, BLUE, (300,400, 60, 50))

# Triangle using polygon(surface, color, points, width=0)
pygame.draw.polygon(display_surface, RED, [[200,100],[130,200],[300,220]],6)


# The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Update the display
    pygame.display.update()

# Ending the game
pygame.quit()