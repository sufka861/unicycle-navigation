import numpy as np
import pygame
from pygame.locals import *
from app.config.config import *

screen = pygame.display.set_mode([screen_width, screen_height], DOUBLEBUF)


class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.ticks = pygame.time.get_ticks()
        self.frames = 0
        # Shared goal position
        self.goalX = np.array(goalX)
        # Create and initialize robots
        self.data = {"screen": screen,
                     "goalX": self.goalX,
                     "vmax": vmax,
                     "gtg_scaling": gtg_scaling,
                     "K_p": K_p,
                     "ao_scaling": ao_scaling}


def init():
    pygame.init()
    pygame.display.set_caption('Unicycle robot')
