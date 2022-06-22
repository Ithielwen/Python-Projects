"""
Instructor: Bro. Parrish
Class: CSE210
Semester: Spring 2022
Team: Methuselah
Assignment: Week 08 Greed Game
Student: Michael Coleman
Class: Mineral Generation
"""
import random

from greed.casting.mineral import Mineral
from greed.casting.gem import Gem
from greed.casting.rock import Rock

from greed.shared.point import Point
from greed.shared.color import Color

class MineralGeneration:
    TEMP_COLS = 60
    TEMP_ROWS = 40
    CELL_SIZE = 15

    #Movement variables
    move_speed = 2

    #Randomization Variables
    min_amount_per_row = 0
    max_amount_per_row = 5
    gem_spawn_chance = .15

    #Visuals
    gem_text = "O"
    rock_text = "*"

    #Timer to make sure there's a gap between rows
    wait_time = 30
    timer = 0



    #Initialize the new generation script by creating a private list of all the minerals
    def __init__(self, cols, rows, size):
        self._all_minerals = []
        self._cols = cols
        self._rows = rows
        self._size = size

    #Setters/Public Methods

    def generate_minerals(self):
        #Check the timer for row gap
        if self.timer > 0:
            self.timer-=1
            return

        #If the timer is below 0, reset it to the wait time between rows
        self.timer = self.wait_time

        #Get a random number of minerals to spawn in the new row
        num_in_row = random.randint(self.min_amount_per_row, self.max_amount_per_row)

        #For each mineral, do a random.random() test - if it's below the gem spawn chance, spawn a gem. Otherwise, spawn a rock
        for num in range(0, num_in_row):
            if random.random() <= self.gem_spawn_chance:
                new_gem = self._create_gem()
                self._all_minerals.append(new_gem)
            else:
                new_rock = self._create_rock()
                self._all_minerals.append(new_rock)

    #Removes the mineral if it's to be destroyed
    def remove_mineral(self, mineral_to_remove):
        self._all_minerals.remove(mineral_to_remove)


    #Private Methods
    def _create_gem(self):
        #Create the gem instance and set the text
        new_mineral = Gem()
        new_mineral.set_text(self.gem_text)

        #Set the gem at a random spot in the row
        x = random.randint(1, self._cols - 1)
        y = -0
        position = Point(x, y)
        position = position.scale(self._size)

        #Give the mineral instance its position and set the velocity to the move speed
        new_mineral.set_position(position)
        new_mineral.set_velocity(Point(0, self.move_speed))

        #Set the color and font size
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        new_mineral.set_color(Color(r, g, b))

        new_mineral.set_font_size(15)

        #Return Gem
        return new_mineral    

    def _create_rock(self):
        #Create the rock instance and set the text
        new_mineral = Rock()
        new_mineral.set_text(self.rock_text) 

        #Set the rock at a random spot in the row
        x = random.randint(1, self._cols - 1)
        y = 0
        position = Point(x, y)
        position = position.scale(self._size)

        #Give the rock instance its position and set the velocity to the move speed
        new_mineral.set_position(position)
        new_mineral.set_velocity(Point(0, self.move_speed))

        #Set the rock color and font size
        new_mineral.set_color(Color(100, 100, 100))

        new_mineral.set_font_size(15)

        #Return Rock
        return new_mineral





    #Getters
    def get_minerals(self):
        return self._all_minerals

