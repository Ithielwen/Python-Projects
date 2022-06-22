'''
UserInput Class

Brennon Jacobson
Greed Game
'''
import pyray
# added point import
from shared.point import Point

class UserInput:
    """
    Detects player input. from the keyboard. This in responsible for moving a player horizontally
    """

    # added cell_size
    def __init__(self, cell_size = 1):
        self._cell_size = cell_size

    def get_direction(self):
        """Gets the selected direction based on the currently pressed keys.

        Returns:
            x_direction: The number of spaces to move on the x axis
        """
        x_direction = 0

        if pyray.is_key_down(pyray.KEY_LEFT):
            x_direction = -1
        
        if pyray.is_key_down(pyray.KEY_RIGHT):
            x_direction = 1
            

        # return x_direction
        # Changed direction values
        direction = Point(x_direction, 0)
        direction = direction.scale(self._cell_size)

        return direction