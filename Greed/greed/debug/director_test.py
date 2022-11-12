# empty for now, just a placeholder, copied from RFK game

'''
Main file

Testing - Brennon
'''
import pyray
from greed.directing.director import Director
from greed.services.user_input import UserInput
from greed.services.display import Display
from greed.casting.mineral import Mineral
from greed.services.music import PlaySound
from pyray import *

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
CELL_SIZE = 15
CAPTION = "GREED"
FRAME_RT = 60
DEBUG = False

game_input = UserInput()
game_display = Display(CAPTION,SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE, FRAME_RT, DEBUG)

controller = Director(game_input, game_display)

# initialize sound device and play background music
pyray.init_audio_device()
music = PlaySound()
music.play_music()

controller.start_game()