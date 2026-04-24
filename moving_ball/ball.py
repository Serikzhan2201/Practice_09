import pygame

class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        # Red ball
        self.color = (255, 0, 0)

    def move(self, dx, dy, screen_width, screen_height):
        new_x = self.x + dx
        new_y = self.y + dy
        
        # Fix boundary checking so the ball never crosses any edge
        # Ignore movement that would place any part of the ball outside the window
        if (new_x - self.radius >= 0 and new_x + self.radius <= screen_width and
            new_y - self.radius >= 0 and new_y + self.radius <= screen_height):
            self.x = new_x
            self.y = new_y

    def draw(self, screen):
        # Use pygame.draw.circle() directly
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
