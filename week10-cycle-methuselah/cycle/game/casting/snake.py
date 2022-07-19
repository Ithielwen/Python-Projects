"""
Instructor: Bro. Parrish
Class: CSE 210
Semester: Spring 2022
Team: Methuselah
Assignment: Week 10 Cycle Game
Student: Brennon Jacobson
"""
import constants
from game.casting.actor import Actor
from game.shared.point import Point

class Snake(Actor):
    '''
    The snake/player object
    '''
    def __init__(self, start_x = int(constants.MAX_X/2), start_y = int(constants.MAX_Y/2), head_color = constants.YELLOW, body_color = constants.GREEN):
        super().__init__()
        self._body = []
        self.start_x = start_x
        self.start_y = start_y
        self.head_color = head_color
        self.body_color = body_color
        self._make_snake()

    def _make_snake(self):
        x = self.start_x
        y = self.start_y

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velo = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "#"
            color = self.head_color if i == 0 else self.body_color
            part = Actor()
            part.set_position(position)
            part.set_velocity(velo)
            part.set_text(text)
            part.set_color(color)
            self._body.append(part)
    
    def extend_tail(self, add_length):
        head_size = self.get_head().get_font_size()
        for i in range(add_length):
            tail = self._body[-1]
            velo = tail.get_velocity()
            offset = velo.reverse()
            position = tail.get_position().add(offset)

            part = Actor()
            part.set_position(position)
            part.set_velocity(velo)
            part.set_text("#")
            part.set_font_size(head_size)
            part.set_color(self.body_color)
            self._body.append(part)

    ##### MOVEMENT #####
    def move(self):
        for part in self._body:
            part.move()
        
        for i in range(len(self._body) - 1, 0, -1):
            curr = self._body[i]
            prev = self._body[i -1]
            velo = prev.get_velocity()
            curr.set_velocity(velo)

    def turn(self, velocity):
        head = self.get_head()
        head.set_velocity(velocity)

    ##### GETTERS #####
    def get_snake(self):
        return self._body

    def get_head(self):
        return self._body[0]

    def get_body_color(self):
        return self.body_color

    def set_body_color(self, color):
        self.body_color = color