"""
Instructor: Bro. Parrish
Class: CSE210
Semester: Spring 2022
Team: Methuselah
Assignment: Week 10 Cycle
Student: Joel Jensen
Class: KeyInput
"""
import pyray

class KeyInput:
  """"""

  def __init__(self):
    """"""
    self._keys = {}

    self._keys["w"] = pyray.KEY_W
    self._keys["a"] = pyray.KEY_A
    self._keys["s"] = pyray.KEY_S
    self._keys["d"] = pyray.KEY_D

    self._keys["q"] = pyray.KEY_Q
    self._keys["e"] = pyray.KEY_E
    self._keys["f"] = pyray.KEY_F

    self._keys["i"] = pyray.KEY_I
    self._keys["j"] = pyray.KEY_J
    self._keys["k"] = pyray.KEY_K
    self._keys["l"] = pyray.KEY_L

    self._keys["o"] = pyray.KEY_O
    self._keys["u"] = pyray.KEY_U
    self._keys["h"] = pyray.KEY_H

    self._keys[" "] = pyray.KEY_SPACE
    self._keys["\b"] = pyray.KEY_BACKSPACE
    self._keys["`"] = pyray.KEY_GRAVE
    self._keys["\r"] = pyray.KEY_ENTER
    self._keys["\t"] = pyray.KEY_TAB

    self._keys["left alt"] = pyray.KEY_LEFT_ALT
    self._keys["right alt"] = pyray.KEY_RIGHT_ALT

    self._keys["left ctrl"] = pyray.KEY_LEFT_CONTROL
    self._keys["right ctrl"] = pyray.KEY_RIGHT_CONTROL
    self._keys["page down"] = pyray.KEY_PAGE_DOWN


  def is_key_up(self, key):
    """"""
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