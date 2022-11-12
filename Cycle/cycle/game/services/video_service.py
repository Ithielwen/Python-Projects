"""
Instructor: Bro. Parrish
Class: CSE210
Semester: Spring 2022
Team: Methuselah
Assignment: Week 10 Cycle
Student: Joel Jensen
Class: Display
"""
import pyray
import constants
from game.shared.point import Point


class Display:
  """Responsible for the placement of game resources onscreen."""

  def __init__(self, debug = False):
    """Creates a new Display class. 
    
    Args:
      debug (boolean): Turns debug on or off. Displays grid when on.
    """
    self._debug = debug

  
  def close_window(self):
    """Closes game window. Clears game resources.
    
    Args:
      None.
    """
    pyray.close_window()

  
  def clear_buffer(self):
    """Clears game buffer. This refreshes the screen, allowing new resource assets and positions to be loaded into the buffer for next frame.
    
    Args:
      None.
    """
    pyray.begin_drawing()

    pyray.clear_background(pyray.BLACK)

    if self._debug == True:
      self._draw_grid()

    
  def draw_actor(self, actor, place_center = False):
    """Used to place the text icon for the actor on screen.
    
    Args:
      actor (Actor):  Icon displayed onscreen which represents player and npcs.
    """
    icon = actor.get_text()
    x_cord = actor.get_position().get_x()
    y_cord = actor.get_position().get_y()
    font_size = actor.get_font_size()
    color = actor.get_color().to_tuple()

    if place_center:
      icon_width = pyray.measure_text(icon, font_size)

      offset_icon = int(icon_width / 2)

      x_cord -= offset_icon

    pyray.draw_text(icon, x_cord, y_cord, font_size, color)


  def draw_actors(self, actors, place_center = False):
    """Like draw_actor, reads from list of actors and places multiple text icons on screen.
    
    Args:
      actors (list): Actor list from which characters are drawn."""
    for actor in actors:
      self.draw_actor(actor, place_center)

  
  def _get_x_offset(self, icon, font_size):
    """Offset x position to 1/2 icon width.
    
    Args:
      icon: actor text-based icon
      font_size: current size of icon
    """
    icon_width = pyray.measure_text(icon, font_size)

    return int(icon_width / 2)


  def hide_actor(self, actor):
    """
    Places the actor off-screen so they are no longer visible to the player. Can be used after collision or for random placement of actors, storing them when they are unused.

    Attributes:
      actor (Actor): Icon displayed onscreen which represents player and npcs.
    """
    x = -1
    y = -1

    position = Point(x, y)
    actor.set_position(position)


  def flush_buffer(self):
    """Buffer contents is cleared and copied to screen. Always call after screen output contents is drawn to buffer."""
    pyray.end_drawing()


  def is_window_open(self):
    """Check to see if user closed game window.
    
    Returns:
      boolean: True if window is closing, otherwise False.
    """
    return not pyray.window_should_close()

  
  def open_window(self):
    """Creates a new window for game screen."""
    pyray.init_window(constants.MAX_X, constants.MAX_Y, constants.CAPTION)

    pyray.set_target_fps(constants.FRAME_RATE)


  def _draw_grid(self):
    """Adds grid to screen to assist with debugging."""
    for grid_y in range(0, constants.MAX_Y, constants.CELL_SIZE):
      pyray.draw_line(0, grid_y, constants.MAX_X, grid_y, pyray.GRAY)

    for grid_x in range(0, constants.MAX_X, constants.CELL_SIZE):
        pyray.draw_line(grid_x, 0, grid_x, constants.MAX_Y, pyray.GRAY)
    