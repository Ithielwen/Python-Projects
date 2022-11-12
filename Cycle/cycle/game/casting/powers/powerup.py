"""
Instructor: Bro. Parrish
Class: CSE 210
Semester: Spring 2022
Team: Methuselah
Assignment: Week 10 Cycle Game
Student: Brennon Jacobson
"""
import constants
import random
from game.casting.food import Food
from game.shared.point import Point

class PowerUp(Food):
    '''
    A special instance of food that provides a special ability
    '''
    def __init__(self, points=50):
        super().__init__(points)
        self.set_text("$")
        self.set_color(constants.ORANGE)
        self.reset()
    
    def reset(self):
        """Overrides default reset to not adjust points"""
        x = random.randint(1, constants.COLUMNS - 1)
        y = random.randint(1, constants.ROWS - 1)
        position = Point(x, y)
        position = position.scale(constants.CELL_SIZE)
        self.set_position(position)

    def use_ability(self, snake):
        '''
        method to use ability. designed to be overriden by other power ups
        '''
        pass