'''
Director/Controller Class

Brennon Jacobson
Greed Game
'''

from services.generation import MineralGeneration

# added Roster and Spawn imports
# import pyray
from player.crew import Roster
# from player.player import Player
# from player.spawn import Collision, Spawn, Message
from player.spawn import Spawn
from player.banner import Message
from player.collision import Collision

from shared.color import Color
from shared.point import Point

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
        mineral_generator = MineralGeneration()

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
        collision = Collision()

        self._display.init_window()
        while self._display.is_window_open():
            self.move_minerals(mineral_generator)
            #move player // self._move_player()
            self.draw_minerals(mineral_generator)
            #draw player // self.draw_player()
            self.draw_player(crew_roster)
            self._get_inputs(crew_roster)
            self._move_player(crew_roster)

            # Scoreboard and collision tests
            player1 = crew_roster.get_first_member("miners")
            # scoreboard.check_collision(mineral_generator, player1)
            collision.check_collision(mineral_generator, player1, scoreboard)

    def move_minerals(self, mineral_generator):
        minerals = mineral_generator._get_minerals()
        for mineral in minerals:
            mineral.move_next(self._display._width, self._display._height)

    def draw_minerals(self, mineral_generator):
        self._display.clear()

        mineral_generator._generate_minerals()
        minerals = mineral_generator._get_minerals()
        self._display.draw_minerals(minerals)

        self._display.end_drawing()

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

        self._display.end_drawing()
        
    def _do_outputs(self):
        '''draw the player on the screen'''
        pass