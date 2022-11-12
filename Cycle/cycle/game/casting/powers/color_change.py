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

from game.casting.powers.powerup import PowerUp
from game.shared.point import Point

class ColorChange(PowerUp):
    '''
    A special type of food that changes increases the velocity a snake moves by 2
    '''
    def __init__(self):
        super().__init__()
        self.set_text("%")
        self.set_font_size(15)
        self.set_color(self.new_color())
    
    def use_ability(self, snake):
        '''Use Speed ability to increase speed of a snake'''
        new_color = self.new_color()
        snake.set_body_color(new_color)
        for part in snake.get_snake()[1:]:
            part.set_color(new_color)

    def new_color(self):
        '''Select a random color and set to new random color'''
        colors = [constants.RED, constants.YELLOW, constants.GREEN, constants.ORANGE, constants.PURPLE, constants.BLUE]
        new_color = random.choice(colors)

        return new_color

    def reset(self):
        """Overrides default reset to randomize color"""
        x = random.randint(1, constants.COLUMNS - 1)
        y = random.randint(1, constants.ROWS - 1)
        position = Point(x, y)
        position = position.scale(constants.CELL_SIZE)
        self.set_position(position)
        self.set_color(self.new_color())