'''
Director/Controller Class
Brennon Jacobson
Greed Game
'''
# added pyray import
import pyray

from services.generation import MineralGeneration
# added spawn player import
from casting.player import Collision
from casting.spawn import Spawn
from casting.cast import Cast

#added constant variables
# PLAYERX = int(pyray.get_screen_width() / 2)
# PLAYERY = int(pyray.get_screen_height() - 45)

# ICON = "@"
# FONTSIZE = 15
# COLOR = (179, 28, 234)
# SPEED = (0, 1)
# POSITION = (PLAYERX, PLAYERY)

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
        mineral_generator = MineralGeneration() # added ()
        
        #added miner
        miner = Spawn()
        # miner.set_attributes(ICON, FONTSIZE, COLOR, SPEED, POSITION)
        # miner.create_player()

        #added collision
        castlist = Cast()
        hazards = Collision(castlist, mineral_generator, miner)

        self._display.init_window()
        while self._display.is_window_open():
            self.move_minerals(mineral_generator)
            #move player // self._move_player()
            self.draw_minerals(mineral_generator)
            #draw player // self.draw_player()

            #added
            self._move_player(miner)
            self.draw_player(miner)
            #added
            hazards.check_collision(castlist, mineral_generator, miner)


    def move_minerals(self, mineral_generator):
        minerals = mineral_generator._get_minerals()
        for mineral in minerals:
            mineral.move_next(self._display._width, self._display._height) # removed get from get_width & get_height

    def draw_minerals(self, mineral_generator):
        self._display.clear()   #added _

        mineral_generator._generate_minerals()
        minerals = mineral_generator._get_minerals()
        self._display.draw_minerals(minerals)    #added _

        self._display.end_drawing()  #added _

    def _get_inputs(self):
        '''get direction input'''
        pass

    def _move_player(self, miner):
        '''move player on screen'''
        #added to _move_player
        y_cord = int(pyray.get_screen_height() - 45)
        x_cord = int(pyray.get_screen_width())
        miner.set_velocity((self._user_input.get_direction(), 0))
        miner.move_next(x_cord, y_cord)

    #added to draw_player
    def draw_player(self, miner):
        self._display.clear()

        
        miner.spawn_player()

        self._display.end_drawing()  #added _
        
    def _do_outputs(self):
        '''draw the player on the screen'''
        pass