import pygame

# Initialize pygame
pygame.init()

# Create a display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Sound Effects!")

# Load sound effects
sound_1 = pygame.mixer.Sound("Sound_1.wav")
sound_2 = pygame.mixer.Sound("Sound_2.wav")

# Play the sound effects
sound_1.play()
pygame.time.delay(3000)
sound_2.play()
pygame.time.delay(3000)

# Change the volume of a sound effect
sound_2.set_volume(.4)
sound_2.play()

# Load background music
pygame.mixer.music.load("music.wav")

# Play and stop the music
pygame.mixer.music.play(-1,0.0)
pygame.time.delay(7000)
pygame.mixer.music.stop()

# The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# End the game
pygame.quit()