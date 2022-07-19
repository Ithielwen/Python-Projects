"""
Instructor: Bro. Parrish
Class: CSE 210
Semester: Spring 2022
Team: Methuselah
Assignment: Week 10 Cycle Game
Student: Brennon Jacobson
"""
import random

import constants
from game.casting.actor import Actor
from game.shared.point import Point

class Food(Actor):
    '''
    The object to collect in the game that a snake eats.

    Attributes:
        _points (INT) : The number of points the food is worth
    '''
    def __init__(self, points = 5):
        '''constructs new food'''
        super().__init__()
        self._points = points
        self.set_text("@")
        self.set_color(constants.RED)
        self.reset()

    ##### ACTIONS #####
    def reset(self):
        """Selects a random position and points that the food is worth."""
        self._points = random.randint(1, 8)
        x = random.randint(1, constants.COLUMNS - 1)
        y = random.randint(1, constants.ROWS - 1)
        position = Point(x, y)
        position = position.scale(constants.CELL_SIZE)
        self.set_position(position)
    ##### GETTERS #####
    def get_points(self):
        '''Gets point value'''
        return self._points

    ##### SETTERS #####
    def set_points(self, new_points):
        '''Set new point value of food'''
        self._points = new_points
