"""
Instructor: Bro. Parrish
Class: CSE210
Semester: Spring 2022
Team: Methuselah
Assignment: Final Project
Student: Michael Coleman
"""

# Import section
from game.casting.actor import Actor
from game.shared.point import Point

class Vehicle(Actor):
    """A visable vehicle on the screen
    
    Keeps track of image, size, position and velocity"""

    def __init__(self):
        """constructs a new vehicle object"""
        self._size = 24
        self._sprite = [Point(0, 0), Point(0, 0)]
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)
        self._scale = .75
        self._rotate = 180.0
        self._modifier = 3.0
        self._rotation_point = (75, 25)
        self._moving_right = False;

    # getters
    def get_size(self):
        """returns the color for the vehicle"""
        return self._size

    def get_position(self):
        """returns the position of the vehicle"""
        return self._position
    
    def get_velocity(self):
        """returns the speed and direction of the vehicle"""
        return self._velocity

    def get_rotation(self):
        """Moves frog to its next position according to its velocity.
            
        Args:
        None.

        Returns:
        rotate (float): current rotation of frog sprite in degrees, 0 - 360.
        """
        return self._rotate

    def get_rotation_point(self):
        return self._rotation_point

    def get_scale(self):
        return self._scale

    def get_moving_right(self):
        return self._moving_right
    
    # setters    
    def set_size(self, new_size):
        """sets the size for the object's collisions"""
        self._size = new_size
    
    def set_position(self, position):
        """updates the position of the vehicle - this is the number of spaces it takes up (the frog is one space)"""
        self._position = position

    def set_rotation(self, rotation):
        self._rotate = rotation

    def set_velocity(self, velocity):
        """updates the velocity of the vehicle"""
        self._velocity = velocity
    
    def set_rotation_point(self):
        self._rotation_point = (self.get_sprite()[1].get_x() / 2, 2 * self.get_sprite()[1].get_y() / 3)

    def set_direction(self, direction):
        self._moving_right = direction
    
    # movement
    def move_next(self, max_x, max_y):
        """moves vehicle to its next position based on its velocity"""
        x = (self._position.get_x() + self._velocity.get_x()) % max_x
        y = (self._position.get_y() + self._velocity.get_y()) % max_y
        self._position = Point(x, y)