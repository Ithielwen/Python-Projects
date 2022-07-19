"""
Instructor: Bro. Parrish
Class: CSE 210
Semester: Spring 2022
Team: Methuselah
Assignment: Week 13 Frogger Game
Student: Mark Hammer and Brennon Jacobson
"""

import pyray

class KeyInput:
  """"""

  def __init__(self):
    """"""
    self._keys = {}

    self._keys["up"] = pyray.KEY_UP
    self._keys["left"] = pyray.KEY_LEFT
    self._keys["down"] = pyray.KEY_DOWN
    self._keys["right"] = pyray.KEY_RIGHT

  def is_key_up(self, key):
    """movement"""
    current_key = self._keys[key.lower()]
    
    return pyray.is_key_up(current_key)

  
  def is_key_down(self, key):
    """"""
    current_key = self._keys[key.lower()]

    return pyray.is_key_down(current_key)


  def is_key_pressed(self, key):
    """"""
    current_key = self._keys[key.lower()]

    return pyray.is_key_pressed(current_key)


  def is_key_released(self, key):
    """"""
    current_key = self._keys[key.lower()]

    return pyray.is_key_released(current_key)