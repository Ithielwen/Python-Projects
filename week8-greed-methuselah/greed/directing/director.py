"""
Instructor: Bro. Parrish
Class: CSE210
Semester: Spring 2022
Team: Methuselah
Assignment: Week 08 Greed Game
Student: Brennon Jacobson
Class: Director
"""

from greed.services.generation import MineralGeneration

from greed.player.crew import Roster

from greed.player.spawn import Spawn
from greed.player.banner import Message
from greed.player.collision import Collision

from greed.shared.color import Color
from greed.shared.point import Point

import pyray

class Director:
    """Control the game play
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        input_class (UserInput)
        display_output (Display)
    """

    def __init__(self, input_class, display_output):
        """Constructs a new Director using the specified user_input and display classes.
        
        Args:
            input_class (UserInput)
            display_output (Display)
        """
        self._user_input = input_class
        self._display = display_output
        
    def start_game(self):
        """Start the game"""
        cols = self._display.get_cols()
        rows = self._display.get_rows()
        cell_size = self._display.get_cell_size()

        mineral_generator = MineralGeneration(cols, rows, cell_size)

        # added Miner
        m_icon = "@"
        m_font_sz = 15
        red = int(179)
        green = int(28)
        blue = int(234)
        m_style = Color(red, green, blue)
        # m_position = Point(m_x, m_y)
        m_position = Point(400, 555)
        
        crew_roster = Roster()
        miner = Spawn()
        miner.set_text(m_icon)
        miner.set_font_size(m_font_sz)
        miner.set_color(m_style)
        miner.set_position(m_position)
        crew_roster.add_member("miners", miner)


        # added Scoreboard
        scoreboard = Message()
        # scoreboard.set_text(m_icon)
        # scoreboard.set_font_size(m_font_sz)
        # scoreboard.set_color(m_style)
        # scoreboard.set_position(m_position)
        crew_roster.add_member("scoreboards", scoreboard)

        # added Collision
        #collision = Collision()

        self._display.init_window()
        player1 = crew_roster.get_first_member("miners")

        while self._display.is_window_open():
            self._get_inputs(crew_roster)  

            self.move_minerals(mineral_generator)
            self._move_player(crew_roster)

            self.draw_minerals(mineral_generator)
            self.draw_player(crew_roster)

            half_cell_size = cell_size/2

            #Check for found item and update score
            for mineral in mineral_generator.get_minerals():
                #Check if row at bottom of screen
                mineral_x = mineral.get_position().get_x()
                mineral_y = mineral.get_position().get_y()
                player_x = player1.get_position().get_x()
                player_y = player1.get_position().get_y()

                if ((player_x - half_cell_size < mineral_x < player_x + half_cell_size) and 
                    player_y - half_cell_size < mineral_y < player_y + half_cell_size):

                    player1.update_score(mineral.get_points())
                    
                #delete row
                if (mineral_y > player_y - half_cell_size):
                    mineral_generator.remove_mineral(mineral)

            banner_message = f"Score: {str(player1.get_score())}"
            pyray.draw_text(banner_message, 50, 50, 24, pyray.WHITE)
            self._display.end_drawing()

    def move_minerals(self, mineral_generator):
        minerals = mineral_generator.get_minerals()
        for mineral in minerals:
            mineral.move_next(self._display.get_width(), self._display.get_height())

    def draw_minerals(self, mineral_generator):
        self._display.clear()

        mineral_generator.generate_minerals()
        minerals = mineral_generator.get_minerals()
        self._display.draw_minerals(minerals)

    def _get_inputs(self, crew_roster):
        '''get direction input'''
        miner = crew_roster.get_first_member("miners")
        speed = self._user_input.get_direction()
        miner.set_velocity(speed)

    def _move_player(self, crew_roster):
        '''move player on screen'''
        #added to _move_player
        miner = crew_roster.get_first_member("miners")

        x_cord = self._display.get_width()
        y_cord = self._display.get_height()

        miner.move_next(x_cord, y_cord)

    def draw_player(self, crew_roster):
        self._display.clear()

        miner = crew_roster.get_first_member("miners")
        miner.spawn_player()