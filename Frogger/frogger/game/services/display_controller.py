"""
Instructor: Bro. Parrish
Class: CSE 210
Semester: Spring 2022
Team: Methuselah
Assignment: Week 13 Frogger Game
Student: Mark Hammer and Brennon Jacobson
"""

import pyray
import constants
from game.shared.point import Point
from game.services.draw_background import Background
from game.casting.actor import Actor
from game.player.frog import Act


class Display:
  """Responsible for the placement of game resources onscreen."""

  def __init__(self, debug = False):
    """Creates a new Display class. 
    
    Args:
      debug (boolean): Turns debug on or off. Displays grid when on.
    """
    self._debug = debug
    self._character = []
    self._color = pyray.RAYWHITE
  
  def draw_background(self):
    """Draws the background from the background class. 
    """
    myBackground = Background(self._character)
  
  def set_color(self, new_color):
    self._color = new_color
    
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

  def draw_text(self, actor, place_center = False):
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

    pyray.draw_text(icon, int(x_cord), int(y_cord), int(font_size), color)

  def draw_actor(self, actor, place_center = False):
    """Used to place the text icon for the actor on screen.
    
    Args:
      actor (Actor):  Icon displayed onscreen which represents player and npcs.
    """
    icon = actor.get_sprite()
    x_cord = actor.get_position().get_x()
    y_cord = actor.get_position().get_y()
    width = actor.get_sprite()[1].get_x()
    height = actor.get_sprite()[1].get_y()

    pyray.draw_texture_tiled(
      self._character, 
      pyray.Rectangle(
        actor.get_sprite()[0].get_x(), 
        actor.get_sprite()[0].get_y(), 
        actor.get_sprite()[1].get_x(), 
        actor.get_sprite()[1].get_y()),
      pyray.Rectangle(
        actor.get_position().get_x(), 
        actor.get_position().get_y(), 
        actor.get_sprite()[1].get_x() * actor.get_scale(), 
        actor.get_sprite()[1].get_y() * actor.get_scale()), 
      pyray.Vector2(actor.get_rotation_point()[0], actor.get_rotation_point()[1]), 
      actor.get_rotation(), 
      actor.get_scale(), 
      pyray.RAYWHITE
      )  

  def draw(self, actor, place_center = False):
    """Used to place the text icon for the actor on screen.
    
    Args:
      actor (Actor):  Icon displayed onscreen which represents player and npcs.
    """
    # frog = actor.get_first_actor("frog")
    w = actor.get_sprite_width()
    h = actor.get_sprite_height()
    p = actor.get_position()
    rp = actor.get_rotation_point()
    s = actor.get_scale()
    fps = actor.get_fps()
    frate = actor.get_framerate()
    fset = actor.get_frameset()
    frame_x = 0
    frame_y = 0
    # actor.set_player_action(Act.JUMP)
    # action = actor.get_player_action()
    counter = actor.get_counter()
    frame = actor.get_frame()
    
    if actor.get_player_action() == Act.IDLE:
      pyray.draw_texture_tiled(
        self._character, 
        pyray.Rectangle(
          frame_x, 
          frame_y, 
          w, 
          h),
        pyray.Rectangle(
          p.get_x(), 
          p.get_y(), 
          w * s, 
          h * s), 
        pyray.Vector2(rp[0], rp[1]), 
        actor.get_rotation(), 
        actor.get_scale(), 
        self._color
        )
    # else:
    if actor.get_player_action() == Act.JUMP:
      for _ in range(fset):
        counter += 1
        actor.set_counter(counter)

        if counter >= fps / frate:
          counter = 0
          actor.set_counter(counter)
          frame += 1
          actor.set_frame(frame)

        if frame > fset:
          frame = 0
          actor.set_frame(frame)

        frame_x = frame * w

        pyray.draw_texture_tiled(
          self._character, 
          pyray.Rectangle(
            frame_x, 
            frame_y, 
            w, 
            h),
          pyray.Rectangle(
            p.get_x(), 
            p.get_y(), 
            w * s, 
            h * s), 
          pyray.Vector2(rp[0], rp[1]), 
          actor.get_rotation(), 
          actor.get_scale(), 
          self._color
          )
        return
      # if not actor.get_movement():
      #   if actor.get_player_action() == Act.JUMP:
      #     actor.set_player_action(Act.IDLE)
      #     return
      # else:
      #   if actor.get_player_action() == Act.IDLE:
      #     actor.set_player_action(Act.JUMP)
      # # actor.set_player_action(Act.IDLE)
      #     return

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

    self._character = pyray.load_texture("frogger/game/images/frogger_sprites.png")

  def _draw_grid(self):
    """Adds grid to screen to assist with debugging."""
    for grid_y in range(0, constants.MAX_Y, constants.CELL_SIZE):
      pyray.draw_line(0, grid_y, constants.MAX_X, grid_y, pyray.GRAY)

    for grid_x in range(0, constants.MAX_X, constants.CELL_SIZE):
        pyray.draw_line(grid_x, 0, grid_x, constants.MAX_Y, pyray.GRAY)
