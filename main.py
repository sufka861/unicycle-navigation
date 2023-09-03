from pygame.locals import *
from robot import *
from circular_obsts import *
from config import *

screen = pygame.display.set_mode([screen_width, screen_height], DOUBLEBUF)

def main():
    # PyGame inits
    pygame.init()
    pygame.display.set_caption('Unicycle robot')
    clock = pygame.time.Clock()
    ticks = pygame.time.get_ticks()
    frames = 0

    # Robot configuration
    robot_list = []

    # Shared goal position
    goalX = np.array([600, 400])

    # Create and initialize robots
    data = {"screen": screen, "goalX": goalX, "vmax": 0.5, "gtg_scaling": 0.0001, "K_p": 0.01, "ao_scaling": 0.00005}

    for _ in range(num_robots):
        robot_x = random.randint(50, screen_width - 50)
        robot_y = random.randint(50, screen_height - 50)
        # robot_phi = random.uniform(0, 2 * np.pi)
        robot_phi = 0
        robot_l = 15
        robot_b = 6
        robot_list.append(robot(robot_x, robot_y, robot_phi, robot_l, robot_b, data))

    # Shared goal position
    goalX = np.array([600, 400])

    # Create obstacles
    [radius, circ_x, circ_y] = create_circular_obsts(num_circ_obsts)

    # PyGame loop
    while True:
        # To exit
        event = pygame.event.poll()
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            break
        screen.fill((50, 55, 60))  # background

        # Draw robots, sensor skirts, obstacles, and goal
        for bot in robot_list:
            bot = robot(bot.x, bot.y, bot.phi, bot.l, bot.b, data)
            pygame.draw.circle(screen, (100, 100, 100), (int(bot.x), int(bot.y)), skirt_r, 0)  # Draw sensor skirt
            bot.show()  # Draw the robot
        draw_circular_obsts(radius, circ_x, circ_y)
        pygame.draw.circle(screen, (0, 255, 0), goalX, 8, 0)  # Draw goal

        # Check if obstacles are in sensor skirts of any robots
        for bot in robot_list:
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

            # Update robot position and orientation as per control input
            bot.update_position(v, omega)


        # FPS. Print if required
        clock.tick(300)  # To limit FPS, controls the speed of the animation
        fps = (frames * 1000) / (pygame.time.get_ticks() - ticks)  # Calculate current FPS

        # Update PyGame display
        pygame.display.flip()
        frames += 1


if __name__ == '__main__':
    main()
