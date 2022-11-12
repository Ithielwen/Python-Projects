"""
Assignment: Week 8 - Greed Game
Course: CSE210 Programming with Classes
Team: Methuselah
Author: Joel Jensen
Email: jen21092@byui.edu
"""

from typing import Any
import pyray

from shared.point import Point
from shared.color import Color

PLAYERX = int(pyray.get_screen_width() / 2)
PLAYERY = int(pyray.get_screen_height() - 45)

ICON = "@"
FONTSIZE = 15
COLOR = (28, 217, 234)
VELOCITY = (1, 0)
POSITION = (360, 555)


class Player:
    """Stores player attributes

    Attributes:
        _text (string): Player icon as string.
        _font_size (int): Player size.
        _color (tuple): Player color.
        _position (tuple): Player spawn location.
        _velocity (tuple): The speed and direction.
    """

    def __init__(self):
        """Constructs a new Player."""
        self._text = ICON
        self._font_size = FONTSIZE
        self._color = COLOR
        self._position = POSITION
        self._velocity = VELOCITY

    def get_color(self):
        """Gets the player's color as a tuple of three ints (r, g, b).
        
        Returns:
            Color: The player's text color.
        """
        return self._color

    def get_font_size(self):
        """Gets the player's font size.
        
        Returns:
            Point: The player's font size.
        """
        return self._font_size

    def get_position(self):
        """Gets the player's position in 2d space.
        
        Returns:
            Point: The player's position in 2d space.
        """
        return self._position
    
    def get_text(self):
        """Gets the player's textual representation.
        
        Returns:
            string: The player's textual representation.
        """
        return self._text

    def get_velocity(self):
        """Gets the player's speed and direction.
        
        Returns:
            Point: The player's speed and direction.
        """
        return self._velocity
    
    def move_next(self, max_x, max_y):
        """Moves the player to its next position according to its velocity. Will wrap the position 
        from one side of the screen to the other when it reaches the given maximum x and y values.
        
        Args:
            max_x (int): The maximum x value.
            max_y (int): The maximum y value.
        """
        if max_x > 0:
          x = (self._position[0] + self._velocity[0]) % max_x
          # y = (self._position[1] + self._velocity[1]) % max_y
          self._position = (x, max_y)

    def set_color(self, color):
        """Updates player's color.
        
        Args:
            color (Color): Updated color.
        """
        self._color = color

    def set_position(self, position):
        """Updates the player's positon.
        
        Args:
            position (Point): Updated position.
        """
        self._position = position
    
    def set_font_size(self, font_size):
        """Updates the player's font size.
        
        Args:
            font_size (int): Updated font size.
        """
        self._font_size = font_size
    
    def set_text(self, text):
        """Updates the player's appearance.
        
        Args:
            text (string): Player's icon.
        """
        self._text = text

    def set_velocity(self, velocity):
        """Updates the velocity to the given one.
        
        Args:
            velocity (Point): The given velocity.
        """
        self._velocity = velocity


class Score(Player):
  """Class keeps track of Score"""
  def __init__(self):
    self._total = 0
    # self._message = ""

  def get_total(self):
    """Gets the current total score.
    
    Returns:
      int: value of current score
    """
    return self._total

  def set_total(self, total):
    """Udates the total score.
    
    Returns:
      int: total (int): Current total score.
    """
    self._total = total

  # def get_message(self):
  #   """Get message.
    
  #   Returns:
  #       string: The message.
  #   """
  #   return self._message
    
  # def set_message(self, message):
  #   """Update message.
    
  #   Args:
  #       message (string): The given message.
  #   """
  #   self._message = message


class Collision:
  # for all gems & rocks
  # if collision
  # delete gem/rock
  # add value to total
  # update score banner
  # def __init__(self, cast, gems, rocks, player):
  def __init__(self, cast, generator, player):
    self._cast = cast
    self._generator = generator
    # self._gem = gems
    # self._rock = rocks
    self._spawn = player
    self._message = ""
    self._score = 0

  # def check_collision(self, cast, gems, rocks, player):
  def check_collision(self, cast, generator, player):
    quarry = generator._get_minerals()
    # loc = Point(player.get_position(), 555)
    # loc = Point(360, 555)
    loc = player.get_position()
    # create player bounding box
    # loc_start_x = loc.get_x()
    # loc_start_y = loc.get_y()
    # loc_point = loc.add(Point(int(loc[0]) + 15, int(loc[1]) + 30))
    # loc_end_x = loc_point.get_x()
    # loc_end_y = loc_point.get_y()
    loc_start_x = str(player.get_position()[0])
    loc_start_y = str(player.get_position()[1])
    loc_boxend = Point(player.get_position()[0], player.get_position()[1]).boxend(15, 30)
    # loc_factor = loc.scale(2)
    loc_end_x = str(loc_boxend.get_x())
    loc_end_y = str(loc_boxend.get_y())

    loc_x = str(player.get_position()[0])
    # rx = cast.get_first_mineral(generator)
    rx = generator._get_minerals()[0].get_position().get_x()
    rx = str(rx)
    ry = generator._get_minerals()[0].get_position().get_y()
    ry = str(ry)
    points = self._score
    # for stone in quarry:
    for i in range(len(quarry)):
      stone = quarry[i]

      #create stone bounding box
      stone_start_x = stone.get_position().get_x()
      stone_start_y = stone.get_position().get_y()
      stone_boxend = stone.get_position().boxend(15, 30)
      stone_end_x = stone_boxend.get_x()
      stone_end_y = stone_boxend.get_y()

      # if loc.equals(Point(200, 555)):
      # if loc.equals(stone.get_position()):
      
      # if pyray.check_collision_lines([loc_start_x, loc_start_y], [loc_end_x, loc_end_y], [stone_start_x, stone_start_y], [stone_end_x, stone_end_y], Any):
        # points += 1
        # rx = stone.get_position()
        # rx = str(rx[0])
        # cast.remove_mineral(tuple(quarry), stone)
        # cast.remove_mineral(generator, stone)

    
    self.draw_message(str(stone_end_y), rx, ry, str(points))

  def draw_message(self, msg, rx, ry, points):
    pyray.draw_text("Player x:", 10, 575, 24, (255, 255, 255))
    pyray.draw_text(msg, 125, 575, 24, (255, 255, 255))
    pyray.draw_text("1st Rock (x, y):", 200, 575, 24, (255, 255, 255))
    pyray.draw_text(rx, 390, 575, 24, (255, 255, 255))
    pyray.draw_text(ry, 440, 575, 24, (255, 255, 255))
    pyray.draw_text("Score:", 540, 575, 24, (255, 255, 255))
    pyray.draw_text(points, 640, 575, 24, (255, 255, 255))
    # pyray.draw_text(ry, 125, 575, 24, (255, 255, 255))
