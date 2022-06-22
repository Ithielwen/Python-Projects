"""
Assignment: Week 8 - Greed Game
Course: CSE210 Programming with Classes
Team: Methuselah
Author: Joel Jensen
Email: jen21092@byui.edu
"""
import pyray
from greed.player.player import Player

class Spawn(Player):
  """Spawns new player"""
  def __init__(self):
    super().__init__()

  def spawn_player(self):
    """Update player attributes"""
    text = self.get_text()
    x = int(self.get_position().get_x())
    y = int(self.get_position().get_y())
    font_size = self.get_font_size()
    color = self.get_color().to_tuple()
    pyray.draw_text(text, x, y, font_size, color)

  def set_attributes(self, text, font, color, speed, position):
    """Save player attributes"""
    self._text = text
    self._font_size = font
    self._color = color
    self._velocity = speed
    self._position = position
