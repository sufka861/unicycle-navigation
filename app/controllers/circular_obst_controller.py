import random
from app.config.config import *
from app.entities.circular_obsts import Circular_Obstacle


def create_circular_obsts(num):
    obstacle_list = []
    for i in range(num):
        radius = random.randint(obst_min_radius, obst_max_radius)
        circ_x = random.randint(radius, screen_width - radius)
        circ_y = random.randint(radius, screen_height - radius)
        circle_obst = Circular_Obstacle(radius, circ_x, circ_y)
        obstacle_list.append(circle_obst)
    return obstacle_list
