"""
Instructor: Bro. Parrish
Class: CSE 210
Semester: Spring 2022
Team: Methuselah
Assignment: Week 10 Cycle Game
Student: Brennon Jacobson
"""

from game.casting.actor import Actor

class Score(Actor):
    '''
    Keep track of each players points
    '''
    def __init__(self):
        super().__init__()
        self._points = 0

    def add_points(self, points):
        '''
        Add points

        Args:
            points (int): points to add
        '''
        self._points += points
        self.set_text("Score: " + str(self._points))