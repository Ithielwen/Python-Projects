"""
Instructor: Bro. Parrish
Class: CSE 210
Semester: Spring 2022
Team: Methuselah
Assignment: Week 10 Cycle Game
Student: Brennon Jacobson
"""

import constants

from game.casting.powers.powerup import PowerUp
from game.shared.point import Point

class GROW(PowerUp):
    '''
    A special type of food that changes increases the velocity a snake moves by 2
    '''
    def __init__(self):
        super().__init__()
        self.set_text("+")
        self.set_font_size(20)
        self.set_color(constants.ORANGE)
    
    def use_ability(self, snake):
        '''Use Speed ability to increase speed of a snake'''
        for part in snake.get_snake():
            curr_size = part.get_font_size()
            big = curr_size + 10
            part.set_font_size(big)

    