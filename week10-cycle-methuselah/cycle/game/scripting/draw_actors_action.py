"""
Instructor: Bro. Parrish
Class: CSE 210
Semester: Spring 2022
Team: Methuselah
Assignment: Week 10 Cycle Game
Student: Michael Coleman
"""
import constants

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
        self._timer = 0 #This is the timer for increasing the snake's tail as it moves

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        score1 = cast.get_actor_by_group("scores")[0]
        score2 = cast.get_actor_by_group("scores")[1]
    
        food = cast.get_first_actor("foods")
        powerups = cast.get_actor_by_group("powers")
        snake1 = cast.get_actor_by_group("snakes")[0]
        snake1_seg = snake1.get_snake()
        snake2 = cast.get_actor_by_group("snakes")[1]
        snake2_seg = snake2.get_snake()


        #This adds one to the snake tail after 20 refreshes
        self._timer += 1
        if self._timer >= 20:
            self._timer = 0
            if snake1.get_head().get_color() != constants.WHITE:
                snake1.extend_tail(1)
                snake2.extend_tail(1)
            

        messages = cast.get_actor_by_group("messages")

        self._video_service.clear_buffer()
        self._video_service.draw_actor(food)
        self._video_service.draw_actors(powerups)
        self._video_service.draw_actors(snake1_seg)
        self._video_service.draw_actors(snake2_seg)
        self._video_service.draw_actor(score1)
        self._video_service.draw_actor(score2)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()