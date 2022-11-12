"""
Instructor: Bro. Parrish
Class: CSE210
Semester: Spring 2022
Team: Methuselah
Assignment: Final Project
Student: Michael Coleman
"""

# Import section
from game.shared.point import Point

class EndZone:
    """The end zone on the screen
    
    Keeps track of size and position"""

    def __init__(self):
        """constructs a new vehicle object"""
        self._size = 24
        self._position = Point(0, 0)

    # getters
    def get_size(self):
        """returns the size of the zone"""
        return self._size

    def get_position(self):
        """returns the position of the zone"""
        return self._position
        
    # setters    
    def set_size(self, new_size):
        """sets the size for the zone's collisions"""
        self._size = new_size
    
    def set_position(self, position):
        """updates the position of the zone"""
        self._position = position
    