import pygame
import random
from config import *
from main import screen


def create_circular_obsts(num):
    radius = []
    circ_x = []
    circ_y = []
    for i in range(num):
        radius.append(random.randint(obst_min_radius, obst_max_radius))
        circ_x.append(random.randint(radius[i], screen_width - radius[i]))
        circ_y.append(random.randint(radius[i], screen_height - radius[i]))
    return [radius, circ_x, circ_y]


def draw_circular_obsts(radius, circ_x, circ_y):
    for i in range(num_circ_obsts):
        pygame.draw.circle(screen, (0, 0, 255), (circ_x[i], circ_y[i]), radius[i], 0)