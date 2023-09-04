from app.config.config import *
import pygame
from pygame.locals import *

screen = pygame.display.set_mode([screen_width, screen_height], DOUBLEBUF)


def init():
    pygame.init()
    pygame.display.set_caption('Unicycle robot')
