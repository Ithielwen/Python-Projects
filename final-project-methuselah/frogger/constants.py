"""
Instructor: Bro. Parrish
Class: CSE 210
Semester: Spring 2022
Team: Methuselah
Assignment: Final Project
Student: Michael Coleman
"""
import pyray
from game.shared.color import Color

COLUMNS = 40
ROWS = 20
CELL_SIZE = 75
MAX_X = 900
MAX_Y = 600
FRAME_RATE = 60
FONT_SIZE = 15
CAPTION = "Frogger"
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
YELLOW = Color(255, 255, 0)
GREEN = Color(0, 255, 0)
ORANGE = Color(240, 115, 26)
PURPLE = Color(127, 0, 255)
BLUE = Color(0, 64, 255)
STAGE_COLORS = [pyray.GREEN, pyray.BLUE, pyray.PURPLE, pyray.RED]
STAGE_SPEED = 1.15
STAGE_MAX_SPEED = 10.5
STAGE_TIME_BETWEEN = 20
STAGE_MIN_BETWEEN = 75