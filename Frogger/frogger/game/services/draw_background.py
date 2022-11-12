"""
Instructor: Bro. Parrish
Class: CSE 210
Semester: Spring 2022
Team: Methuselah
Assignment: Final Project
Student: Michael Coleman
"""

from game.shared.point import Point
import pyray
import constants


class Background():

    BIOME = { 
        "Field":[Point(130, 160), Point(110,110)],
        "Pavement": [Point(320, 160), Point(100,100)],
        "Water": [Point(230, 160), Point(100,100)]
        } 
        
    # Initialize the generator's position (should be the beginning or end of one specific row) and set the direction the objects in that row will be moving (0 for left, 1 for right)
    def __init__(self, texture):
       self.texture = texture
       #self._draw_road(75)
       #self._draw_field(0)
       self._draw_field(35)
       self._draw_river(110)
       self._draw_river(185)
       self._draw_road(335)
       self._draw_road(410)
       self._draw_field(260)
       self._draw_field(485)
       self._draw_field(525)
       
    
    # Override the generate method from the ObjectGenerator class
    def _draw_field(self, top_y):
        '''Get a grass object from the sprite and draw a horizontal row at position {top_y}'''
        grass = pyray.Rectangle(self.BIOME["Field"][0].get_x(),self.BIOME["Field"][0].get_y(),self.BIOME["Field"][1].get_x(),self.BIOME["Field"][1].get_y())
        #top row
        top_x = -15
        height = 85
        width = 85

        while top_x < constants.MAX_X:
            drawing_square = pyray.Rectangle(top_x, top_y, width + 10, height)

            myVector = pyray.Vector2(0,0)

            pyray.draw_texture_tiled(self.texture,grass,drawing_square,myVector, 0, 1, pyray.RAYWHITE)

            top_x += width - 10

        #middle row

        #win row
        pass

    def _draw_road(self, top_y):
        '''Get a pavement object from the sprite and draw a horizontal row at position {top_y}'''
        road = pyray.Rectangle(self.BIOME["Pavement"][0].get_x(),self.BIOME["Pavement"][0].get_y(),self.BIOME["Pavement"][1].get_x(),self.BIOME["Pavement"][1].get_y())
        
        #top row
        top_x = 0
        height = 85
        width = 85

        while top_x < constants.MAX_X:
            drawing_square = pyray.Rectangle(top_x, top_y, width, height)

            myVector = pyray.Vector2(0,0)

            pyray.draw_texture_tiled(self.texture,road,drawing_square,myVector, 0, 1, pyray.RAYWHITE)

            top_x += width - 10
        

    def _draw_river(self, top_y):
        '''Get a water object from the sprite and draw a horizontal row at position {top_y}'''
        water = pyray.Rectangle(self.BIOME["Water"][0].get_x(),self.BIOME["Water"][0].get_y(),self.BIOME["Water"][1].get_x(),self.BIOME["Water"][1].get_y())
        #top row
        top_x = 0
        height = 85
        width = 85

        while top_x < constants.MAX_X:
            drawing_square = pyray.Rectangle(top_x, top_y, width, height)

            myVector = pyray.Vector2(0,0)

            pyray.draw_texture_tiled(self.texture,water,drawing_square,myVector, 0, 1, pyray.RAYWHITE)

            top_x += width - 10
    