import pygame


class Ball:
    """Red ball that moves with arrow keys."""

    def __init__(self, x, y, radius=25):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = (220, 50, 50)
        self.step = 20  # pixels per key press

    def move(self, direction, screen_width, screen_height):
        """Move ball in given direction, check boundaries."""
        new_x, new_y = self.x, self.y

        if direction == "UP":
            new_y -= self.step
        elif direction == "DOWN":
            new_y += self.step
        elif direction == "LEFT":
            new_x -= self.step
        elif direction == "RIGHT":
            new_x += self.step

        # Boundary check - ignore move if ball goes off screen
        if self.radius <= new_x <= screen_width - self.radius:
            self.x = new_x
        if self.radius <= new_y <= screen_height - self.radius:
            self.y = new_y

    def draw(self, surface):
        """Draw the ball on surface."""
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
        pygame.draw.circle(surface, (180, 30, 30), (self.x, self.y), self.radius, 3)
        # Shine effect
        pygame.draw.circle(surface, (255, 120, 120),
                           (self.x - 8, self.y - 8), 7)
