"""
Instructor: Bro. Parrish
Class: CSE210
Semester: Spring 2022
Team: Methuselah
Assignment: Week 08 Greed Game
Student: Mark Hammer
Class: Mineral
"""
# Import section
from greed.shared.color import Color
from greed.shared.point import Point

class Mineral:
    """A visable character on the screen
    
    Keeps track of color, text character, font size, position and velocity"""

    def __init__(self):
        """constructs a new mineral object"""
        self._color = Color(0, 0, 255)
        self._text = ""
        self._font_size = 24
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)

    # getters
    def get_color(self):
        """returns the color for the mineral"""
        return self._color

    def get_text(self):
        """returns the character that will be used"""
        return self._text

    def get_font_size(self):
        """returns the color for the mineral"""
        return self._font_size

    def get_position(self):
        """returns the position of the mineral"""
        return self._position
    
    def get_velocity(self):
        """returns the speed and direction of the mineral"""
        return self._velocity
    
    # setters
    def set_color(self, color):
        """sets the color for the object"""
        self._color = color
    
    def set_text(self, text):
        """sets the text character for the object"""
        self._text = text
    
    def set_font_size(self, font_size):
        """sets the font_size for the object"""
        self._font_size = font_size
    
    def set_position(self, position):
        """updates the position of the mineral"""
        self._position = position

    def set_velocity(self, velocity):
        """updates the velocity of the mineral"""
        self._velocity = velocity
    
    # movement
    def move_next(self, max_x, max_y):
        """moves mineral to its next position based on its velocity"""
        x = (self._position.get_x() + self._velocity.get_x()) % max_x
        y = (self._position.get_y() + self._velocity.get_y()) % max_y
        self._position = Point(x, y)