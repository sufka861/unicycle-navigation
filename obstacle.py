import pygame


class Obstacle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 255), (self.x, self.y), self.radius, 0)
