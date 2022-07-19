"""
Instructor: Bro. Parrish
Class: CSE210
Semester: Spring 2022
Team: Methuselah
Assignment: Final Project
Student: Brennon Jacobson
"""

from game.casting.actor import Actor


class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self):
        super().__init__()
        self._points = 0
        self._lives = 3
        self.add_points(0)

    def add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points += points
        self.set_text(f"Score: {self._points}   ||  Lives: {self._lives}")

    def get_points(self):
        return self._points

    def lose_life(self):
        '''Removes one life and updates the text attribute to display new points and lives'''
        self._lives = self._lives - 1
        self.set_text(f"Score: {self._points}   ||  Lives: {self._lives}")

    def get_lives(self):
        '''returns the number of lives left'''
        return self._lives
