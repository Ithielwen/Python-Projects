"""
Instructor: Bro. Parrish
Class: CSE210
Semester: Spring 2022
Team: Methuselah
Assignment: Week 08 Greed Game
Student: Mark Hammer
Class: Gem
"""
# Import section
from greed.casting.mineral import Mineral

class Gem(Mineral):
    """child class to Mineral, sets points and color"""
    
    def __init__(self):
        super().__init__()
        self._points = 1
        # self.color = "" ### don't need this, can inherit from parent

    def get_points(self):
        """returns points"""
        return self._points
    
    def set_points(self, points):
        """sets the new point total"""
        self._points += points
        self.set_text(f"Score: {self._points}")