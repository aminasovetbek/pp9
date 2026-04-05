"""
Moving Ball Game - Practice 09 Task 3.3
Move the red ball with arrow keys.
Ball cannot leave the screen boundaries.
Press ESC to quit.
"""

import pygame
import sys
from ball import Ball

WIDTH, HEIGHT = 600, 600
WHITE  = (255, 255, 255)
GRAY   = (200, 200, 200)
BLACK  = (0, 0, 0)
RED    = (220, 50, 50)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball Game")
clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 20)

# Create ball in center of screen
ball = Ball(x=WIDTH // 2, y=HEIGHT // 2, radius=25)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_UP:
                ball.move("UP", WIDTH, HEIGHT)
            elif event.key == pygame.K_DOWN:
                ball.move("DOWN", WIDTH, HEIGHT)
            elif event.key == pygame.K_LEFT:
                ball.move("LEFT", WIDTH, HEIGHT)
            elif event.key == pygame.K_RIGHT:
                ball.move("RIGHT", WIDTH, HEIGHT)

    # Draw
    screen.fill(WHITE)

    # Grid lines for visual reference
    for x in range(0, WIDTH, 50):
        pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT), 1)
    for y in range(0, HEIGHT, 50):
        pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y), 1)

    # Ball
    ball.draw(screen)

    # Info text
    info = font.render(f"Position: ({ball.x}, {ball.y})  |  Use Arrow Keys  |  ESC = Quit", True, BLACK)
    screen.blit(info, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
