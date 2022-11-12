"""
Instructor: Bro. Parrish
Class: CSE 210
Semester: Spring 2022
Team: Methuselah
Assignment: Week 13 Frogger Game
Student: Brennon Jacobson
"""

# Import section
import constants

from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.directing.play_sound import PlaySound

from game.casting.end_zone import EndZone
from game.casting.water import Water

from game.scripting.generation.vehicle_generator import VehicleGenerator
from game.scripting.generation.log_generator import LogGenerator

from game.shared.point import Point

class Director:
    """
    Purpose: Controls the sequence of the game play
    Attributes:
        _video_service: Creates the display
    """
    
    def __init__(self, video_service):
        """
        Constructs a new version of Director
        """
        self._video_service = video_service
        self._is_game_over = False

    def start_game(self, cast, script):
        """
        handles starting the game
        """
        # add music
        sound_effects = PlaySound()
        self._create_level_one(cast, script)
        self._video_service.open_window()
        sound_effects.play_coin_in()
        
        while self._video_service.is_window_open():
            self._execute_actions("input", cast, script)
            self._execute_actions("update", cast, script)
            self._execute_actions("generate", cast, script)
            self._execute_actions("output", cast, script)
        self._video_service.close_window()

    # Creates all of the generators and the end zone for the first level
    def _create_level_one(self, cast, script):
        # Create the vehicle generators
        vehicle_gen_one = VehicleGenerator(positionX=constants.MAX_X, positionY=constants.MAX_Y - (constants.CELL_SIZE * 2))
        vehicle_gen_two = VehicleGenerator(direction = True, positionX=0, positionY=constants.MAX_Y - (constants.CELL_SIZE * 3))

        # Create the log generators
        log_gen_one = LogGenerator(positionX=constants.MAX_X, positionY=constants.CELL_SIZE * 3)
        log_gen_two = LogGenerator(direction=True, positionX=0, positionY=constants.CELL_SIZE * 2)

        # Create the water zone
        water_zone_one = Water()
        water_zone_one.set_position(Point(constants.MAX_X/2, constants.CELL_SIZE * 2))
        water_zone_two = Water()
        water_zone_two.set_position(Point(constants.MAX_X/2, constants.CELL_SIZE * 3))

        # Create the end zone
        end_zone = EndZone()
        end_zone.set_position(Point(constants.MAX_X/2, constants.CELL_SIZE))

        # Add the generators to the script action manage
        script.add_action("generate", vehicle_gen_one)
        script.add_action("generate", vehicle_gen_two)
        script.add_action("generate", log_gen_one)
        script.add_action("generate", log_gen_two)

        # Add the end_zone and the water zones to the cast to handle collisions
        cast.add_zone("end_zone", end_zone)
        cast.add_zone("water", water_zone_one)
        cast.add_zone("water", water_zone_two)

    def _execute_actions(self, group, cast, script):
        """
        handles game till collission happens
        """
        actions = script.get_actions(group)
        for action in actions:
            action.execute(cast, script)

            if isinstance(action, HandleCollisionsAction):
                self._is_game_over = action.get_is_game_over()