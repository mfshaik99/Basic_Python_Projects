import pygame
import random
import sys

# Start the game
pygame.init()

# Make the screen
width = 400
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Farru Bird")

# Colors
blue = (135, 206, 235)
green = (0, 200, 0)
yellow = (255, 255, 0)
white = (255, 255, 255)

# Bird
bird_x = 100
bird_y = height // 3  # Start higher
bird_size = 20
bird_speed = 0
gravity = 0.3  # Slower gravity
jump = -7      # Better flap

# Pipes
pipe_width = 60
pipe_gap = 150
pipes = []

def make_pipe():
    top = random.randint(100, 400)
    bottom = height - top - pipe_gap
    top_pipe = pygame.Rect(width, 0, pipe_width, top)
    bottom_pipe = pygame.Rect(width, height - bottom, pipe_width, bottom)
    return top_pipe, bottom_pipe

# Clock and font
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)
score = 0

# 🟡 Wait for SPACE to start
waiting = True
while waiting:
    screen.fill(blue)
    msg = font.render("Press SPACE to Start", True, white)
    screen.blit(msg, (50, height // 2))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            waiting = False

# 🔁 Game loop
running = True
frame = 0
while running:
    screen.fill(blue)

    # Check keys and quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_speed = jump

    # Move bird
    bird_speed += gravity
    bird_y += bird_speed
    bird = pygame.Rect(bird_x, bird_y, bird_size, bird_size)

    # Make new pipes
    if frame % 90 == 0:
        pipes.extend(make_pipe())

    # Move pipes
    for pipe in pipes:
        pipe.x -= 3

    # Remove pipes off screen
    pipes = [pipe for pipe in pipes if pipe.x + pipe.width > 0]

    # Check for crash
    for pipe in pipes:
        if bird.colliderect(pipe):
            running = False

    if bird_y > height or bird_y < 0:
        running = False

    # Draw pipes
    for pipe in pipes:
        pygame.draw.rect(screen, green, pipe)

    # Draw bird
    pygame.draw.rect(screen, yellow, bird)

    # Score
    score_text = font.render(f"Score: {int(score)}", True, white)
    screen.blit(score_text, (10, 10))

    for pipe in pipes:
        if pipe.x + pipe_width == bird_x:
            score += 0.5

    pygame.display.update()
    clock.tick(60)
    frame += 1

pygame.quit()
sys.exit()
 
