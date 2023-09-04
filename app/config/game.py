import numpy as np
import pygame
from app.config.config import *
from app.config.init import screen


class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.ticks = pygame.time.get_ticks()
        self.frames = 0
        # Shared goal position
        self.goalX = np.array(goalX)
        # Overall game data
        self.data = {"screen": screen,
                     "goalX": self.goalX,
                     "vmax": vmax,
                     "gtg_scaling": gtg_scaling,
                     "K_p": K_p,
                     "ao_scaling": ao_scaling}