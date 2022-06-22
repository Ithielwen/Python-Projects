from greed.services.generation import *
from greed.casting.mineral import Mineral
from greed.services.display import Display

TEMP_SCREEN_WIDTH = 900
TEMP_SCREEN_HEIGHT = 600
TEMP_CELL_SIZE = 15
CAPTION = "Testing Game"

def start_game():
    mineral_generation = MineralGeneration()
    video_service = Display(CAPTION, TEMP_SCREEN_WIDTH, TEMP_SCREEN_HEIGHT, TEMP_CELL_SIZE, 60, False)


    video_service.init_window()
    while video_service.is_window_open():
        move_stuff(video_service, mineral_generation)
        draw_stuff(video_service, mineral_generation)

def move_stuff(video_service, mineral_generation):
    minerals = mineral_generation._get_minerals()
    for mineral in minerals:
        mineral.move_next(TEMP_SCREEN_WIDTH, TEMP_SCREEN_HEIGHT)


def draw_stuff(video_service, mineral_generation):
    video_service.clear()

    mineral_generation._generate_minerals()
    minerals = mineral_generation._get_minerals()
    video_service.draw_minerals(minerals)

    video_service.end_drawing()


start_game()