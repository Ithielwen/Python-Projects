"""
Instructor: Bro. Parrish
Class: CSE 210
Semester: Spring 2022
Team: Methuselah
Assignment: Week 13 Frogger Game
Student: Emma Hungrige
"""

#Import section

import pyray
import constants

from game.casting.cast import Cast
from game.player.frog import Frog
from game.casting.score import Score
from game.player.dead import Dead

from game.directing.director import Director

from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.script import Script
from game.scripting.generation.generator import Generator

from game.services.frog_controller import KeyInput
from game.services.display_controller import Display

from game.shared.point import Point

def main():
    #Set up services
    frog_controls = KeyInput()

    #Cast creation
    cast = Cast()
    frog = Frog(frog_controls)
    score = Score()
    skull = Dead()
    frog.set_position(Point(constants.MAX_X//2, constants.MAX_Y - constants.CELL_SIZE))
    cast.add_actor("frog", frog)
    cast.add_actor("score", score)
    cast.add_actor("skull", skull)

    game_display = Display()

    #Initialize sound devices and play background music
    pyray.init_audio_device()
  
    #Start the game
    script = Script()
    script.add_action("input", ControlActorsAction(frog_controls))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction(game_display))
    script.add_action("generate", Generator())
    script.add_action("output", DrawActorsAction(game_display))

    director = Director(game_display)
    director.start_game(cast, script)

if __name__ == "__main__":
    main()