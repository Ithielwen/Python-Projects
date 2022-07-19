"""
Instructor: Bro. Parrish
Class: CSE 210
Semester: Spring 2022
Team: Methuselah
Assignment: Week 13 Frogger Game
Student: Michael Coleman
"""

import constants
from game.scripting.action import Action
from game.shared.point import Point
from game.directing.play_sound import PlaySound
from game.casting.game_over import GameOver

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """
    def __init__(self, display):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._display_controller = display

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        print()
        print()
        if not self._is_game_over:
            self._handle_screen_collision(cast)
            self._handle_enemy_collision(cast)
            self._handle_log_collision(cast)
            self._handle_end_zone_collision(cast, script)
        
        else:
            self._handle_game_over(cast)

    def _game_over(self):
        self._is_game_over = True

    def get_is_game_over(self):
        return self._is_game_over

    # Handles the objects reaching the end of the screen so they don't wrap
    def _handle_screen_collision(self, cast):
        vehicles = cast.get_actors("vehicles")
        logs = cast.get_actors("logs")
        for vehicle in vehicles:
            if vehicle.get_moving_right() and vehicle.get_position().get_x() >= constants.MAX_X - 5:
                cast.remove_actor("vehicles", vehicle)
            else:
                if not vehicle.get_moving_right() and vehicle.get_position().get_x() <= 5:
                    cast.remove_actor("vehicles", vehicle)
        
        for log in logs:
            if log.get_moving_right() and log.get_position().get_x() >= constants.MAX_X - 5:
                cast.remove_actor("logs", log)
            else:
                if not log.get_moving_right() and log.get_position().get_x() <= 5:
                    cast.remove_actor("logs", log)

    # Detects the collision with the enemies and ends the game if the frog is colliding with one
    def _handle_enemy_collision(self, cast):
        frog = cast.get_first_actor("frog")
        frog_x = frog.get_position().get_x()
        frog_y = frog.get_position().get_y()
        vehicles = cast.get_actors("vehicles")
        score = cast.get_first_actor("score")
        sound_effects = PlaySound()

        for vehicle in vehicles:
            vehicle_min_x = vehicle.get_position().get_x() - (vehicle.get_sprite()[1].get_x() / 2)
            vehicle_max_x = vehicle.get_position().get_x() + (vehicle.get_sprite()[1].get_x() / 2)
            vehicle_min_y = vehicle.get_position().get_y() - (vehicle.get_sprite()[1].get_y() / 2)
            vehicle_max_y = vehicle.get_position().get_y() + (vehicle.get_sprite()[1].get_y() / 2)

            if frog_y == vehicle.get_position().get_y():
                if frog_x >= vehicle_min_x and frog_x <= vehicle_max_x:
                    sound_effects.play_squash()
                    print(score.get_lives())
                    score.lose_life()
                    if score.get_lives() > 0:
                        self._show_death(cast)
                        self._respawn_frog(cast)
                    else:
                        self._show_death(cast)
                        self._game_over()

    # Handle water collision - called from the _handle_log_collision method if the player isn't on a log
    def _handle_water_collision(self, cast):
        frog = cast.get_first_actor("frog")
        frog_y = frog.get_position().get_y()
        water_zones = cast.get_zones("water")
        score = cast.get_first_actor("score")
        sound_effects = PlaySound()
        
        for zone in water_zones:
            if frog_y == zone.get_position().get_y():
                sound_effects.play_plunk()
                print(score.get_lives())
                score.lose_life()
                if score.get_lives() > 0:
                    self._show_death(cast)
                    self._respawn_frog(cast)
                else:
                    self._show_death(cast)
                    self._game_over()     

    
    # Detects log collision and sets the player's velocity to the log's velocity
    def _handle_log_collision(self, cast):
        frog = cast.get_first_actor("frog")
        frog_x = frog.get_position().get_x()
        frog_y = frog.get_position().get_y()
        logs = cast.get_actors("logs")

        for log in logs:
            log_min_x = log.get_position().get_x() - ((log.get_sprite()[1].get_x() * log.get_scale()) / 2)
            log_max_x = log.get_position().get_x() + ((log.get_sprite()[1].get_x() * log.get_scale()) / 2)

            if frog_y == log.get_position().get_y():
                if frog_x >= log_min_x and frog_x <= log_max_x:
                    frog.set_velocity(log.get_velocity())
                    return
        
        self._handle_water_collision(cast)
    
    # Detects the end zone collision
    def _handle_end_zone_collision(self, cast, script):
        frog = cast.get_first_actor("frog")
        frog_y = frog.get_position().get_y()
        end_zone = cast.get_zones("end_zone")
        score = cast.get_first_actor("score")
        
        for zone in end_zone:
            if frog_y == zone.get_position().get_y():
                score.add_points(100)
                self._hide_death(cast)
                self._respawn_frog(cast)
                stage = round((score.get_points() - 100) / 100)
                generators = script.get_actions("generate")
                for generator in generators:
                    if generator.get_velocity():
                        if generator.get_velocity() < constants.STAGE_MAX_SPEED:
                            generator.update_velocities(constants.STAGE_SPEED)
                        if generator.get_time_between() > constants.STAGE_MIN_BETWEEN:
                            generator.update_time_between(constants.STAGE_TIME_BETWEEN)
                

    # This method handles the game over functionality
    def _handle_game_over(self, cast):
        frog = cast.get_first_actor("frog")
        frog.set_sprite(Point(0, 0), Point(0, 0))
        game_over_text = GameOver()
        cast.add_actor("over", game_over_text)

    def _respawn_frog(self, cast):
        '''reset the frog position, velocity and rotation to the starting point after death or completeing a level'''

        frog = cast.get_first_actor("frog")
        frog_start =  Point(constants.MAX_X / 2, constants.MAX_Y - constants.CELL_SIZE)
        frog.set_position(frog_start)
        frog.set_velocity(Point(0,0))
        frog.set_rotation(180)

    def _show_death(self, cast):
        """set skull to frog death position"""
        skull = cast.get_first_actor("skull")
        frog = cast.get_first_actor("frog")
        skull.set_position(Point(frog.get_position().get_x(), frog.get_position().get_y()))

    def _hide_death(self, cast):
        """hide skull from view"""
        skull = cast.get_first_actor("skull")
        skull.set_position(Point(-56, -72))
