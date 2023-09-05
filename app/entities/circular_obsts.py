import pygame
from app.main import screen


class Circular_Obstacle:
    def __init__(self, radius, circ_x, circ_y):
        self.radius = radius
        self.circ_x = circ_x
        self.circ_y = circ_y

    def draw_circular_obsts(self):
        pygame.draw.circle(screen, (0, 0, 255), (self.circ_x, self.circ_y), self.radius, 0)
