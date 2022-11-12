"""
Instructor: Bro. Parrish
Class: CSE210
Semester: Spring 2022
Team: Methuselah
Assignment: Final Project
Student: Brennon Jacobson
"""

import constants
from game.casting.actor import Actor
from game.shared.point import Point


class GameOver(Actor):
    """
    A game over text object positioned in the middle of the screen
    """
    def __init__(self):
        super().__init__()
        self.set_text("GAME OVER")
        self.set_color(constants.RED)
        self.set_font_size(50)
        center = Point(constants.MAX_X/2, constants.MAX_Y/2 -25)
        self.set_position(center)
