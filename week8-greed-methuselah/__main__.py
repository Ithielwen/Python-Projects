"""
Instructor: Bro. Parrish
Class: CSE210
Semester: Spring 2022
Team: Methuselah
Assignment: Week 08 Greed Game
Student: Emma Hungrige
"""

#Imports
from lzma import CHECK_UNKNOWN
import pyray

from greed.directing.director import Director

from greed.services.display import Display
from greed.services.user_input import UserInput
from greed.services.music import PlaySound

from greed.shared.color import Color

FRAME_RATE = 60
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
WHITE = Color(255, 255, 255)

def main():
    game_input = UserInput()
    game_display = Display(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)

    controller = Director(game_input, game_display)

    # initialize sound device and play background music
    pyray.init_audio_device()
    music = PlaySound()
    music.play_music()

    controller.start_game()

if __name__ == "__main__":
    main()
