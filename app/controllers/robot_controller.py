import random
from app.config.config import *
from app.entities.robot import *


def create_robots(num_robots, data):
    robot_list = []
    for _ in range(num_robots):
        robot_x = random.randint(0, screen_width)
        robot_y = random.randint(0, screen_height)
        robot_phi = random.uniform(0, 2 * np.pi)
        robot_l = 15
        robot_b = 6
        robot_list.append(Robot(robot_x, robot_y, robot_phi, robot_l, robot_b, data))
    return robot_list


def close_obst_count(bot, num_circ_obsts, obstacle_list):
    close_obst = []
    dist = []
    for i in range(num_circ_obsts):
        distance = math.sqrt((obstacle_list[i].circ_x - bot.x) ** 2 + (obstacle_list[i].circ_y - bot.y) ** 2)
        if distance <= (skirt_r + obstacle_list[i].radius):
            close_obst.append([obstacle_list[i].circ_x, obstacle_list[i].circ_y, obstacle_list[i].radius])
            dist.append(distance)
    return close_obst, dist


def min_distance_from_other_robot(bot, robot_list):
    # Avoid other robots
    min_distance = float('inf')  # Initialize to positive infinity
    if len(robot_list) <= 1:
        return min_distance, bot
    for other_robot in robot_list:
        if other_robot is not bot:  # Avoid checking against itself
            distance = math.sqrt((other_robot.x - bot.x) ** 2 + (other_robot.y - bot.y) ** 2)
            if distance < min_distance:
                min_distance = distance
                other_robotX = [other_robot.x, other_robot.y]
    return min_distance, other_robotX


def calculate_movement(bot, robot_list, obstacle_list):
    # Go to gaol while avoiding obstacles
    [close_obst, dist] = close_obst_count(bot, num_circ_obsts, obstacle_list)
    if len(close_obst) == 0:  # No obstacle in sensor skirt
        [v, omega] = bot.go_to_goal()  # Output from controller go_to_goal()
    else:
        closest_obj = dist.index(min(dist))  # Index of the closest object
        obstX = np.array([obstacle_list[closest_obj].circ_x, obstacle_list[closest_obj].circ_y])
        [v, omega] = bot.avoid(obstX)

    # Avoid other robots
    [min_distance, other_robotX] = min_distance_from_other_robot(bot,robot_list)
    if min_distance < skirt_r * 2:  # If another robot within radius, use avoid with the position of the other robot
        [v, omega] = bot.avoid(other_robotX)
    return [v, omega]
