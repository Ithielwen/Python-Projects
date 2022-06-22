import pyray
import os
import random

from casting.mineral import Mineral
from casting.gem import Gem
from casting.rock import Rock

from shared.point import Point
from shared.color import Color

import sys

print("Pythonpath:", sys.path)
print()
print()
print("THE DIRECTORY " + os.getcwd())

class MineralGeneration:
    TEMP_COLS = 60
    TEMP_ROWS = 40
    CELL_SIZE = 15

    #Movement variables
    move_speed = 1

    #Randomization Variables
    min_amount_per_row = 5
    max_amount_per_row = 10
    gem_spawn_chance = .1

    wait_time = 30
    timer = 0

    def __init__(self):
        self._all_minerals = []

    #Setters
    def _generate_minerals(self):
        if self.timer > 0:
            self.timer-=1
            return

        self.timer = self.wait_time

        num_in_row = random.randint(self.min_amount_per_row, self.max_amount_per_row)
        for num in range(0, num_in_row):
            if random.random() <= self.gem_spawn_chance:
                self._create_gem()

            else:
                self._create_rock()

    def _remove_mineral(self, group):
        """Removes a mineral from the given group.
        
        Args:
            group (string): The name of the group.
            mineral (Mineral): The mineral to remove.
        """
        # if group in self._all_minerals:
            # self._all_minerals[group].remove(mineral)
        for mineral in group:
            if mineral.get_text() == "O":
                group.remove(mineral)
            if mineral.get_text() == "X":
                group.remove(mineral)
        # for i, obj in enumerate(group):
            # if msg["msgID"] == desired_id:
            #     del group[i]

    def _create_gem(self):
        new_mineral = Gem()
        new_mineral.set_text("O")

        x = random.randint(1, self.TEMP_COLS - 1)
        y = -0
        position = Point(x, y)
        position = position.scale(self.CELL_SIZE)

        new_mineral.set_position(position)
        new_mineral.set_velocity(Point(0, self.move_speed))

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        new_mineral.set_color(Color(r, g, b))

        new_mineral.set_font_size(15)

        self._all_minerals.append(new_mineral)       

    def _create_rock(self):
        new_mineral = Rock()
        new_mineral.set_text("X") 

        x = random.randint(1, self.TEMP_COLS - 1)
        y = 0
        position = Point(x, y)
        position = position.scale(self.CELL_SIZE)

        new_mineral.set_position(position)
        new_mineral.set_velocity(Point(0, self.move_speed))

        new_mineral.set_color(Color(100, 100, 100))

        new_mineral.set_font_size(15)

        self._all_minerals.append(new_mineral)  

    #Getters
    def _get_minerals(self):
        return self._all_minerals

    