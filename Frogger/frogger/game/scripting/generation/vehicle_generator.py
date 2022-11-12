"""
Instructor: Bro. Parrish
Class: CSE 210
Semester: Spring 2022
Team: Methuselah
Assignment: Final Project
Student: Michael Coleman
"""
import random
from game.scripting.generation.generator import Generator
from game.casting.vehicle import Vehicle
from game.shared.point import Point

class VehicleGenerator(Generator):
    '''
    This is a generator for the vehicles
    '''
    # Generating Values
    OBJECTS = { 
        "Car": [[Point(0, 1050), Point(140,72)],[Point(150, 1050), Point(140,72)], [Point(300, 1050), Point(140,72)]],
        "Truck": [Point(0,960), Point(185,72)]
        } # This is the number of varieties of vehicles it can generate, as well as the texture coordinates from the spritesheet

    MIN_TIME_BETWEEN = 125
    MAX_TIME_BETWEEN = 200
    CURRENT_TIME_BETWEEN = 0

    # Object variables
    MIN_MOVE_SPEED = 3
    MAX_MOVE_SPEED = 3

    # Initialize the generator's position (should be the beginning or end of one specific row) and set the direction the objects in that row will be moving (0 for left, 1 for right)
    def __init__(self, direction = False, positionX = 0, positionY = 0):
       self._moving_right = direction
       self._positionX = positionX
       self._positionY = positionY
    
    # Override the generate method from the ObjectGenerator class
    def execute(self, cast, script):
        '''
        Randomly generates vehicles in the game. This method overrides the parent ObjectGenerator's method

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        '''
        self._check_generation(cast, script)

    # Check if the random timer has reached 0. If it has, generate a random vehicle. If not, lower the timer by one
    def _check_generation(self, cast, script):
        if self.CURRENT_TIME_BETWEEN <= 0:
            self._reset_timer()
            chosen_object = random.randint(0, len(self.OBJECTS) - 1)
            if chosen_object == 0:
                self._generate_car(cast, script)
            else:
                self._generate_truck(cast, script)
        
        else:
            self.CURRENT_TIME_BETWEEN -= 1

    # Reset the spawning cooldown
    def _reset_timer(self):
        self.CURRENT_TIME_BETWEEN = random.randint(self.MIN_TIME_BETWEEN, self.MAX_TIME_BETWEEN)

    # Generate a car on the row
    def _generate_car(self, cast, script):
        new_car = Vehicle()
        
        # Set the position
        position = Point(self._positionX, self._positionY)
        new_car.set_position(position)

        # Set the velocity
        random_velocity = random.uniform(self.MIN_MOVE_SPEED, self.MAX_MOVE_SPEED)
        random_velocity = random_velocity if self._moving_right else -random_velocity
        velocity = Point(random_velocity, 0)
        new_car.set_velocity(velocity)

        # Set the sprite
        random_car_sprite = random.randint(0, len(self.OBJECTS['Car']) - 1)
        new_car.set_sprite(self.OBJECTS['Car'][random_car_sprite][0], self.OBJECTS['Car'][random_car_sprite][1]) # 0 is the texture coordinates, 1 is the size of the texture
        rotation = 0 if self._moving_right else 180
        new_car.set_rotation(rotation)
        # Set the size
        new_car.set_size(1)
        new_car.set_direction(self._moving_right)

        # Add to cast
        cast.add_actor("vehicles", new_car)

    # Generate a truck on the row
    def _generate_truck(self, cast, script):
        new_truck = Vehicle()
        
        # Set the position
        position = Point(self._positionX, self._positionY)
        new_truck.set_position(position)

        # Set the velocity
        random_velocity = random.uniform(self.MIN_MOVE_SPEED, self.MAX_MOVE_SPEED)
        random_velocity = random_velocity if self._moving_right else -random_velocity
        velocity = Point(random_velocity, 0)
        new_truck.set_velocity(velocity)

        # Set the sprite
        new_truck.set_sprite(self.OBJECTS['Truck'][0], self.OBJECTS['Truck'][1]) # 0 is the texture coordinates, 1 is the size of the texture
        rotation = 0 if self._moving_right else 180
        new_truck.set_rotation(rotation)
        # Set the size
        new_truck.set_size(1)
        new_truck.set_direction(self._moving_right)

        # Add to cast
        cast.add_actor("vehicles", new_truck)

    def get_velocity(self):
        return self.MIN_MOVE_SPEED

    def get_time_between(self):
        return self.MIN_TIME_BETWEEN

    def update_velocities(self, new_velocity):
        self.MIN_MOVE_SPEED *= new_velocity
        self.MAX_MOVE_SPEED *= new_velocity

    def update_time_between(self, new_time_between):
        self.MIN_TIME_BETWEEN -= new_time_between
        self.MAX_TIME_BETWEEN -= new_time_between