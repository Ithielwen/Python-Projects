"""
Instructor: Bro. Parrish
Class: CSE210
Semester: Spring 2022
Team: Methuselah
Assignment: Week 08 Greed Game
Student: Brennon Jacobson
Class: Display
"""

import pyray

class Display:
    def __init__(self, caption, width, height, cell_size, frame_rate, debug = False):
        self._caption = caption
        self._width = width
        self._height = height
        self._cell_size = cell_size
        self._frame_rate = frame_rate
        self._debug = debug
    
    def close_window(self):
        '''Close the display window'''
        pyray.close_window()

    def clear(self):
        '''Screen prep for new drawing'''
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)
        if self._debug == True:
            self._draw_grid()

    def _draw_grid(self):
        '''Set up a grid to play'''
        for y in range(0, self._height, self._cell_size):
            pyray.draw_line(0, y, self._width, y, pyray.GRAY)

        for x in range(0, self._width, self._cell_size):
            pyray.draw_line(x, 0, x, self._height, pyray.GRAY)
    
    def is_window_open(self):
        '''Checks if Window is Open'''
        return not pyray.window_should_close()

    def init_window(self):
        '''Set up Window and Frame Rate'''
        pyray.init_window(self._width, self._height, self._caption)
        pyray.set_target_fps(self._frame_rate)

    def draw_mineral(self, mineral):
        '''draw an individual mineral (rock/gem)'''
        text = mineral.get_text()
        posX = mineral.get_position().get_x()
        posY = mineral.get_position().get_y()
        fontSize = mineral.get_font_size()
        color = mineral.get_color().to_tuple()

        pyray.draw_text(text, posX, posY, fontSize, color)

    def draw_minerals(self, minerals):
        '''loop through minerals and draw each mineral'''
        for mineral in minerals:
            self.draw_mineral(mineral)

    def end_drawing(self):
        '''End canvas drawing and swap buffers (double buffering)'''
        pyray.end_drawing()

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def get_cell_size(self):
        return self._cell_size

    def get_rows(self):
        return self._height / self._cell_size

    def get_cols(self):
        return self._width / self._cell_size