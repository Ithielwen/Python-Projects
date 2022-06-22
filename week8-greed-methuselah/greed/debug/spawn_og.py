"""
Assignment: Week 8 - Greed Game
Course: CSE210 Programming with Classes
Team: Methuselah
Author: Joel Jensen
Email: jen21092@byui.edu
"""
import pyray
from casting.player import Player
from shared.point import Point
from shared.color import Color

class Spawn(Player):
  """Spawns new player"""
  def __init__(self):
    super().__init__()

  def create_player(self):
    prospector = Player()

    prospector.set_text(self._text)
    prospector.set_font_size(self._font_size)

    color = self._color
    red = int(color[0])
    green = int(color[1])
    blue = int(color[2])
    prospector.set_color(Color(red, green, blue))

    speed = int(1)
    position = self._position
    x_pos = position[0]
    y_pos = position[1]
    prospector.set_position(Point(x_pos, y_pos))
    prospector.set_velocity(Point(0, speed))


  def spawn_player(self):
    """Update player attributes"""
    text = self.get_text()
    position = self.get_position()
    x = position[0]
    y = position[1]
    font_size = self.get_font_size()
    color = self.get_color()
    pyray.draw_text(text, x, y, font_size, color)

  def set_attributes(self, text, font, color, speed, position):
    """Save player attributes"""
    self._text = text
    self._font_size = font
    self._color = color
    self._velocity = speed
    self._position = position