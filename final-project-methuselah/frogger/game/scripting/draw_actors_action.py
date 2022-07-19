"""
Instructor: Bro. Parrish
Class: CSE 210
Semester: Spring 2022
Team: Methuselah
Assignment: Week 13 Frogger Game
Student: Michael Coleman
"""

from game.scripting.action import Action

class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        frog = cast.get_first_actor("frog")
        skull = cast.get_first_actor("skull")
        score = cast.get_first_actor("score")
        vehicles = cast.get_actors("vehicles")
        logs = cast.get_actors("logs")

        

        self._video_service.clear_buffer()
        self._video_service.draw_background()
        self._video_service.draw_text(score)
        self._video_service.draw_actors(logs)
        self._video_service.draw_actor(skull)
        self._video_service.draw(frog)
        self._video_service.draw_actors(vehicles)

        if cast.get_first_actor("over"):
            game_over = cast.get_first_actor("over")
            self._video_service.draw_text(game_over, True)
        
        self._video_service.flush_buffer()