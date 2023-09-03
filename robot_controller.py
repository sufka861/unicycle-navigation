import random
from config import *
from robot import *


def create_robots(num_robots, data):
    robot_list = []
    for _ in range(num_robots):
        robot_x = random.randint(50, screen_width - 50)
        robot_y = random.randint(50, screen_height - 50)
        robot_phi = random.uniform(0, 2 * np.pi)
        robot_l = 15
        robot_b = 6
        robot_list.append(Robot(robot_x, robot_y, robot_phi, robot_l, robot_b, data))
    return robot_list

def calculate_movment(bot, robot_list, circ_x, circ_y, radius):
    close_obst = []
    dist = []
    for i in range(num_circ_obsts):
        distance = math.sqrt((circ_x[i] - bot.x) ** 2 + (circ_y[i] - bot.y) ** 2)
        if distance <= (skirt_r + radius[i]):
            close_obst.append([circ_x[i], circ_y[i], radius[i]])
            dist.append(distance)
    if len(close_obst) == 0:  # No obstacle in sensor skirt
        [v, omega] = bot.go_to_goal()  # Output from controller go_to_goal()
    else:
        closest_obj = dist.index(min(dist))  # Index of the closest object
        obstX = np.array([circ_x[closest_obj], circ_y[closest_obj]])
        [v, omega] = bot.avoid_obst(obstX)

    # Add avoidance of other robots here
    min_distance = float('inf')  # Initialize to positive infinity
    for other_robot in robot_list:
        if other_robot is not bot:  # Avoid checking against itself
            distance = np.linalg.norm([bot.x - other_robot.x, bot.y - other_robot.y])
            if distance < min_distance:
                min_distance = distance
                other_robotX = [other_robot.x, other_robot.y]
    if min_distance < skirt_r:  # If too close to another robot, use avoid_obst with the position of the other robot
        [v, omega] = bot.avoid_obst(other_robotX)
    return[v, omega]
