"""
Instructor: Bro. Parrish
Class: CSE 210
Semester: Spring 2022
Team: Methuselah
Assignment: Week 13 Frogger Game
Student: Michael Coleman
"""
import constants
from game.scripting.action import Action
from game.shared.point import Point
from game.player.frog import Act

from game.directing.play_sound import PlaySound


# add hop sound
sound = PlaySound()

class ControlActorsAction(Action):
    moving = False

    def __init__(self, frog_controller):
        self._frog_controller = frog_controller
        self._direction = Point(0, 0)
        self._counter = 0

    def execute(self, cast, script):
        frog = cast.get_first_actor("frog")

        self._counter += 1
        if self._counter > frog.get_fps() / 3:
            self._counter = 0
            # frog.set_movement(False)
            frog.set_player_action(Act.IDLE)

        # left
        if self._frog_controller.is_key_pressed('left'):
            frog.set_movement(True)
            frog.set_player_action(Act.JUMP)
            self._direction = Point(-constants.CELL_SIZE, 0)
            frog.set_rotation(90)
            sound.play_hop()
        
        # right
        elif self._frog_controller.is_key_pressed('right'):
            frog.set_movement(True)
            frog.set_player_action(Act.JUMP)
            self._direction = Point(constants.CELL_SIZE, 0)
            frog.set_rotation(270)
            sound.play_hop()
        
        # up
        elif self._frog_controller.is_key_pressed('up'):
            frog.set_movement(True)
            frog.set_player_action(Act.JUMP)
            self._direction = Point(0, -constants.CELL_SIZE)
            frog.set_rotation(180)
            sound.play_hop()
        
        # down
        elif self._frog_controller.is_key_pressed('down'):
            frog.set_movement(True)
            frog.set_player_action(Act.JUMP)
            self._direction = Point(0, constants.CELL_SIZE)
            frog.set_rotation(0)
            sound.play_hop()

        # Don't call move on the frog if there is no input - this allows for the frog to be moved by the log's velocity
        else:
            # self._counter += 1
            # if self._counter > frog.get_fps() / 2:
            #     self._counter = 0
                # frog.set_movement(False)
            # frog.set_player_action(Act.IDLE)
            return
    

        frog.set_velocity(self._direction)
        frog.move()

        # sound.play_hop()
        
        self._direction = Point(0,0)
        frog.set_velocity(self._direction)
