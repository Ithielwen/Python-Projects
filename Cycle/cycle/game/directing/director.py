"""
Instructor: Bro. Parrish
Class: CSE 210
Semester: Spring 2022
Team: Methuselah
Assignment: Week 10 Cycle Game
Student: Mark Hammer
"""

# Import section
from game.scripting.handle_collisions_action import HandleCollisionsAction

class Director:
    """
    Purpose: Controls the sequence of the game play
    Attributes:
        _video_service: Creates the display
    """
    
    def __init__(self, video_service):
        """
        Constructs a new version of Director
        """
        self._video_service = video_service
        self._is_game_over = False

    def start_game(self, cast, script):
        """
        handles starting the game
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._execute_actions("input", cast, script)
            self._execute_actions("update", cast, script)
            self._execute_actions("output", cast, script)
        self._video_service.close_window()

    def _execute_actions(self, group, cast, script):
        """
        handles game till collission happens
        """
        actions = script.get_actions(group)
        for action in actions:
            action.execute(cast, script)

            if isinstance(action, HandleCollisionsAction):
                self._is_game_over = action.get_is_game_over()