"""
Instructor: Bro. Parrish
Class: CSE 210
Semester: Spring 2022
Team: Methuselah
Assignment: Week 10 Cycle Game
Student: Emma Hungrige
"""

# Import section
import pyray

import constants
from game.casting.powers.color_change import ColorChange
from game.casting.powers.grow import GROW

from game.casting.cast import Cast
from game.casting.food import Food
from game.casting.score import Score
from game.casting.snake import Snake

from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction

from game.directing.director import Director
from game.directing.play_sound import PlaySound

from game.services.keyboard_service import KeyInput
from game.services.video_service import Display

from game.shared.color import Color
from game.shared.point import Point

def main():

    #Cast creation
    player1 = Snake()
    player2 = Snake(start_y= int(constants.MAX_Y / 4), body_color=constants.PURPLE)
    score1 = Score()
    score2 = Score()

    score2.set_position(Point(constants.MAX_X - 100, 0))

    cast = Cast()
    cast.add_actor("foods", Food())
    cast.add_actor("powers", GROW())
    cast.add_actor("powers", ColorChange())
    cast.add_actor("snakes", player1)
    cast.add_actor("snakes", player2)
    cast.add_actor("scores", score1)
    cast.add_actor("scores", score2)

    # initialize sound devices and play background music
    pyray.init_audio_device()
    music = PlaySound()
    music.play_music()

    #Start the game
    keyboard_service = KeyInput()
    video_service = Display()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))

    director = Director(video_service)
    director.start_game(cast, script)

if __name__ == "__main__":
    main()