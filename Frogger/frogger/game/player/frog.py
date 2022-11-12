"""
Instructor: Bro. Parrish
Class: CSE 210
Semester: Spring 2022
Team: Methuselah
Assignment: Week 14 Frogger Game
Student: Joel Jensen
"""
# Inherited from Actor class

# move(self)

# get_color(self):
# get_font_size(self):
# get_size(self):
# get_position(self):
# get_text(self):
# get_sprite(self):
# get_velocity(self):

# set_color(self, color):
# set_font_size(self, font_size):
# set_size(self, new_size):
# set_position(self, position):
# set_text(self, text):
# set_sprite(self, textureCoordinates, textureSize):
# set_velocity(self, velocity):

import constants
import pyray

from game.casting.actor import Actor
from game.shared.point import Point
# from game.services.frog_controller import KeyInput
# from game.scripting.control_actors_action import ControlActorsAction

# Import enum.Enum class for creating enumerated constant values
from enum import Enum

class Act(Enum):
  IDLE = 0
  JUMP = 1

class Frog:
  """Our intrepid amphibian adventurer."""

  def __init__(self, frog_controller):
    """Create the player frog"""
    self._fc = frog_controller
    self._position = Point(constants.MAX_X / 2, constants.MAX_Y - constants.CELL_SIZE)
    self._velocity = Point(0,0)
    self._sprite = [Point(0, 0), Point(53, 72)]

    # adding for animation
    self._counter = 0
    self._frame = 0
    self._player_action = Act.IDLE
    self._moving = False

    self._fps = 60
    self._framerate = 12
    self._sprite_width = 56
    self._sprite_height = 72
    self._frameset = 4

    self._scale = 1.0
    self._rotate = 180.0
    self._modifier = 3.0
    self._rotation_point = (self._sprite_width / 2, 2 * self._sprite_height / 3)

  def get_counter(self):
    """"""
    return self._counter

  def get_fps(self):
    """"""
    return self._fps

  def get_frame(self):
    """"""
    return self._frame

  def get_framerate(self):
    """"""
    return self._framerate

  def get_frameset(self):
    """"""
    return self._frameset

  def get_movement(self):
    """"""
    return self._moving

  def get_player_action(self):
    """"""
    return self._player_action

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

  def get_modifier(self):
    """Get the value that modifies frog's velocity.
        
    Args:
      None.

    Returns:
      rotate (float): current modifier value.
    """
    return self._modifier

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

  def set_counter(self, num):
    """"""
    self._counter = num

  def set_fps(self, fps):
    """"""
    self._fps = fps

  def set_frame(self, frame):
    """"""
    self._frame = frame

  def set_framerate(self, framerate):
    """"""
    self._framerate = framerate

  def set_frameset(self, frameset):
    """"""
    self._frameset = frameset
    
  def set_movement(self, movement):
    """"""
    self._moving = movement

  def set_player_action(self, action):
    """"""
    self._player_action = action

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

  def set_modifier(self, num):
    """Change the value that modifies frog's velocity.
        
    Args:
      num (float): new modifier vale.
    """
    self._modifier = num

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

  # def draw(self):
  #   # use the key name of _animation_values dict to get its value and set that to animation_values variable as: (frame_count, sprite_size, offset), i.e.: self._animation_values[(Action.IDLE)] = AnimationInfo(1, (56,72), (0,0))        
  #   # animation_values = self._animation_values[(self._player_action)]
  #   w = self._sprite_width
  #   h = self._sprite_height
  #   p = self._position
  #   rp = self._rotation_point
  #   s = self._scale
  #   fps = self._fps
  #   frate = self._framerate
  #   fset = self._frameset
  #   frame_x = 0
  #   frame_y = 0
  #   # frog_frames = rl.Rectangle(frame_x, frame_y, w, h)
  #   # frog_location = rl.Rectangle(p[0], p[1], w * s, h * s)

  #   if self._player_action == Act.JUMP:
  #     self._counter += 1

  #     if self._counter >= fps / frate:
  #         self._counter = 0
  #         self._frame += 1

  #     if self._frame > fset:
  #         self._frame = 0

  #     frame_x = self._frame * w

  #     # rl.draw_texture_tiled(sprite file, frog frames, frog location, origin pivot point, degree rotation, frog scale, color)
  #     #pyray.draw_texture_tiled(self._sprite_page, pyray.Rectangle(frame_x, frame_y, w, h), pyray.Rectangle(p[0], p[1], w * s, h * s), pyray.Vector2(rp[0], rp[1]), self._rotation, self._scale, pyray.ORANGE)

  def move(self):
    """Moves frog to its next position according to its velocity.
        
    Args:
      None.
    """
    # #moving = False
    # self.set_velocity(0, 0)

    # if pyray.is_key_down(pyray.KEY_UP):
    #   moving = True
    #   self.set_velocity(0, 1) -= self._modifier
    #   self._rotation = 180
    # elif pyray.is_key_down(pyray.KEY_RIGHT):
    #   moving = True
    #   velocity[0] += self._modifier
    #   self._rotation = 270
    # elif pyray.is_key_down(pyray.KEY_DOWN):
    #   moving = True
    #   velocity[1] += self._modifier
    #   self._rotation = 0
    # elif pyray.is_key_down(pyray.KEY_LEFT):
    #   moving = True
    #   velocity[0] -= self._modifier
    #   self._rotation = 90
    # else:
    #   moving = False

    # if not self._moving:
    #   # If player is not moving stop jumping animation
    #   if self._player_action == Act.JUMP: 
    #     self._player_action = Act.IDLE
    # else:
    #   # Start jumping animation if player is moving
    #   if self._player_action == Act.IDLE:
    #     self._player_action = Act.JUMP

    # update frog x-position
    x = (self._position.get_x() + self._velocity.get_x()) # % constants.MAX_X

    # update frog y-position
    y = (self._position.get_y() + self._velocity.get_y()) # % constants.MAX_Y

    # prevent frog from moving off left/right side of screen
    if x < constants.CELL_SIZE or x > constants.MAX_X - constants.CELL_SIZE:
      x = (self._position.get_x())

    # prevent from from moving off top/bottom of screen
    if y < constants.CELL_SIZE or y > constants.MAX_Y - constants.CELL_SIZE:
      y = (self._position.get_y())

    self._position = Point(x, y)