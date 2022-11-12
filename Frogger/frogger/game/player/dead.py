"""
Instructor: Bro. Parrish
Class: CSE 210
Semester: Spring 2022
Team: Methuselah
Assignment: Week 14 Frogger Game
Student: Joel Jensen
"""
# Inherited from Actor class
import constants
import pyray

from game.casting.actor import Actor
from game.shared.point import Point

# Import enum.Enum class for creating enumerated constant values
from enum import Enum

class Dead(Actor):
  """Our intrepid amphibian adventurer, has died."""

  def __init__(self):
    """Create the player skull"""
    self._position = Point(-56, -72)
    self._velocity = Point(0,0)
    self._sprite = [Point(302, 322), Point(65, 72)]

    self._sprite_width = 56
    self._sprite_height = 72

    self._scale = 1.0
    self._rotate = 0.0
    self._modifier = 3.0
    self._rotation_point = (self._sprite_width / 2, 2 * self._sprite_height / 3)

  def get_rotation(self):
    """Moves frog to its next position according to its velocity.
        
    Args:
      None.

    Returns:
      rotate (float): current rotation of frog sprite in degrees, 0 - 360.
    """
    return self._rotate

  def get_rotation_point(self):
    return self._rotation_point

  def get_scale(self):
    return self._scale

  def get_sprite_width(self):
    return self._sprite_width

  def get_sprite_height(self):
    return self._sprite_height

  def get_position(self):
    """Get the (x, y) coordinates of the players position.

    Returns:
      Point: Player's (x, y) coordinates.
    """
    return self._position

  def get_velocity(self):
    """Gets two values representing the rate at which the player moves and which direction.
    
    Returns:
      Point: Player rate of speed and direction of traversal.
    """
    return self._velocity

  def get_sprite(self):
      """returns the color for the vehicle"""
      return self._sprite

  def set_rotation(self, degrees):
    """Change direction frog is facing.
        
    Args:
      degrees (float): current rotation of frog sprite in degrees, 0 - 360.
    """
    self._rotate = degrees
    
  def set_sprite_width(self, width):
    self._sprite_width = width

  def set_sprite_height(self, height):
    self._sprite_height = height

  def set_position(self, position):
    """Updates the position of the player.
    
    Args:
      position (Point): Updated player position (x, y) coordinates.
    """
    self._position = position

  def set_velocity(self, velocity):
    """Sets the new velocity of the character.
    
    Args:
      velocity (Point): Updated character speed and direction as (0, 0).
    """
    self._velocity = velocity

  def set_sprite(self, textureCoordinates, textureSize):
      self._sprite = [textureCoordinates, textureSize]