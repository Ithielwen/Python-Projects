import pyray
from greed.player.spawn import Spawn
from greed.player.banner import Message
from greed.shared.point import Point

class Collision(Spawn):
  # def __init__(self, gems, rocks):
  def __init__(self):
    # self._gem = gems
    # self._rock = rocks
    self._score = 0

  # def check_collision(self, gems, rocks, player):
  def check_collision(self, generator, player, banner):
    quarry = generator.get_minerals()

    loc = player.get_position()
    loc_start_x = loc.get_x()
    loc_start_y = loc.get_y()

    loc = Point(loc_start_x, loc_start_y).scale(15)

    # create player bounding box
    # loc_point = Point(loc_start_x, loc_start_y).boxend(15, 30)
    # loc_end_x = loc_point.get_x()
    # loc_end_y = loc_point.get_y()

    # loc_x = str(player.get_position()[0])
    # rx = cast.get_first_mineral(generator)
    
    rx = generator.get_minerals()[0].get_position().get_x()
    rx = str(rx)
    ry = generator.get_minerals()[0].get_position().get_y()
    ry = str(ry)
    points = self._score

    for stone in quarry:
    # for i in range(len(quarry)):
    #   stone = quarry[i]

      stone_start_x = stone.get_position().get_x()
      stone_start_y = stone.get_position().get_y()
      
      stone_loc = Point(stone_start_x, stone_start_y).scale(15)

      #create stone bounding box
      # stone_boxend = stone.get_position().boxend(15, 30)
      # stone_end_x = stone_boxend.get_x()
      # stone_end_y = stone_boxend.get_y()

      # if pyray.check_collision_lines((loc_start_x, loc_start_y), (loc_end_x, loc_end_y), (stone_start_x, stone_start_y), (stone_end_x, stone_end_y), 1):
      if loc.equals(stone_loc):
        points += 1
        generator.remove_mineral(quarry)
        if stone.get_text() == "O":
            # self._message = "Shiny!"
            banner.set_message("Shiny!")
        if stone.get_text() == "X":
            # self._message = "Ouch!"
            banner.set_message("Ouch!")
        # rx = stone.get_position()
        # rx = str(rx[0])
        # cast.remove_mineral(tuple(quarry), stone)
        # cast.remove_mineral(generator, stone)

    greet = banner.get_message()
    self.draw_message(str(loc_start_x), rx, ry, str(points), greet)

  def draw_message(self, msg, rx, ry, points, greet):
    pyray.draw_text("Player x:", 10, 575, 24, (255, 255, 255))
    pyray.draw_text(msg, 125, 575, 24, (255, 255, 255))
    pyray.draw_text("1st Rock (x, y):", 200, 575, 24, (255, 255, 255))
    pyray.draw_text(rx, 390, 575, 24, (255, 255, 255))
    pyray.draw_text(ry, 440, 575, 24, (255, 255, 255))
    pyray.draw_text("Score:", 540, 575, 24, (255, 255, 255))
    pyray.draw_text(points, 640, 575, 24, (255, 255, 255))
    pyray.draw_text(greet, 700, 575, 24, (255, 255, 255))
    # pyray.draw_text(ry, 125, 575, 24, (255, 255, 255))