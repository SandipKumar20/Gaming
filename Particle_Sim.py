import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BACKGROUND_COLOR = (0, 100, 0) # Dark Green
PARTICLE_COLOR = (255, 211, 67) # Yellow
PARTICLE_RADIUS = 5
NUM_PARTICLES = 100

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Particle Simulation")

# Create a list to store particles
particles = []

# Create particles with random positions and velocities
for _ in range(NUM_PARTICLES):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    vx = random.uniform(-1, 1)
    vy = random.uniform(-1, 1)
    particles.append([x, y, vx, vy])

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Update and draw particles
    for i, particle in enumerate(particles):
        x, y, vx, vy = particle

        # Update particle position
        x += vx
        y += vy

        # Bounce off the screen edges
        if x < 0 or x > WIDTH:
            vx = -vx
        if y < 0 or y > HEIGHT:
            vy = -vy

        # Store updated values
        particles[i] = [x, y, vx, vy]

        # Draw the particle
        pygame.draw.circle(screen, PARTICLE_COLOR, (int(x), int(y)), PARTICLE_RADIUS)

    pygame.display.flip()
    clock.tick(FPS)
