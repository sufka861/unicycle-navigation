# Unicycle-Navigation V2 - Multiple Robots

This is a complimentary README to the original README file. It will go over the changes that were made according to the task at hand:
1. Support multiple independent robots each one moving towards the goal.
2. Each robot should start at a random location.
3. The number of obstacles should be up to 3.
4. Extra: The robots should avoid colliding with each other.

## Multiple robot support
The initial implementation regarded a single robot, and all calculations were directly performed on specified variables that held the robots data.
In Order to support multiple robots, the `robot_list = create_robots(num_robots, game.data)` 
performed the creation of robots by the amount specified in the argument `num_robots = 3` inside `app.config.config.py`.
From this point forward, the same logic was maintained as before, but now every time there is a reference or an operation on the robot `bot` - 
it is done through the loop over each `bot` in `robot_list`.
Moreover, the manipulation of data is done per each bot individually rather than using the previous `robot_X`, 
now each robot maintains its own data as can accessed through `bot.x`.
For this reason, the `update_position(self, v, omega)` was added to the `Robot` class in order to maintain its values.

## Random start location
Inside the `app.controllers.robot_controller.py` the function `create_robots(num_robots, data)` loops over and creates the robots. 
Each iteration a new `Robot` is declared with random x/y/phi variables.
```
robot_x = random.randint(0, screen_width)
robot_y = random.randint(0, screen_height)
robot_phi = random.uniform(0, 2 * np.pi)
```
The x/y coordinates are generated using the `random.randint(self, a:int, b:int)` in order to output a random int inside the screen.  
The phi degree is generated using the `random.uniform(self, a:float, b:float)` between the range of 0 - 360 (0 - 2π).

## Up to 3 obstacles
The number of obstacles is configured in the `app.config.config.py` file as `num_circ_obsts = 3`.

## Robots should avoid colliding with each other
The logic of the robots movement is performed in the function `calculate_movement(bot, robot_list, circ_x, circ_y, radius)` inside the `app.controllers.robot_controller.py`.
The robot first checks if it is near any obstacles in its radius `skirt_r` in the function `close_obst_count(bot, num_circ_obsts, circ_x, circ_y, radius)`.
If there aren't any, the robot generates its `v, omega` from `go_to_goal()`.
If there is an obstacle close by, the values will be generated from `avoid(self, obstX)`.
Last, the robot will calculate its distance from other robots. If another robots radius is within its own radius, the robot will use the 
same `avoid(self, obstX)` but now with the other robot as `obstX` and calculate the same 'paranoid' `v, omega`.
