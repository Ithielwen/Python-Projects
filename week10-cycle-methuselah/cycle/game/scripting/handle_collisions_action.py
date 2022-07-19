"""
Instructor: Bro. Parrish
Class: CSE 210
Semester: Spring 2022
Team: Methuselah
Assignment: Week 10 Cycle Game
Student: Michael Coleman
"""

import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """
    losing_snake = int

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_food_collision(cast)
            self._handle_powers_collision(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    def _game_over(self):
        self._is_game_over = True

    def get_is_game_over(self):
        return self._is_game_over

    def _handle_food_collision(self, cast):
        """Updates the score nd moves the food if the snake collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score1 = cast.get_actor_by_group("scores")[0]
        score2 = cast.get_actor_by_group("scores")[1]
    
        food = cast.get_first_actor("foods")
        # snake = cast.get_first_actor("snakes")

        snakes = cast.get_actor_by_group("snakes")
        snake_num = 0

        for snake in snakes:
            snake_num += 1

            head = snake.get_head()
            if head.get_position().equals(food.get_position()):
                points = food.get_points()
                snake.extend_tail(points)
                if snake_num == 1:
                    score1.add_points(points)
                else:
                    score2.add_points(points)
                food.reset()

    def _handle_powers_collision(self, cast):
        """Updates the score, applies the power up, and moves the power up if the snake collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score1 = cast.get_actor_by_group("scores")[0]
        score2 = cast.get_actor_by_group("scores")[1]
    
        powers = cast.get_actor_by_group("powers")
        # snake = cast.get_first_actor("snakes")

        snakes = cast.get_actor_by_group("snakes")
        snake_num = 0

        for snake in snakes:
            snake_num += 1

            head = snake.get_head()
            for power in powers:
                if head.get_position().equals(power.get_position()):
                    points = power.get_points()
                    power.use_ability(snake)

                    if snake_num == 1:
                        score1.add_points(points)
                    else:
                        score2.add_points(points)
                    power.reset()
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        # snake = cast.get_first_actor("snakes")
        snakes = cast.get_actor_by_group("snakes")

        collision_positions = []
        #Store a local list of all heads and all segments, then fill that from both snakes
        '''
        for snake in snakes:
            snake_body = snake.get_snake()
            for part in snake_body:
                collision_positions.append(part)

            found = 0

            for pos in collision_positions:
                if pos in collision_positions:
                    found += 1
            
            if found > 1:
                self._game_over()
                self.losing_snake = snakes.index(snake)
        '''
        all_heads = []
        all_segments = []
        for snake in snakes:
            all_heads.append(snake.get_head())

            _segments = snake.get_snake()[1:]
            for seg in _segments:
                all_segments.append(seg)

        #Loop through all of the segments and heads to determine collision
        for head in all_heads:
           for body in all_segments:
                
                if head.get_position().equals(body.get_position()):
                    self._is_game_over = True
                    self.losing_snake = all_heads.index(head)
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            snakes = cast.get_actor_by_group("snakes")
            segments = []
            for snake in snakes:
                _segments = snake.get_snake()
                for seg in _segments:
                    segments.append(seg)
            food = cast.get_first_actor("foods")
            powers = cast.get_actor_by_group("powers")

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text(f"Game Over! Player {self.losing_snake + 1} loses!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segments:
                segment.set_color(constants.WHITE)
            food.set_color(constants.WHITE)

            for power in powers:
                power.set_color(constants.WHITE)