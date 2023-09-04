from app.config.init import *
from app.entities.circular_obsts import *
from app.controllers.robot_controller import *


def main():
    # PyGame inits
    pygame.init()
    pygame.display.set_caption('Unicycle robot')
    clock = pygame.time.Clock()
    ticks = pygame.time.get_ticks()
    frames = 0

    # Shared goal position
    goalX = np.array([600, 400])

    # Create and initialize robots
    data = {"screen": screen,
            "goalX": goalX,
            "vmax": vmax,
            "gtg_scaling": gtg_scaling,
            "K_p": K_p,
            "ao_scaling": ao_scaling}

    # initialize robot_list
    robot_list = create_robots(num_robots, data)

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
            bot = Robot(bot.x, bot.y, bot.phi, bot.l, bot.b, data)
            pygame.draw.circle(screen, (100, 100, 100), (int(bot.x), int(bot.y)), skirt_r, 0)  # Draw sensor skirt
            bot.show()  # Draw the robot
        draw_circular_obsts(radius, circ_x, circ_y)
        pygame.draw.circle(screen, (0, 255, 0), goalX, 8, 0)  # Draw goal

        # Check if obstacles are in sensor skirts of any robots
        for bot in robot_list:
            [v, omega] = calculate_movement(bot, robot_list, circ_x, circ_y, radius)

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
