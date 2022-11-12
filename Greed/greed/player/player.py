import raylib

from greed.shared.color import Color
from greed.shared.point import Point

class Player:
  """Representation of the player, which can be moved in different directions on a 2D plane.
  
  Attributes:
    _text (str): The text character that represents the player.
    _font_size (int): Sets the size of the player.
    _color (Color): Color of the player's text-based icon.
    _position (Point): Coordinates of player location.
    _velocity (Point): Player's speed and direction.
  """
  def __init__(self):
    """Attributes of the new player."""
    self._text = "?"
    self._font_size = 15
    self._color = Color(28, 217, 234)
    self._position = Point(360, 555)
    self._velocity = Point(0, 0)
    self._score = 0

  def get_color(self):
    """Uses a tuple of int values to store player's color (r, g, b)
    
    Returns:
      Color: Player's rgb color
    """
    return self._color

  def get_font_size(self):
    """Get the font size of the player.
    
    Returns:
      Point: Player's font size
    """
    return self._font_size

  def get_position(self):
    """Get the (x, y) coordinates of the players position.

    Returns:
      Point: Player's (x, y) coordinates.
    """
    return self._position

  def get_text(self):
    """Get the text icon that represents the player onscreen.
    
    Returns:
      string: The text icon of the player.
    """
    return self._text

  def get_velocity(self):
    """Gets two values representing the rate at which the player moves and which direction.
    
    Returns:
      Point: Player rate of speed and direction of traversal.
    """
    return self._velocity

  def move_next(self, max_x, max_y):
    """Updates player movement based on velocity.
    
    Args:
      max_x (int): The maximum x value.
      max_y (int): The maximum y value.
    """
    x = (self._position.get_x() + self._velocity.get_x()) % max_x
    y = (self._position.get_y() + self._velocity.get_y()) % max_y
    self._position = Point(x, y)

  def set_color(self, color):
    """Can be used to change text color.
    
    Args:
      color (Color): Updated color (r, g, b).
    """
    self._color = color

  def set_position(self, position):
    """Updates the position of the player.
    
    Args:
      position (Point): Updated player position (x, y) coordinates.
    """
    self._position = position
  
  def set_font_size(self, font_size):
    """Updates the font size of the text representation.
    
    Args:
      font_size (int): Updated font size.
    """
    self._font_size = font_size
  
  def set_text(self, text):
    """Updates the text icon used to represent the character.
    
    Args:
      text (string): Updated text value.
    """
    self._text = text

  def set_velocity(self, velocity):
    """Sets the new velocity of the character.
    
    Args:
      velocity (Point): Updated character speed and direction as (0, 0).
    """
    self._velocity = velocity

  def update_score(self, add_points):
    '''
      Updates the player score. To subtract points add a negative number
    '''
    self._score += add_points

  def get_score(self):
    return self._score